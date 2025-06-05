---
description: Key questions about the Secoda product
---

# FAQ

## Does Secoda read the data from my data source?

Some of Secoda's features do read the data from the source, however **these are all optional features that can be turned off**. If permissions are provided, the data from the datasource can be read in the following circumstances:

* When using the [**Preview tab**](features/data-previews.md) in Secoda. Preview can be disabled or configured in the integrations Permissions settings.
  * For tables, the Preview tab will show 50 rows of data (excluding columns that are tagged as PII). This data is not stored, as it is queried and displayed in real time.&#x20;
  * For dashboards, we show an iFrame directly from the data source.&#x20;
* When using [**Query**](features/queries/) blocks. If permissions are provided, Admins and Editors can write and execute queries directly on the source through Secoda. Queries can be disabled or configured in the integrations Permissions settings. Query results are stored to make it easier to access and download without re-running the query.&#x20;
* When running [**Column Profiling**](features/column-profiling.md). In this instance, Secoda will analyze the Minimums, Maximums, Range, etc of the columns, which requires analysis of the data. For some data sources, this information is provided by the Information schema and querying the data itself is not necessary. Column profile results are stored.
* When setting up [**Monitors**](features/monitoring.md) on your resources. Secoda will execute queries on the source to detect and identify any anomalies or issues. The results from each query are stored.
* When using [**Metrics**](features/metrics.md). Once a metric is set up, it will automatically run queries on the data source according to the set schedule. The result of these queries are stored.

If you prefer to not have your data read, many of our great features work by only accessing your metadata! **Secoda does not need to read any source data to be a great data management tool for your team.**&#x20;

## What can I do on the free tier?

Secoda recommends following the [Getting Started ](./)step-by-step guide. You can also play around with docs, questions, collections and dictionary terms to see if it meets your needs.

The first, crucial step is to get your data connected to Secoda. If you experience any difficulty connecting to your data source or don't see your source as an available integration, please contact us via Intercom, our Slack community, or send an email to support@secoda.co

After your data is connected to Secoda, you'll be able to add users, owners, descriptions, definitions, collections, tags etc. to your data.

## Can I see how people are using our data in my organization?

As an editor in Secoda, we provide you with an [analytics](features/analytics-dashboard.md) dashboard to see how people are using Secoda in your company. Beyond that, you can also look at queries, joins, lineage and popularity of datasets in Secoda.

You can also use our [API](broken-reference) to visualize any information from Secoda in a BI tool.

## How is the popularity calculated?

In Secoda, the [**Popularity**](features/popularity.md) of a resource is a piece of metadata pulled directly from the source. It can be seen in the catalog or resource page. It is defined as the number of queries (for a database/data warehouse) or the number of views (for a data visualization tool) over the previous 24 hours from the last sync with that source.

In contrast, **Popular Resources** in the workspace are determined by calculating the number of views of the resource in Secoda over the last 180 days. It can be seen in the Analytics, or in the Search.

When ranking search results by Popularity, Secoda uses a combination of external and internal metrics.

## How is search ordered in Secoda?

Search results are based on a number of factors. The primary factor is the matching of text in the resource title or description to what has been inputted into the search bar.

Popularity of the resource (from external and internal metrics) are also used to order the search results.

The search order can be fine tuned by adding filters to your search. Read more here [#how-search-works](features/search.md#how-search-works "mention").

## How often does Secoda sync with my integration?

You can choose when to run an extraction for each [integrations](integrations/). Schedules for syncs can be set to run on a daily, weekly, or monthly basis. One off manual syncs are available as well, and can only be run by Admins.

## Can I edit in Secoda?

Editing certain resources in Secoda is only possible if you're an Editor or Admin. Depending on your role, you may not be able to make changes to documentation in Secoda.

You should contact the admin(s) within your organization to ask for more permissions.

To learn more about user roles in Secoda, check out our[ **User Management** ](user-management/)section.

## What happens if someone edits the description in Secoda?

For many integrations, Secoda will extract the description from the source on the first sync. If that description is re-written in Secoda, Secoda will remain the source of truth. This means that subsequent syncs with the source will **not** override the description in Secoda.

If you'd like to override the description in Secoda in the following syncs, you can set the preferences for the integration in the Integration settings.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/84990c85-e78e-44ee-a67c-ed5cfe8415f8.png" alt=""><figcaption></figcaption></figure>

## What is Secoda's back up policy?

Secoda backs up all metadata every 5 minutes. This data is retained for 24 months unless you explicitly ask for your data to be deleted.

## When will you support \_\_\_\_ integration?

There's a good chance we're already working on it! In order to support as many popular tools as possible, we are working on it diligently. If you need something that we do not support yet, create a request by reaching out to us over support@secoda.co.&#x20;

## Can I give feedback about Secoda?

We'd love to hear from you. You can email support@secoda.co with any feedback that you have.

## What are the IP addresses for Secoda?

* `3.122.13.89` in the EU/UK region (eu.secoda.co).
* `35.175.75.15` in North America (app.secoda.co).
* `13.251.200.242` in the Asia-Pacific region (apac.secoda.co).

Please ensure the relevant address is whitelisted in any tool you'd like to integrate with Secoda. **Note:** These are only for Cloud workspaces. If you are on a managed instance, you can find the IPs in Secoda on the integration setup page (show below).

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/bd79c274-9b2e-4429-be9e-ac30efdf69f0.gif" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Not using Secoda to manage your data knowledge yet? Sign up for free [here](https://app.secoda.co) 👈
{% endhint %}
