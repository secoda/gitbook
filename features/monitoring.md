---
description: Create data monitors for visibility into the health of your data stack
---

# Monitoring

## Introduction

Monitoring plays a crucial role in maintaining data quality by allowing you to configure alerts for changes in your data. Automatically schedule monitors and set thresholds to track run history and visualize monitor performance.

Admins and Editors can access existing Monitors from the Monitors page accessible via the side panel. Here, you can view all monitors and incidents across the platform and create new ones.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/337f012c-4ced-4657-a69b-819b044089a0.png" alt=""><figcaption></figcaption></figure>

To learn about how our current customers are using Monitors in Secoda to improve their data quality, check out this list of [monitoring-use-cases.md](monitoring/monitoring-use-cases.md "mention").

{% hint style="info" %}
**Note:** Read permissions for the source data (in addition to the metadata) are required for the monitoring feature.
{% endhint %}

## Types of Monitors

Select from a variety of Monitors to suit your needs:

* **Row Count** - The number of rows over time
* **Freshness** - The time elapsed since last update
* **Cardinality** - The number of distinct values of a given column
* **Maximum** - The highest value of a numeric column
* **Minimum** - The lowest value of a numeric column
* **Mean** - The arithmetic mean of a numeric column
* **Null Percentage** - The percentage of values in a column that are null
* **Unique Percentage** - The percentage of values in a column that are unique
* [**Custom SQL**](monitoring.md#custom-sql-monitors) - Define a monitor by writing your own SQL query

The monitor will alert if any of these values are higher or lower than expected.

## Creating Monitors

Monitors can be created via the **Monitors** section in the sidebar or through the **Monitors tab** on the resource page:

1.  Navigate to "**Monitors**" and click "**Add monitor."**&#x20;

    <figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/cedab835-f00f-4bef-b5c1-2aeb80fa032a.png" alt=""><figcaption><p>Add monitor option on the main monitors page</p></figcaption></figure>
2.  Choose the monitor type and select the integration.

    &#x20;(if adding a new Monitor from the resource itself, the integration will be pre-selected):

    <figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/d82f0b01-677b-419d-b7c8-123755b818ca.png" alt=""><figcaption></figcaption></figure>
3.  Select one or multiple resources that you'd like to add the monitor to.

    <figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/475c98f5-c217-477b-8c36-265884ea5fee.png" alt=""><figcaption><p>configuration window for monitors<br></p></figcaption></figure>
4. Adjust the **Threshold** and **Schedule** to your preferred configuration.
   * **Schedule Options:** Daily, Every 12, 6 or 3 hours, or Hourly
   * **Threshold:** Automatic or Manual
     * Note: For Automatic thresholds to be set, it can take 4 days for hourly, 6 days for multiple times a day, and 8-9 days for daily monitors.&#x20;
5. Once configured, click add monitor and it show now show up within the list of monitors. You can view and edit the configurations from the sidebar on the monitor page

<div align="center">

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/c6c8550e-a537-479d-814e-a158003a4e42.png" alt="" width="317"><figcaption><p>Configuration details</p></figcaption></figure>

</div>

{% hint style="info" %}
**Note:** You can only add a monitor type which each of the columns support.

For example, if you have 3 numeric columns selected, you can add a "MIN" or "MAX" monitor, but you cannot do it if even one string column is selected in the modal.
{% endhint %}

### Custom SQL Monitors

A user is be able to create a monitor that runs custom SQL to create an output. The only requirement is that the final output of the custom SQL must be a single value.

Follow the same steps as above, but choose "Custom SQL" as the Monitor type. After creating, click into it so that you can add your desired query in the right side panel.

<div align="center">

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/4721c037-cdf0-4071-99fa-2e1dbd07023c.png" alt=""><figcaption><p>Custom SQL monitor</p></figcaption></figure>

</div>

### WHERE clause

Standard monitors such as nullness, row count, etc can be modified with custom SQL that’s added as a WHERE clause within the standard SQL.

<div align="center">

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/0e0b3170-52c0-43f1-882b-b3747af5f804.png" alt="" width="277"><figcaption><p>Adding WHERE clause</p></figcaption></figure>

</div>

## Managing Monitors

View **Status**, **Last** and **Next Run** details, and a **Chart Visualization** of the monitor's historical performance.

<div align="left">

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/f470b8d4-08eb-47ce-b27d-24b1bb09a2d1.png" alt=""><figcaption></figcaption></figure>

</div>

### Thresholds and Incidents

{% hint style="info" %}
If you've chosen Automatic thresholds, it can take up to a week for Secoda to finish learning what the right thresholds should be for your monitors.
{% endhint %}

The lighter green surrounding the main line represent the **threshold** limits - once the threshold is passed, it'll show a red dot indicating an incident

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/88d0fea1-144d-4b61-94c0-903bc22d6275.gif" alt=""><figcaption></figcaption></figure>

At the bottom of the Monitor page, you will find a history of all measurements, including those that have triggered incidents. You can easily filter this list to view only incidents and specify a particular time period.

When an incident occurs, you have two primary options for handling it: you can either acknowledge the incident to recognize that it has occurred or resolve it once appropriate actions have been taken.

The incident page provides visibility into all resources impacted downstream of the affected table or column. Additionally, the activity log allows team members to comment on the incident, tag others, and add relevant context for resolution.

If you have an existing integration with Jira, you can create a ticket for the incident directly from the Secoda incident page, streamlining your workflow.

Incidents are automatically acknowledged if a comment is made or a Jira ticket is created. They are automatically resolved if the measurement returns to range after three consecutive monitoring runs.

This incident management system is designed to enhance team collaboration and streamline the resolution process.

### Annotations

The **Monitoring Annotations** feature provides a way to mark specific data points within monitoring incidents, giving teams a deeper context and helping refine automatic thresholds over time. This feature includes a **Normal** button, which allows users to indicate that a particular data point is not an anomaly, but rather expected behavior.

**Using Monitoring Annotations with the Normal Button**

1. Navigate to the Incident that you wish to annotate.
2. Select the **Normal** button for the data point that you want to classify as expected.
3. This action marks the data point as typical, contributing to the accuracy of Secoda's automatic thresholding over time.

By tagging data points through Monitoring Annotations, you help Secoda’s monitoring become more attuned to your data’s unique patterns, reducing false alerts and improving the identification of true anomalies.

<figure><img src="../.gitbook/assets/Kapture 2024-11-04 at 11.46.05.gif" alt=""><figcaption><p>Monitor Annotations</p></figcaption></figure>

### Errors

You may receive an error on your Monitors for various reasons. The Error will appear under Status. You are able to click into the error to see exactly what went wrong with the Monitor. In the example below, a Custom SQL monitor was chosen but a query was never provided, causing it to error out.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/268a5907-a2bc-4b80-9d2d-ff8edbbab26b.gif" alt=""><figcaption></figcaption></figure>

## Best Practices

To optimize the effectiveness of data monitoring and manage resource utilization, consider these best practices:

1. **Selective Monitoring:** Focus on the most critical data elements. Prioritize columns and tables that are essential for your business operations to avoid unnecessary strain on resources.
2. **Optimize Frequency:** Set monitoring frequencies that balance timeliness and resource consumption. For many applications, configuring monitors to run **daily** is sufficient to catch issues without incurring excessive costs.
3. **Regular Reviews:** Periodically review data quality monitoring configurations. This ensures that your monitoring strategies stay aligned with evolving business needs and data landscapes.
4. **Workflow Integration:** Embed monitoring alerts into your team’s daily workflows using tools like Slack or email (see [#monitoring-notifications](monitoring.md#monitoring-notifications "mention")). This ensures that the right personnel are promptly notified, enabling swift action.
5. **Documentation and Training:** Keep detailed documentation of your monitor setups and procedures. Train your team on the importance of monitoring and the actions required when specific alerts are triggered.
6. **Trend Analysis:** Leverage historical data from your monitoring activities to identify trends and patterns. This analysis can help refine your data management practices and predictive monitoring over time.

By following these guidelines, you can ensure your monitoring processes are both efficient and effective, providing critical insights while maintaining control over costs and resource use.

## Monitoring Permissions

Monitoring functionality is primarily intended for users with Edit or Admin roles, rather than end business users who typically have Viewer permissions.

1. **Creating:**
   * Any Admin or Editor can now create monitors, without requiring specific integration permissions.
2. **Editing and Owning:**
   * Initially, any Admin or Editor can edit monitors. However, once an owner is designated for a monitor, only the owner and Admins will have editing rights.
   * Owners and Admins will also have the ability to invite additional owners to the monitors.
3. **Deleting, Running, and Resolving:**
   * The permissions for deleting, running, and resolving monitors will mirror those for editing. This means that only the monitor's owner and Admins can perform these actions once an owner is assigned.
4. **Viewing:**
   * Viewing permissions remain unchanged, with any Admin or Editor able to view monitors. We are planning future updates that will allow more granular control over who can view monitor outputs, enhancing privacy and data security.

## Monitoring Notifications

Stay informed about the status of your monitors by adjusting your Notification settings. Specify your preferred channels for receiving alerts—whether through Slack DMs, email, or directly within the app.&#x20;

<div align="left">

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/4be1ef82-00c9-46ba-a9de-b6639784c8e7.png" alt=""><figcaption><p>Monitor notifications in Settings</p></figcaption></figure>

</div>

Notifications for monitor incidents are issued only after the **first occurrence** following a successful run. The same incident will not trigger new alerts unless the issue has been resolved and another incident occurs. This policy minimizes repetitive alerts and ensures that notifications remain meaningful and actionable.

#### **Configuring Slack Channel Notifications**

Admins can direct monitoring notifications to specific Slack channels, distinct from other notification settings. This ensures that the right team members are alerted promptly. For detailed steps on setting this up, visit [here](../integrations/productivity-tools/slack-connection/#steps-for-setting-up-slack).

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/138d2dd7-a4f6-4adf-a404-ff041566eabe.png" alt=""><figcaption><p>Example Slack notification</p></figcaption></figure>

#### Email Monitoring Notifications

Email notifications provide direct links to the relevant sections in Secoda. As shown in the image below, clicking the "Open Secoda" link takes you to the Inbox notification, while other links direct you to specific incidents or tables.

<figure><img src="../.gitbook/assets/image (38).png" alt=""><figcaption><p>Image explaining the links in email notifications</p></figcaption></figure>

## Video resource

{% embed url="https://www.loom.com/share/03c92029f9cd4de4ae11653a2cea6c0c?sid=202df101-4494-44f7-8594-b0606f3cf5d9" %}
