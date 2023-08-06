import os
from concurrent.futures import ThreadPoolExecutor, as_completed

from tqdm import tqdm

from .adapters import get_adapter
from .templater import get_template
from .utils import DEFAULT_DBT_PROFILE_PATH, read_dbt_profile, list_yaml, write_file, read_source_yaml

template = get_template("base_model.sql")


def make_model_sql(*args, **kwargs):
    sql = template.render(*args, **kwargs)
    return sql


def generate_base_from_sources(profile, output_folder, source_path):
    sources = read_source_yaml(source_path)

    for source in sources:
        source_database = source.get("database")
        source_name = source["name"]
        source_identifier = source.get("schema", source_name)

        # Make folder for each source
        sub_folder = os.path.join(output_folder, source_name)
        os.makedirs(sub_folder, exist_ok=True)

        # Adapter to connect database
        adapter = get_adapter(profile, database=source_database)

        for table in source["tables"]:
            table_name = table["name"]
            table_identifier = table.get("identifier", table_name)

            # Identifier is name used in database
            columns = adapter.list_columns(source_identifier, table_identifier)

            # While, name is used in dbt
            sql_content = make_model_sql({"source_name": source_name, "table_name": table_name, "columns": columns})
            sql_path = os.path.join(sub_folder, f"stg__{table_name}.sql")
            write_file(sql_path, sql_content)


def generate_base_model(profile_path, output_folder, source_path, profile_name="default", target="dev", threads=None):
    os.makedirs(output_folder, exist_ok=True)

    profile = read_dbt_profile(profile_path, profile_name=profile_name, target=target)
    paths = list_yaml(source_path)

    with ThreadPoolExecutor(threads) as executor:
        futures = {}
        for fp in paths:
            futures[
                executor.submit(generate_base_from_sources, profile, output_folder, fp)
            ] = fp

        for ft in tqdm(as_completed(futures), total=len(futures)):
            pass

    print("Done")


def run(args):
    generate_base_model(
        profile_path=args.profile_path,
        output_folder=args.output_folder,
        source_path=args.source_path,
        profile_name=args.profile_name,
        target=args.target,
        threads=args.threads,
    )


def config_parser(parser):
    parser.set_defaults(func=run)
    parser.add_argument("source_path", type=str, help="Path to dbt source YAML.")
    parser.add_argument(
        "output_folder",
        type=str,
        help="Folder to write base models.",
    )
    parser.add_argument(
        "--profile-path",
        type=str,
        default=DEFAULT_DBT_PROFILE_PATH,
        help=("Path to dbt profile YAML." f" Default is {DEFAULT_DBT_PROFILE_PATH}"),
    )
    parser.add_argument("--profile-name", type=str, default="default", help="Dbt profile name. Default is `default`.")
    parser.add_argument("--target", type=str, default="dev", help="Dbt profile target. Default is `dev`.")
    parser.add_argument(
        "--threads",
        type=int,
        default=None,
        help="Max threads. Default is your machine number of threads.",
    )
