---
description: >-
  Learn more about how to identify your most popular sources and how Secoda
  measures this metric
---

# Popularity

Popularity metrics can be found a few places throughout the product. Check which tools and data warehouses we are currently pull this metadata from: [integrations](../integrations/ "mention").

## What does Popularity measure?

The popularity of a data resource in Secoda is calculated based on the number of times it has been queried or viewed in the last 24 hours, pulled directly from the Source.

By default in Secoda, all columns in a table, tables in a database, dashboards etc. will be ordered by popularity so you can always see what's being used most frequently.

The popularity, and thus the order of the resources, might change after each Metadata extraction (which is dependent on your set schedule for the integration), as the extraction will bring in the latest information of usage (views, queries, users) of the resource from the Source.

To learn more about popularity and usage within the Secoda app, scroll down to the [**Popularity based on Views in Secoda**](popularity.md#popularity-based-on-views-in-secoda) section below.

## Searching for popular resources in Secoda

### Popularity based on queries and views outside of Secoda

Anyone is Secoda can sort by popularity directly within Search. The resources that are most often used and queried from the source will appear at the top.

<figure><img src="../.gitbook/assets/Kapture 2024-11-20 at 22.37.11.gif" alt=""><figcaption></figcaption></figure>

Once you're clicked into a catalog resource, you can see the number of queries run on that data, as well as it's frequent users.

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

### Views in Secoda

As an editor or admin in Secoda, you can see what's popular across your workspace users _within_ Secoda by filtering in the [**Analytics**](analytics-dashboard.md) dashboard or on the Search page. In the example below, the resource type filter is used to show which dashboards are being looked at the most directly within Secoda.

<figure><img src="../.gitbook/assets/Kapture 2024-11-20 at 22.45.24.gif" alt=""><figcaption></figcaption></figure>



## Improving accuracy of the popularity metric

If the users are not members of the Secoda workspace, they will be considered Service Accounts. Service Accounts can be opted in or out of Popularity calculations.

Make your popularity metric more accurate by marking certain emails as service accounts, by following these steps [define-service-accounts.md](../getting-started/secoda-as-an-admin/connect-your-data/define-service-accounts.md "mention").
