---
description: >-
  After connecting your data to Secoda, you'll be able to get a high level view
  of your data lineage both at the table and column level.
---

# Lineage

In the context of Secoda, data lineage refers to the process of tracking and documenting the relationships between different data assets within an organization. This can include information about where data comes from, how it has been transformed or modified over time, and how it is being used.

Data lineage is an important part of data governance and can help organizations understand the origin and history of their data, identify potential sources of errors or inconsistencies, and ensure that data is being used appropriately.

In Secoda, data lineage is typically tracked and documented through the creation of data lineage diagrams or graphs that show the relationships between different data assets. These diagrams can include information about the data sources, transformations applied to the data, and the resulting data outputs.

Secoda also provides tools and features for automatically generating data lineage documentation, such as descriptions, definitions, and metadata, to help others understand and use the data more effectively.

Overall, data lineage is an important aspect of data management and can help organizations improve transparency, trustworthiness, and understanding of their data.

## **Everything about Secoda Lineage** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

Secoda automatically extracts queries to generate data lineage. This can help data teams identify the downstream and upstream dependencies of a table easily.&#x20;

On each dependency, you will be able to see how many levels away a particular table is.&#x20;

1. Select the data asset that you'd like to view the lineage of from the Data button in the navigation bar, or, search for it using the search bar.&#x20;
2. After selecting the asset you'd like to view, click on the **Lineage** tab. In the Lineage tab you can toggle on List view, or Column view to see Column Level lineage. See below for an example.&#x20;

{% embed url="https://www.loom.com/share/68c2c5a9b5454adfaa3c3e3b91b9df44" %}

## How is Lineage Created?

When you connect a data source to Secoda, Lineage is automatically generated from SQL queries, such as:

* `CREATE_TABLE_AS_SELECT`
* `CREATE_VIEW`
* `MERGE`
* `JOIN`

{% hint style="info" %}
Not using Secoda to manage your data knowledge yet? Sign up for free [here](https://app.secoda.co) 👈
{% endhint %}
