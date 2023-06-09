# Create your CSV

Generate a CSV of your data that contains a list of all of your columns in the database in the following format.

| col\_name | col\_description | col\_type | sort\_order | database | schema | name  | description            | is\_view | last\_updated\_time |
| --------- | ---------------- | --------- | ----------- | -------- | ------ | ----- | ---------------------- | -------- | ------------------- |
| id        | ID of the user   | int       | 1           | secoda   | public | users | the table of all users | false    | None                |
| name      | name of the user | char      | 2           | secoda   | public | users | the table of all users | false    | None                |

* **col\_name**: the name of the column
* **col\_description**: the description of the column
* **col\_type**: can be any string
* **col\_sort\_order**: can be any integer. Can also just set it to 0
* **database**: the name of the database the column is in
* **schema**: the name of the schema the column is in
* **name**: the name of the table the column is in
* **description**: the description for the table this column is in
* **is\_view**: boolean value on wether or not the table is a view
* **last\_updated\_time**: timestamp of when the table was last updated

For example with Snowflake, this CSV can be generated with a SQL statement like this.&#x20;

```sql
SELECT DISTINCT
    lower(c.column_name)                                    AS col_name,
    c.comment                                               AS col_description,
    lower(c.data_type)                                      AS col_type,
    lower(c.ordinal_position)                               AS col_sort_order,
    lower(c.table_catalog)                                  AS database,
    lower(c.table_schema)                                   AS schema,
    lower(c.table_name)                                     AS name,
    t.comment                                               AS description,
    decode(lower(t.table_type), 'view', 'true', 'false')    AS is_view,
    DATE_PART(EPOCH, t.last_altered)                        AS last_updated_time
FROM {database.title}.INFORMATION_SCHEMA.COLUMNS AS c
LEFT JOIN {database.title}.INFORMATION_SCHEMA.TABLES t ON c.TABLE_NAME = t.TABLE_NAME
 AND c.TABLE_SCHEMA = t.TABLE_SCHEMA
WHERE c.TABLE_SCHEMA not in ({','.join(SnowflakeConnectionConstants.DEFAULT_IGNORED_SCHEMAS)}) \
        AND c.TABLE_SCHEMA not like 'STAGE_%' \
        AND c.TABLE_SCHEMA not like 'HIST_%' \
        AND c.TABLE_SCHEMA not like 'SNAP_%' \
        AND lower(c.TABLE_SCHEMA) not like 'dbt_cloud_pr%' \
        AND lower(c.TABLE_SCHEMA) not like 'ci_impact_resilience_%' \
        AND lower(c.COLUMN_NAME) not like 'dw_%' \
```

Feel free to reach out to us for more guidance on how to generate CSVs.&#x20;

If you'd like to add custom properties to your resources, you can add extra columns with the heading of the custom property you'd like to add.&#x20;

Now it's time to upload the CSV!&#x20;
