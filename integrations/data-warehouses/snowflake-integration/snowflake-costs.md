---
description: Learn about and set monitors on your Snowflake costs in Secoda
---

# Snowflake costs

Everyone is thinking about cost containment these days, and so are we! You can track your Snowflake costs, using our Snowflake Cost widget as part of the [Analytics Dashboard](../../../features/analytics-dashboard.md).

<figure><img src="../../../.gitbook/assets/Kapture 2024-01-17 at 10.57.36 (1).gif" alt=""><figcaption></figcaption></figure>

## How does the Widget work?

We provide cost analysis for _everything_ in your Snowflake warehouse. This information is provided through the information schemas of each table, for the entire warehouse.&#x20;

Visualizing your cost trends using the Widget **will not** impact your overall costs, as Secoda is already querying the information schemas to extract the metadata for your workspace. To learn more about what queries Secoda makes to your Snowflake instance, navigate to the [Secoda impact on Snowflake Costs](snowflake-costs.md#secodas-impact-on-snowflake-costs) section below.&#x20;

## Add Monitors on Snowflake costs

You can even use our monitoring features on a Snowflake cost widget to be alerted about changes to daily costs. Simply create the widget, then use the three dot menu to create a monitor.

<figure><img src="../../../.gitbook/assets/Screenshot 2023-12-28 at 4.21.09 PM.png" alt=""><figcaption></figcaption></figure>

Add filters on usage type and balance source, and voila! You can catch changes before they become larger issues.

<div align="left">

<figure><img src="../../../.gitbook/assets/Screenshot 2023-12-27 at 2.17.19 PM.png" alt="" width="375"><figcaption></figcaption></figure>

</div>

## Secoda's Impact on Snowflake Costs

At every sync, Secoda runs queries on your Snowflake instance. Generally, these queries costs anywhere between 0.1 to 1 credit in total.

Secoda queries Snowflake in two ways during each sync. The first, is querying the information schema of each database in Snowflake. The second, is querying the `snowflake.account_usage.query_history` table. From these two queries, Secoda is able to extract and calculate [Metadata](snowflake-metadata/), [Cost](../../../features/analytics-dashboard.md), [Lineage](../../../features/data-lineage.md), [Query History](../../../features/queries/), [Popularity](../../../features/popularity.md) and [profile](../../../features/column-profiling.md) the Snowflake Columns.&#x20;

Note, queries outside of a sync, such as those from [Monitors](../../../features/monitoring.md), are not included in the cost above, and can vary depending on how the feature is implemented in your workspace.&#x20;
