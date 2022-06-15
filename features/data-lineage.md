---
description: >-
  After connecting your data to Secoda, you'll be able to get a high level view
  of your data lineage both at the table and column level.
---

# Data Lineage in Secoda

## **Everything about Secoda Lineage** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

Secoda automatically extracts queries to generate data lineage. This can help data teams identify the downstream and upstream dependencies of a table easily.&#x20;

On each dependency, you will be able to see how many levels away a particular table is.&#x20;

1. Select the data asset that you'd like to view the lineage of from the Data button in the navigation bar, or, search for it using the search bar.&#x20;
2. After selecting the asset you'd like to view, click on the **Lineage** tab. You'll find a visual demonstration of your data lineage here, and can zoom in, out, and select what lineage detail you'd like to view on the right side.&#x20;

![](<../.gitbook/assets/ezgif.com-gif-maker (2) (1).gif>)

To view the dependencies of a table, click **Downstream** on the top tabs.&#x20;

You'll be able to sort the dependencies of that table by source, name, resource type, and schema by typing the name of what you'd like to sort by. You can navigate through the lineage using either the graph or the downstream / upstream tabs. The list view may be easier to use when navigating large graphs which show lots of connected data.

![](<../.gitbook/assets/Screen Shot 2022-04-08 at 7.17.17 AM.png>)

Secoda also captures column lineage to show dependencies across your columns. To flip to the column lineage, just click on the "lineage detail" on the right hand side.

![](<../.gitbook/assets/ezgif.com-gif-maker (1).gif>)

## How is Lineage Created?

When you connect a data source to Secoda, Lineage is automatically generated from SQL queries, such as:

* `CREATE_TABLE_AS_SELECT`
* `CREATE_VIEW`
* `MERGE`
* `JOIN`

To make it even easier to navigate lineage for tables or dashboards with many fields, you can search within a table or dashboard.

First click the item you want to search so the magnifying glass icon appears, then type your search to narrow the results.

{% hint style="info" %}
Not using Secoda to manage your data knowledge yet? Sign up for free [here](https://app.secoda.co) 👈
{% endhint %}
