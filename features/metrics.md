---
description: Define and visualize your organization's Metrics
---

# Metrics

## What are Metrics in Secoda?

Metrics in Secoda are a way to centralize, visualize and define your organization's metrics. Metrics allow you to plug in a query and generate a graph visualization of that query.

Metrics are different than Dictionary terms in a way that they are a calculation, whereas terms are static. For example, a term could be "customer" and a metric could be "weekly average customers".

{% hint style="info" %}
Viewers in the workspace are only able to see the chart visualization, not the actual query that creates it. Admins and Editors, however, can see and edit both.
{% endhint %}

## Benefits of Metrics

* Enable consistent metric definitions across the organization.
* Reduce redundancy and errors in metric reporting.
* Improve decision-making by providing current and accurate data.
* Empower data producers to define and share metrics easily.
* Provide a seamless experience in visualizing query-based metrics.

## Creating metrics

You can find the Metrics in the side navigation bar beneath Collections, if it is enabled for the Team you are working in. Reach out to a workspace Admin if you are unable to see this.

Once in the Metrics, you'll be able to see all of the current metrics your team has created, sorted by last added.

1. **Name Metric**: To create a new metric, simply click "New Metric" in the top left.
2. **Enrich / Add metadata to the Metric**: You'll have the option to name the metric, add a definition, select the Team(s) and Collections you'd like it to appear in, assign ownership, and add applicable tags.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/94e4792e-0bcb-47da-b0dd-fe12b273a2d4.gif" alt=""><figcaption></figcaption></figure>

3.  **Define the Metric with a Query:** After creating a metric, you'll see the "New query" option. Just choose which integration you'd like to query (it can be _any_ [Database](../integrations/databases/) or [Data Warehouse](../integrations/data-warehouses/) integration that we support), type your SQL, and click the Run button.

    <figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/c4aea352-9607-428b-894f-b5f66c54f431.png" alt=""><figcaption></figcaption></figure>
4. **Visualize the Metric**: After running the query, Secoda will visualize the metric for you. Currently time-series based line graphs are supported.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/106ef08b-c953-42d1-b206-bfe378b99eed.gif" alt=""><figcaption></figcaption></figure>

## Setting refresh schedules

After defining a metric, the user can set a schedule on how often they'd like the query to be run. Simply click into the Metric, and see the **Configuration** settings on the right hand side. Next to Refresh, you have the option to set the frequency of updates to be hourly, daily, weekly, monthly, or none.

![](https://secoda-public-media-assets.s3.amazonaws.com/7880707d-d229-40b7-ab88-33f47585ea58.png)

In the Metrics overview page, you'll also see two columns for **Run status** and **Last run**. Run status tells us whether or not the query was successfully run, and will appear as "Normal" or "Abnormal". Last run tells us when the query was last run.

## Embed Metrics in Documents

Some users might want to reference a Metric in a Document. You can embed a Metric chart directly into a Document by typing /metric and searching for the metric.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/6b006aef-9970-4424-8061-c9fa45459774.gif" alt=""><figcaption></figcaption></figure>

## Nesting Metrics

Similar to how you can [nest Dictionary terms](broken-reference/), you can also nest Metrics under each other to create a folder structure.

To do so, create the Metrics including the parent Metrics, check off the box of the Metrics you'd like to be nested, and click "Set parent".

## Use Cases for Metrics

Here are some examples of Metrics that your Team might consider setting up in Secoda.

1. **Monthly Recurring Revenue (MRR):**
   * **Description:** Measures the total predictable revenue that a company expects to receive every month from all active subscriptions.
   * **Importance:** MRR is crucial for understanding the steady income stream and predicting long-term financial performance in the subscription-based business model of SaaS.
2. **Customer Acquisition Cost (CAC):**
   * **Description:** Calculates the total cost of acquiring a new customer, including all marketing and sales expenses.
   * **Importance:** CAC is vital for evaluating the effectiveness of marketing strategies and understanding the investment needed to attract new users.
3. **Customer Lifetime Value (CLTV):**
   * **Description:** Estimates the total revenue a business can reasonably expect from a single customer account throughout the business relationship.
   * **Importance:** CLTV helps companies understand how valuable customers are over their lifecycle and is often used in conjunction with CAC to assess return on investment.
4. **Churn Rate:**
   * **Description:** The percentage of customers who cancel or do not renew their subscriptions during a given time period.
   * **Importance:** Monitoring churn rate is essential for assessing customer retention strategies and product satisfaction.
5. **Lead-to-Customer Conversion Rate:**
   * **Description:** The percentage of leads that become paying customers.
   * **Importance:** This metric helps measure the effectiveness of the sales funnel and the efficiency of the sales and marketing teams.
6. **Average Revenue Per User (ARPU):**
   * **Description:** The average revenue received from each user or account typically calculated on a monthly or annual basis.
   * **Importance:** ARPU provides insights into revenue generation efficiency and how much each user contributes to the bottom line.
7. **Net Promoter Score (NPS):**
   * **Description:** A measure of customer satisfaction and loyalty based on the likelihood of customers to recommend a company's product or service to others.
   * **Importance:** NPS is a strong indicator of customer loyalty and can predict business growth and customer retention.

## Video resource

{% embed url="https://www.loom.com/share/7ebbf4c731c7440d9eb138deaaca8f1b?sid=6a1e8e4e-f532-4ab0-b88c-ebc4136a9b09" %}
