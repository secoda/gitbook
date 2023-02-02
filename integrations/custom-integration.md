---
description: How to build a custom integration in Secoda
---

# Custom Integration

### Create an Integration on Secoda

You only have to do this step once. Create an Integration on Secoda either using the API or the interface on `https://app.secoda.co/integrations`

```python
import requests

headers = dict(
    Authorization="Bearer <your-api-token>"
)
integration_type = "bigquery"

response = requests.post(
    "https://api.secoda.co/integration/integrations/",
    json=dict(type=integration_type, name="My Custom Integration", credentials={}),
    headers=headers
).json()
print("Integration ID", response.get("id"))
```

Please only do this step once to get the integration ID. You can change the integration type to “snowflake”, “oracle”, “postgres”, etc.

### Generate a CSV of Your Data

Generate a CSV of your data that contains a list of all of your columns in the database in the following format

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

For example with snowflake, this CSV can be generated with a SQL statement like this

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

### Upload the CSV

Upload the file to Secoda by making a request to the `https://eapi.secoda.co/integration/integrations/<integration-id>/import_metadata/`

```python
import requests

integration_id = "integration id from step 1"
headers = dict(
    Authorization="Bearer <your-api-token>"
)

requests.post(
    f"https://eapi.secoda.co/integration/integrations/{integration_id}/import_metadata/",
    files=dict(file=open("dump.csv", "rb")),
    headers=headers
)
```

Now if you open Secoda and navigate to the integration page, you should see an extraction running for your custom integration
