---
description: >-
  Learn more about how to identify your most popular sources and how Secoda
  measures this metric
---

# Popularity

## What does Popularity measure?

The popularity of a data resource in Secoda is calculated based on the number of times it has been queried or viewed in the last 24 hours, pulled directly from the Source.&#x20;

We are currently pulling this data from the following BI tools and data warehouses:

* [Tableau](../integrations/data-visualization-tools/tableau-integration/)
* [Mode](../integrations/data-visualization-tools/mode/)
* [Looker](../integrations/data-visualization-tools/looker-integration/)
* [Snowflake](../integrations/data-warehouses/snowflake-integration/)
* [Redshift](../integrations/data-warehouses/redshift-integration/)
* [BigQuery](../integrations/data-warehouses/bigquery-integration/)
* [Glue](../integrations/data-pipeline-tools/aws-glue-integration/)

By default, all columns in a table, all tables in a database, all dashboards in a BI tool will be ordered by the popularity in Secoda so you can always see what's being used most frequently.&#x20;

The popularity, and thus the order of the resources, might change after each Metadata extraction (which is dependent on your set schedule for the integration), as the extraction will bring in the latest information of usage (views, queries, users) of the resource from the Source.

The popularity of a resource is further enhanced by the number of times it has been used, documented, or viewed in Secoda over the last 180 days. To learn more about usage within Secoda, scroll down to the [**Popularity based on Views in Secoda**](popularity.md#popularity-based-on-views-in-secoda) section below.

## Searching for popular resources in Secoda

There are a few ways to identify the most popular resources in your workspace. Secoda calculates popularity through usage pulled from the Source, as well as usage directly in Secoda.&#x20;

### Popularity based on queries and views outside of Secoda

As a viewer**,** you can sort by popularity directly within Search. The resources that are most often used and queried from the source will appear at the top.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/0fb3b56b-8f73-41e3-8acb-60ee2fd6f0f1.gif" alt=""><figcaption><p>Sorting in Search</p></figcaption></figure>

Once you're clicked into a catalog resource, you can see the number of queries run on that data, as well as it's frequent users.&#x20;

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/f96f8a71-af5a-4dd4-9fd3-c0748a52e2ef.png" alt=""><figcaption><p>Popularity metadata</p></figcaption></figure>

### Popularity based on views in Secoda

As an editor or admin in Secoda, you can see what's popular across your workspace users _within_ Secoda by filtering in the [**Analytics**](analytics-dashboard.md) dashboard. In the example below, I've filtered the resource type to dashboard to show which dashboards are being looked at the most directly within Secoda.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/ebaaaa0d-0fbe-488b-b13c-a670da616f44.gif" alt=""><figcaption><p>Analytics Dashboard</p></figcaption></figure>

## Improving accuracy of the popularity metric

If the users are not members of the Secoda workspace, they will be considered Service Accounts. Service Accounts can be opted in or out of Popularity calculations.&#x20;

Make your popularity metric more accurate by marking certain emails as service accounts, by following these steps [define-service-accounts.md](../getting-started/secoda-as-an-admin/connect-your-data/define-service-accounts.md "mention").
