---
description: Access and manage your query history and creation queries in Secoda.
---

# Extracted Queries

Secoda seamlessly extracts queries directly from an integration, pulling both the Query History and the Creation Query for each resource.

## Query History

By clicking on the Queries tab from a resource in Secoda, you can access the resource's query history. Query history is extracted from the following integrations:

* [snowflake-integration](../../integrations/data-warehouses/snowflake-integration/ "mention")
* [redshift-integration](../../integrations/data-warehouses/redshift-integration/ "mention")
* [bigquery-integration](../../integrations/data-warehouses/bigquery-integration/ "mention")
* [databricks-integration](../../integrations/data-warehouses/databricks-integration/ "mention")

### How Secoda Extracts Queries

During the extraction process, Secoda retrieves the queries since the last integration sync run, or a maximum of 30 days, directly from the integration. Any new, previously unseen queries are added to the list of queries associated with that resource in Secoda. This comprehensive list can be found under the Queries tab on the resource page, as shown below.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/6ba6695e-8db9-46f6-94e4-8e6a3afc0f98.gif" alt=""><figcaption></figcaption></figure>

### How to Access Queries Run on a Resource

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

To view detailed information about queries run on a specific resource, follow these steps:

1. **Locate the Resource**:
   * Click into a resource from the Catalog, or find it using the Search function.
2. **Navigate to the Queries Tab**:
   * Once you are on the resource page, go to the "Queries" tab.
3. **Review Query Information**:
   * For each query run on the resource, you will see the following details:
     * **SQL Query**: The full query executed on the resource from the integration source.
     * **Average Runtime**: The average amount of time it takes to run the query.
     * **Total Runtime**: The total amount of run time in the past 24 hours.
     * **Total Runs**: The number of times the query has been run in the past 24 hours.
     * **Users**: The user(s) who have executed this query.
4. **Explore the Query Summary**:
   * Click on a query to access the Query Summary, where you can:
     * **Visual Analytics**: View visual analytics related to the specific query.
     * **Query History**: See the query history, including date, user, runtime, and cost details.
     * **Referenced Resources**: View the list of resources that the query references.
     * **Filter History**: Filter the history to see data from the last 30 days, 7 days, or 1 day.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/0f34d014-88bd-43a8-940e-64276a9bac79.gif" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Queries can easily be copied, and run directly in Secoda through the [Query editor within a document](running-queries-in-secoda/).
{% endhint %}

### How to Access All Queries within the last 30 days

To view a comprehensive list of all extracted queries within the last 30 days across all resources in Secoda, follow these steps:

1. **Open the Command Palette**:
   * Press `CMD + K` on your keyboard.
2. **Search for "Queries"**:
   * In the command palette, type "Queries" or scroll to select the "Queries" option.
3. **Utilize the Aggregate Queries Page**:
   * On the aggregate queries page, you can:
     * **Search**: Use the search bar to find specific queries.
     * **Analyze Runtime**: Look at the Average Runtime column to identify the slowest running queries. This can help you pinpoint areas for optimization.

## Creation queries

For resources created from a query (e.g., Views), the Creation Query can be found by clicking the `</>` icon in the top right-hand corner. This query can also be copied for easy reuse.

<figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/be747437-f61a-4942-afb1-d2043c6c5a36.gif" alt=""><figcaption></figcaption></figure>
