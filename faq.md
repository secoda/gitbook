---
description: Key questions about the Secoda product
---

# FAQ

## What can I do on the free tier?

Secoda recommends following the Getting Started step-by-step guide. You can also play around with docs, questions, collections and dictionary terms to see if it meets your needs.

The first, crucial step is to get your data connected to Secoda. If you experience any difficulty connecting to your data source or don't see your source as an available integration, please contact us via Intercom, our Slack community, or send an email to support@secoda.co

After your data is connected to Secoda, you'll be able to add users, owners, descriptions, definitions, collections, tags etc. to your data.&#x20;

## Can I see how people are using our data in my organization?

As an editor in Secoda, we provide you with an analytics dashboard to see how people are using Secoda in your company. Beyond that, you can also look at queries, joins, lineage and popularity of datasets in Secoda.&#x20;

You can also use our API to visualize any information from Secoda in a BI tool.

## How is the popularity calculated?

The popularity of a piece of data depends on the number of times it has been queried, the number of users over the last 180 days. The popularity of a resource is further enhanced by the number of times it has been used, documented, or viewed on Secoda. Dashboards take into account the number of views, frequency of queries and when a resource was accessed.

## How is search ordered in Secoda?

Search results are based on a number of factors.&#x20;

This is the most important factor that determines search results: matching the text of the resource (in the column, the table, or the dashboard) with the text entered into the search.

## Does Secoda read the data from my data source?

Nope! We're only looking at the metadata. The way we do this is by querying the information schema on a table. This provides us with metadata such as the names of columns, tables, schemas, etc.

If permissions are provided, the data from the datasource can be read in the following circumstances:

* When the Preview tab in Secoda is used. Preview is an optional feature that can be disabled for the workspace. For tables, the Preview tab will show 50 rows of data (excluding columns that are tagged as PII). For dashboards, we show an iFrame directly from the data source.&#x20;
* When using [Query](features/queries/) blocks. If permissions are provided, Admins and Editors can write and execute queries directly on the source through Secoda.
* When [Column Profiling](features/column-profiling.md). In this instance, Secoda will analyze the Minimums, Maximums, Range, etc of the columns, which requires analysis of the data.&#x20;
* When [Monitoring](features/monitoring.md) is set up. In this case, Secoda will query the data to detect and identify anomalies or issues.&#x20;

Even if the data is read, it is never saved or logged by Secoda.

## How often does Secoda update?

You can choose when to run an extraction for each integrations. Admins can run manual syncs as well and can set the schedule on a daily, weekly or monthly basis.&#x20;

## Can I edit in Secoda?

Editing certain resources in Secoda is only possible if you're an Editor or Admin. Depending on your role, you may not be able to make changes to documentation in Secoda.&#x20;

You should contact the admin(s) within your organization to ask for more permissions.

To learn more about user roles in Secoda, check out our[ **User Management** ](user-management/)section.&#x20;

## What happens if someone edits the documentation in Secoda?

Documentation from your tools automatically syncs with Secoda. We will stop writing documentation back to our tool once all changes have been made to documentation inside Secoda. So that your documentation has a consistent "source of truth", we do this.

Secoda documentation can be returned programmatically through our API to your tool.

Our support team can disable the editing of descriptions for specific data sources inside Secoda if you need to.

## What is Secoda's back up policy?

Secoda backs up all metadata every 5 minutes. This data is retained for 24 months unless you explicitly ask for your data to be deleted.

## When will you support \_\_\_\_ integration?

There's a good chance we're already working on it! In order to support as many popular tools as possible, we are working on it diligently. If you need something that we do not support yet, let us know on Slack or in Intercom.

## Can I give feedback about Secoda?

We'd love to hear from you. You can join our Slack community [**thedataleap.slack.com**](https://www.thedataleap.slack.com) and provide feedback in #secoda-feature-requests. We always love building with our customers!

As an existing customer, you have access to our feedback tool Canny. About Canny:

* **Submit Feedback**: Share suggestions and report bugs effortlessly.
* **Track Requests**: Stay informed as we review, prioritize, and implement changes.
* **Engage with the Community**: Vote and comment on features that other customers have already requested.

We're looking at relevance to not just one workspace but to all of our customers, which is why the vote feature will be important for making decisions on what to prioritize.&#x20;

Access our Canny instance at [**feedback.secoda.co**](http://feedback.secoda.co/)**.** Check out our [**Video tutorial**](https://www.loom.com/share/86eb9317d7924835957e13c716b99c48?sid=1bf38c4a-e15b-4b1f-ab5e-3016b3c544af).

**Troubleshooting Access if you get an error**

* Create a Canny account using the same email address that you use for Secoda, and create a password (even if you normally use SSO to log into Secoda)
* Log into Secoda in another tab, then try again

Note: we're still available on Slack for urgent requests, questions, and general chit chat!

{% hint style="info" %}
Not using Secoda to manage your data knowledge yet? Sign up for free [here](https://app.secoda.co) 👈
{% endhint %}
