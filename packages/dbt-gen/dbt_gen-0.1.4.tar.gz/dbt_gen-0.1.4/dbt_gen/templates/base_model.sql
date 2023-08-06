with source as (

    select * from {% raw %}{{ source({% endraw %}'{{ source_name }}', '{{ table_name }}'{% raw %}) }}{% endraw %}

),

renamed as (

    select
        {%- for column in columns %}
        {{ column.name | lower }}{{"," if not loop.last}}
        {%- endfor %}

    from source

)

select * from renamed
