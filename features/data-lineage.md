---
description: >-
  After connecting your data to Secoda, you'll be able to get a high level view
  of your lineage both at the table and column level.
---

# Lineage

## What is Lineage?

In the context of Secoda, lineage refers to the process of tracking and documenting the relationships between different data assets within an organization. This can include information about where data comes from, how it has been transformed or modified over time, and how it is being used. Secoda automatically extracts queries to generate lineage. This helps data teams identify the downstream and upstream dependencies of a table easily.&#x20;

Lineage is an important part of data governance and can help organizations understand the origin and history of their data, identify potential sources of errors or inconsistencies, and ensure that data is being used appropriately.

Overall, lineage is an important aspect of data management and can help organizations improve transparency, trustworthiness, and understanding of their data.

## **How to see Lineage in Secoda** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

1. Choose which resource you'd like to view the lineage for. Find it either from the Catalog in the navigation bar, or through Search.&#x20;
2. Once on the resource page, click on the **Lineage** tab.&#x20;
3. From here, you can see lineage visualized in a graph view. Click through the arrows on each node to see how the relationships are connected.
4.  From any node, click the three dots and **Analyze Impact** to see a list-view of all upstream and downstream dependencies of that resource. This view makes impact analysis quick and easy with just one click.&#x20;

    <figure><img src="../.gitbook/assets/Screenshot 2023-11-30 at 12.06.01 PM.png" alt=""><figcaption></figcaption></figure>
5.  There is also a Search bar within Lineage that allows you to find and zoom in on a specific node, including columns. This can be helpful for larger, more complex lineage graphs.&#x20;

    <figure><img src="../.gitbook/assets/Screenshot 2023-11-30 at 12.06.54 PM.png" alt=""><figcaption></figcaption></figure>
6.  On certain resources, you can expand to see the Column Level lineage. You can search within the Columns view to drill down to find the relevant columns.

    1. If you click into any of the columns, it opens up it's own Impact Analysis showing what is upstream and downstream of that column.

    <figure><img src="../.gitbook/assets/Screenshot 2023-11-30 at 12.13.08 PM.png" alt=""><figcaption></figcaption></figure>

## How is Lineage Created?

When you connect a data source to Secoda, Lineage is automatically generated from SQL queries, such as:

* `CREATE_TABLE_AS_SELECT`
* `CREATE_VIEW`
* `MERGE`
* `JOIN`

{% hint style="info" %}
Not using Secoda to manage your data knowledge yet? Sign up for free [here](https://app.secoda.co) 👈
{% endhint %}
