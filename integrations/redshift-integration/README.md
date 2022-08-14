---
description: An overview of the Secoda integration with Redshift
---

# Redshift Integration

{% content-ref url="redshift.md" %}
[redshift.md](redshift.md)
{% endcontent-ref %}

{% content-ref url="redshift-metadata.md" %}
[redshift-metadata.md](redshift-metadata.md)
{% endcontent-ref %}

After connecting Redshift to Secoda, to view the metadata associated with one of your Redshift tables, visit the [catalog](https://app.secoda.co/catalog) page and click on the title of your Redshift table. That link will bring you to the following page.

![](<../../.gitbook/assets/image (5) (2).png>)

**Tables**

The tables associated with the schemas that have been selected in your Redshift integration will be imported. If a [comment ](https://docs.snowflake.com/en/sql-reference/sql/comment.html)is present on the table, that comment will be brought in as a description.

**Columns**

The columns associated with the tables will be imported into Secoda. The column name, type primary key, and comment will be brought in. Optionally, clicking the "Run Profiler" button will show a distribution of each Redshift column.

**Lineage**

Table and column lineage is automatically imported into Secoda. The last day of queries are parsed with our lineage parser to build a map of the relationships between columns and tables.

![](<../../.gitbook/assets/image (11).png>)

**Queries**

The queries from the last day of query history in Redshift will be brought in and automatically associated with the tables that they reference.
