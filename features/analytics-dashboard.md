---
description: Take a look into the usage of your workspace
---

# Analytics

Admins and Editors have access to the Analytics dashboard which showcases how their Secoda workspace is being used. They also receive a weekly email that highlights the metrics in this analytics dashboard.

Some metrics that are tracked include:

* Monthly, Weekly and Daily active users
* Popular resources and searches
* Top editors and viewers
* Integration-specific: [Snowflake costs](../integrations/data-warehouses/snowflake-integration/snowflake-costs.md), dbt tests, dbt runs

This feature is located above Settings in the left side panel.

## Reports

Create Reports to organize your Analytics widgets into separate themes. For example, you can have one Report that shows stats on your users, another on documentation, and another on Snowflake costs.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/897aaaf0-057b-472d-b73f-ba6545aa3129.png" alt=""><figcaption></figcaption></figure>

## Filtering

You are able to filter on the widgets in the dashboard. In the gif below, you can see how to filter on "Popular resources" to show the most popular _charts_ for example!

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/24b65dee-8b43-448c-89c7-a3b9602651ef.gif" alt=""><figcaption><p>Popular charts</p></figcaption></figure>

## Identifying undocumented resources

Another important metric you can filter for here is **undocumented popular resources**. This would be an important metric to know about so that you can make sure to build out the documentation since your users are often visiting these resources.

{% embed url="https://www.loom.com/share/96a0cdf5b99c4f0dba83f43c1dceb19d?sid=067c899c-c2fd-40ab-b0d8-35afbf1e36e6" %}

### Widgets

#### Automations

* **Automation Run Count**: Line chart for the number of automation runs over time
* **Automation Resources Updated**: Line chart for number of resources updated by automations over time

#### Monitors

* **Monitor**: Real-time monitoring dashboard showing current status and alerts
* **Monitor Count**: Line chart for the number of monitors in the workspace over time
* **Incident Count**: Line chart for the number of incidents detected over time

#### Secoda AI

* **AI Chat History**: Table for AI interactions and conversations in the workspace
* **AI Chat Count**: Line chart for the n of AI chat conversations over time

#### Users

* **Daily Active Users**: Line chart for the unique daily users
* **Weekly Active Users**: Line chart for the unique weekly users
* **Monthly Active Users**: Line chart for the unique monthly users
* **Users with Most Views**: Table showing users ranked by content view count
* **Users with Most Edits**: Table displaying users ranked by edit frequency
* **Users with Most Resources**: Table showing users who own the most resources
* **Users with Least Edits**: Table identifying users with minimal editing activity
* **Users with Most Searches**: Table ranking users by search activity

#### Teams

* **Teams with Most Edits**: Table showing team-level editing activity
* **Teams with Most Views**: Table displaying team-level viewing patterns

#### Searches

* **Popular Searches**: Table showing most frequently used search terms
* **Number of Searches**: Line chart for number of searches over time

#### Questions

* **Questions Asked**: Line chart for the number of questions asked over time
* **Question Answer Time**: Line chart for the average response time for questions

#### Resources

* **Popular Resources**: Table for the most queried resources
* **Total Resources**: Line chart for the total number of resources
* **Resource Views**: Line chart for the number of resource views
* **Documented Resources Percentage**: Line chart for the percentage of documented resources

#### Tests

* **dbt Test Results**: Various charts showing test execution results and statistics including pass percentage, number of failures, and model coverage.

#### Costs

* **Snowflake Analytics**: Multiple widgets tracking costs, credits, query volume, and usage metrics.

Each widget can be customized with:

* Different time ranges (weekly, monthly, all-time)
* Various visualization types (line charts, bar charts, tables)
* Size adjustments (small, medium, large, full)
* Custom filters based on the metric type

