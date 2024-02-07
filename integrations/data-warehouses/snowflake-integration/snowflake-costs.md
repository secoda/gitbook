---
description: Learn about and set monitors on your Snowflake costs in Secoda
---

# Snowflake costs

You're able to see how your Snowflake costs have changed over time with the Pipeline health widgets built from the [analytics-dashboard.md](../../../features/analytics-dashboard.md "mention").

<figure><img src="../../../.gitbook/assets/Kapture 2024-01-17 at 10.57.36 (1).gif" alt=""><figcaption></figcaption></figure>

## How it works

We provide cost analysis for _everything_ in your Snowflake platform because we are querying the SNOWFLAKE.INFORMATION\_SCHEMA. This schema spans all resources in Snowflake, not just the ones you bring into Secoda.

Cost monitoring does _not_ add more costs to Snowflake since we are only querying the INFORMATION\_SCHEMA in Snowflake.

## Add Monitors on Snowflake costs

You can even use our monitoring features on a Snowflake cost widget to be alerted about changes to daily costs. Simply create the widget, then use the three dot menu to create a monitor.

<figure><img src="../../../.gitbook/assets/Screenshot 2023-12-28 at 4.21.09 PM.png" alt=""><figcaption></figcaption></figure>

Add filters on usage type and balance source, and voila! You can catch changes before they become larger issues.

<div align="left">

<figure><img src="../../../.gitbook/assets/Screenshot 2023-12-27 at 2.17.19 PM.png" alt="" width="375"><figcaption></figcaption></figure>

</div>
