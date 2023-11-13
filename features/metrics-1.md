---
description: Define and visualize your organization's Metrics
---

# Metrics

## What are Metrics in Secoda?

Metrics in Secoda are a way to centralize, visualize and define your organization's metrics. Metrics allow you to plug in a query and generate a graph visualization of that query.

Metrics are different than Dictionary terms in a way that they are a calculation, whereas terms are static. For example, a term could be "customer" and a metric could be "weekly average customers".

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
2. **Enrich/ Add metadata to the Metric**: You'll have the option to name the metric, add a definition, select the Team(s) and Collections you'd like it to appear in, assign ownership, and add applicable tags.

<figure><img src="../.gitbook/assets/Kapture 2023-11-07 at 17.04.16.gif" alt=""><figcaption></figcaption></figure>

3.  **Define the Metric with a Query:** After creating a metric, you'll see the "New query" option. Just choose which integration you'd like to query, type your SQL, and click the Run button.&#x20;

    <figure><img src="../.gitbook/assets/Screenshot 2023-11-13 at 4.29.18 PM.png" alt=""><figcaption></figcaption></figure>
4. **Visualize the Metric**: After running the query, Secoda will visualize the metric for you. You'll have the option to customize the graph based on the data type, for example line, bar, or pie charts.

## Setting refresh schedules

After defining a metric, the user can set a schedule on how often they'd like the query to be run. Simply click into the Metric, and see the **Configuration** settings on the right hand side. Next to Refresh, you have the option to set the frequency of updates to be hourly, daily, weekly, monthly, or none.

![](<../.gitbook/assets/Screenshot 2023-11-13 at 4.21.44 PM.png>)

In the Metrics overview page, you'll also see two columns for **Run status** and **Last run**. Run status tells us whether or not the query was successfully run, and will appear as "Normal" or "Abnormal". Last run tells us when the query was last run.

## Nesting Metrics

Similar to how you can [nest Dictionary terms](metrics/#nesting-terms), you can also nest Metrics under each other to create a folder structure.

To do so, create the Metrics including the parent Metrics, check off the box of the Metrics you'd like to be nested, and click "Set parent".
