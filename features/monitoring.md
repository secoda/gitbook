---
description: Create data monitors for visibility into the health of your data stack
---

# Monitoring

Monitoring is an essential player in maintaining data quality. Within Secoda, you can configure essential monitors to be alerted about changes to your data. Automatically schedule and create thresholds with the ability to track the history of runs and visualize performance of your monitors.

{% hint style="info" %}
If you've chosen Automatic thresholds, it can take up to a week for Secoda to finish learning what the right thresholds should be for your monitors.
{% endhint %}

Choose from the following monitor types:

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

{% hint style="info" %}
**Note:** Read permissions for the source data (in addition to the metadata) are required for the monitoring feature.&#x20;
{% endhint %}

Admins and Editors can find existing Monitors in the Monitors page from the side panel. You can see all the monitors and incidents across the entire platform, and also create new ones from here.&#x20;

<figure><img src="../.gitbook/assets/Screenshot 2023-11-27 at 5.26.07 PM.png" alt=""><figcaption></figcaption></figure>

## Creating Monitors

There are 2 ways to create monitors in Secoda. You can either use the **Monitors** section in the sidebar navigation or through the **Monitors tab** on the resource page.&#x20;

1.  Select the "**Monitors**" section from the sidebar navigation and click "**Add monitor"** (also found within the monitors tab under the resource)**:**&#x20;



    <figure><img src="../.gitbook/assets/Screen Shot 2023-12-05 at 3.39.08 PM.png" alt=""><figcaption><p>Add monitor option on the main monitors page</p></figcaption></figure>


2.  Select the monitor type you want to create and choose the integration you want to create the monitor for (if adding a new monitor from the resource itself, the integration will be pre-selected):



    <figure><img src="../.gitbook/assets/Screen Shot 2023-12-05 at 3.43.42 PM (1).png" alt=""><figcaption></figcaption></figure>


3.  Select one or multiple resources that you'd like to add the monitor to:\


    <figure><img src="../.gitbook/assets/Screen Shot 2023-12-05 at 4.08.55 PM.png" alt=""><figcaption><p>configuration window for monitors<br><br></p></figcaption></figure>
4. Adjust the **Threshold** and **Schedule** to your preferred configuration
   * **Schedule:** Choose between Daily, Every 12, 6 or 3 hours, or Hourly
   * **Threshold:** Automatic or Manual\

5. Once configured, click add monitor and it show now show up within the list of monitors. You can view and edit the configurations from the sidebar on the monitor page

<div align="center">

<figure><img src="../.gitbook/assets/Screen Shot 2023-12-05 at 5.02.38 PM.png" alt="" width="317"><figcaption><p>Configuration details</p></figcaption></figure>

</div>

{% hint style="info" %}
**Note:** You can only add a monitor type which each of the columns support.

For example, if you have 3 numeric columns selected, you can add a "MIN" or "MAX" monitor, but you cannot do it if even one string column is selected in the modal.
{% endhint %}

### Custom SQL Monitors

A user is be able to create a monitor that runs custom SQL to create an output. The only requirement is that the final output of the custom SQL must be a single value.

Follow the same steps as above, but choose "Custom SQL" as the Monitor type. After creating, click into it so that you can add your desired query in the right side panel.

<div align="center">

<figure><img src="../.gitbook/assets/Screenshot 2023-11-27 at 5.22.03 PM.png" alt=""><figcaption><p>Custom SQL monitor</p></figcaption></figure>

</div>

### WHERE clause&#x20;

Standard monitors such as nullness, row count, etc can be modified with custom SQL that’s added as a WHERE clause within the standard SQL.

<div align="center">

<figure><img src="../.gitbook/assets/where clause.png" alt="" width="277"><figcaption><p>Adding WHERE clause</p></figcaption></figure>

</div>

## Managing Monitors

View **Status**, **Last** and **Next Run** details, and a **Chart Visualization** of the monitor's historical performance

<div align="left">

<figure><img src="../.gitbook/assets/Screen Shot 2023-12-05 at 5.33.20 PM.png" alt=""><figcaption></figcaption></figure>

</div>

### Thresholds and Incidents

The lighter green surrounding the main line represent the **threshold** limits - once the threshold is passed, it'll show a red dot indicating an incident

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/88d0fea1-144d-4b61-94c0-903bc22d6275.gif" alt=""><figcaption></figcaption></figure>

Scroll down to see Run history, and filter for triggered Incident Reports. Here you can see any Downstream Resources that may be impacted by the incident.

<figure><img src="../.gitbook/assets/Kapture 2023-12-08 at 13.58.03.gif" alt=""><figcaption></figcaption></figure>

You can either Acknowledge or Resolve the incident by click these buttons below. The incident will be automatically resolved if the numbers go back into a good state (within the threshold).



<div align="center">

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/c64a75ec-8256-4980-8e90-5e322f7fd72b.png" alt="" width="282"><figcaption></figcaption></figure>

</div>

### Errors

You may receive an error on your Monitors for various reasons. The Error will appear under Status. You are able to click into the error to see exactly what went wrong with the Monitor. In the example below, a Custom SQL monitor was chosen but a query was never provided, causing it to error out.

<figure><img src="../.gitbook/assets/Kapture 2024-01-05 at 15.33.43.gif" alt=""><figcaption></figcaption></figure>

## Monitoring Notifications

Ensure that you receive notifications about your monitors by going into your Notification settings. Check off where you'd like to be notified, whether that's in Slack DMs, by email, and/or in the app.\


<div align="left">

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/4be1ef82-00c9-46ba-a9de-b6639784c8e7.png" alt=""><figcaption><p>Monitor notifications</p></figcaption></figure>

</div>

#### Slack Channel for Monitoring notifications

In the Slack integration Channels settings, Admins are able to set the monitoring notifications to go to a specific channel. This can be the same or different channel than what you've set up for other notifications. Learn more [here](../integrations/productivity-tools/slack-connection/#steps-for-setting-up-slack).

<figure><img src="../.gitbook/assets/image (9) (1).png" alt=""><figcaption></figcaption></figure>

## Video resource

{% embed url="https://www.loom.com/share/03c92029f9cd4de4ae11653a2cea6c0c?sid=202df101-4494-44f7-8594-b0606f3cf5d9" %}
