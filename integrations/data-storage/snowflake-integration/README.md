---
description: An overview for the Snowflake integration with Secoda
---

# Snowflake Integration

{% content-ref url="snowflake.md" %}
[snowflake.md](snowflake.md)
{% endcontent-ref %}

{% content-ref url="snowflake-metadata.md" %}
[snowflake-metadata.md](snowflake-metadata.md)
{% endcontent-ref %}

After connecting Snowflake, to view the metadata associated with one of your Snowflake tables, visit the [catalog](https://app.secoda.co/catalog) page and click on the title of your Snowflake table. That link will bring you to the following page.

![](<https://secoda-public-media-assets.s3.amazonaws.com/image%20(10)%20(1)%20(1).png>)

**Tables**

The tables associated with the schemas that have been selected in your Snowflake integration will be imported. If a [comment ](https://docs.snowflake.com/en/sql-reference/sql/comment.html)is present on the table, that comment will be brought in as a description.

**Columns**

The columns associated with the tables will be imported into Secoda. The column name, type and comment will be brought in. Optionally, clicking the "Run Profiler" button will show a distribution of each Snowflake column.

**Lineage**

Table and column lineage is automatically imported into Secoda. The last day of queries are parsed with our lineage parser to build a map of the relationships between columns and tables.

![](<https://secoda-public-media-assets.s3.amazonaws.com/image%20(6)%20(2).png>)

**Queries**

The queries from the last day of query history in Snowflake will be brought in and automatically associated with the tables that they reference.
