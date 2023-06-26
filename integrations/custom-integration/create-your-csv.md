# Create your CSV

Generate a CSV of your data that contains a list of all of your columns in the database in the following format.

| col\_name | col\_description | col\_type | sort\_order | database | schema | name  | description            | is\_view | last\_updated\_time |
| --------- | ---------------- | --------- | ----------- | -------- | ------ | ----- | ---------------------- | -------- | ------------------- |
| id        | ID of the user   | int       | 1           | secoda   | public | users | the table of all users | false    | None                |
| name      | name of the user | char      | 2           | secoda   | public | users | the table of all users | false    | None                |

* **col\_name** -> The name of the column (ex. `event_name`)
  * :exclamation:**Required**
  * Column names can be made up of numbers, letters, and any special characters **except** periods (ex. `event.name` :thumbsdown:).
  * :information\_source: Column names will be made lower case when brought into Secoda
* **col\_description** -> The description of the column
  * Column descriptions can be made up of numbers, letters, and any special characters.
  * :information\_source: There is no additional validation or transformation on this field. The way you input it into the CSV is the way it will show in the UI.&#x20;
* **col\_type** -> The type of data in the column (ex. `character varying(25)`)
  * Column types can be made up of numbers, letters, and any special characters.
  * :information\_source: There is no additional validation or transformation on this field. The way you input it into the CSV is the way it will show in the UI.&#x20;
* **col\_sort\_order** -> The default order that the columns should be sorted in
  * Sort order must be an integer.
  * :information\_source: If sort order is not important, you can set the field to `0` and it will default to alphabetical order.
* **name** -> The name of the _table_ the column belongs to
  * :exclamation:**Required**
  * Table names can be made up of numbers, letters, and any special characters **except** periods.&#x20;
* **description** -> The description for the _table_ the column belongs to.
  * Table descriptions can be made up of numbers, letters, and any special characters.
  * :information\_source: There is no additional validation or transformation on this field. The way you input it into the CSV is the way it will show in the UI.&#x20;
* **database** -> The name of the database the column and table belong to.
  * :exclamation:**Required**
  * Column names can be made up of numbers, letters, and any special characters **except** periods.
* **schema** -> The name of the schema the column and table belong to.
  * :exclamation:**Required**
  * Column names can be made up of numbers, letters, and any special characters **except** periods.
* **is\_view** -> Indicates whether the _table_ is a view (generated from a query).
  * Is View is a boolean value expecting either `true` or `false`.
* **last\_updated\_time** -> The timestamp of when the _table_ was last updated.
  * Last updated time is a timestamp that expects an integer value of the Unix Epoch time.&#x20;

{% hint style="info" %}
For rows which contain columns belonging to the **same** table, the `is_view`, `last_updated_time`, `name`, and `description` fields should all be identical.&#x20;

Ex. If there are 5 columns all belonging to the table `TestTable`, each row for the columns in the CSV would have a name of `TestTable` and an identical description.&#x20;
{% endhint %}

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

At this point, you cannot add custom properties or tags using the CSV upload. However, you can add custom properties and tags after the initial extraction has been done using the [Import/Export ](../../resource-and-metadata-management/import-and-export-data.md)feature.&#x20;

Now it's time to upload the CSV!&#x20;
