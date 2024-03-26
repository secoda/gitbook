---
description: Common questions about the Secoda product
---

# FAQ

## Does Secoda read the data from my data source?

Some of Secoda's features do read the data from the source, however **these are all optional features that can be turned off**. If permissions are provided, the data from the datasource can be read in the following circumstances:

* When using the [**Preview tab**](features/data-previews.md) in Secoda. For tables, the Preview tab will show 50 rows of data (excluding columns that are tagged as PII). For dashboards, we show an iFrame directly from the data source. Preview can be disabled or configured in the integrations Permissions settings.
* When using [**Query**](features/queries/) blocks. If permissions are provided, Admins and Editors can write and execute queries directly on the source through Secoda. Queries can be disabled or configured in the integrations Permissions settings.
* When running [**Column Profiling**](features/column-profiling.md). In this instance, Secoda will analyze the Minimums, Maximums, Range, etc of the columns, which requires analysis of the data. For some data sources, this information is provided by the Information schema and querying the data itself is not necessary.&#x20;
* When setting up [**Monitors**](features/monitoring.md) on your resources. In this case, Secoda will query the data to detect and identify anomalies or issues.
* When using [**Metrics**](features/metrics.md). Once a metric is set up, it will run queries on the source at a specified cadence.&#x20;

The data is read and saved in short term storage to show historical trends, allow for CSV downloads, and limit the number of queries made on your source.&#x20;

If you prefer to not have your data read, many of our great features work by only accessing your metadata! **Secoda does not need to read any source data to be a great data management tool for your team.**&#x20;

## What can I do on the free tier?

Secoda recommends following the [Getting Started ](./)step-by-step guide. You can also play around with docs, questions, collections and dictionary terms to see if it meets your needs.

The first, crucial step is to get your data connected to Secoda. If you experience any difficulty connecting to your data source or don't see your source as an available integration, please contact us via Intercom, our Slack community, or send an email to support@secoda.co

After your data is connected to Secoda, you'll be able to add users, owners, descriptions, definitions, collections, tags etc. to your data.

## Can I see how people are using our data in my organization?

As an editor in Secoda, we provide you with an [analytics](features/analytics-dashboard.md) dashboard to see how people are using Secoda in your company. Beyond that, you can also look at queries, joins, lineage and popularity of datasets in Secoda.

You can also use our [API](secoda-api.md) to visualize any information from Secoda in a BI tool.

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

There's a good chance we're already working on it! In order to support as many popular tools as possible, we are working on it diligently. If you need something that we do not support yet, create a request at [https://feedback.secoda.co/](https://feedback.secoda.co/).&#x20;

## Can I give feedback about Secoda?

We'd love to hear from you. You can join our Slack community [**thedataleap.slack.com**](https://www.thedataleap.slack.com) and provide feedback in #secoda-feature-requests or #secoda-support. We always love building with our customers!

As an existing customer, you have access to our feedback tool [Canny](https://feedback.secoda.co/). About Canny:

* **Submit Feedback**: Share suggestions and report bugs effortlessly.
* **Track Requests**: Stay informed as we review, prioritize, and implement changes.
* **Engage with the Community**: Vote and comment on features that other customers have already requested.

We're looking at relevance to not just one workspace but to all of our customers, which is why the vote feature will be important for making decisions on what to prioritize.

Access our Canny instance at [**feedback.secoda.co**](http://feedback.secoda.co/)**.** Check out our [**Video tutorial**](https://www.loom.com/share/86eb9317d7924835957e13c716b99c48?sid=1bf38c4a-e15b-4b1f-ab5e-3016b3c544af).

**Troubleshooting Access if you get an error**

* Create a Canny account using the same email address that you use for Secoda, and create a password (even if you normally use SSO to log into Secoda)
* Log into Secoda in another tab, then try again

Note: we're still available on Slack for urgent requests, questions, and general chit chat!

## What are the IP addresses for Secoda?

* `3.122.13.89` in the EU/UK region (eu.secoda.co).
* `35.175.75.15` in North America (app.secoda.co).
* `13.251.200.242` in the Asia-Pacific region (apac.secoda.co).

Please ensure the relevant address is whitelisted in any tool you'd like to integrate with Secoda. **Note:** These are only for Cloud workspaces. If you are on a managed instance, you can find the IPs in Secoda on the integration setup page (show below).

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/bd79c274-9b2e-4429-be9e-ac30efdf69f0.gif" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Not using Secoda to manage your data knowledge yet? Sign up for free [here](https://app.secoda.co) 👈
{% endhint %}
