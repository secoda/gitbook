---
description: Create data monitors for visibility into the health of your data stack
---

# Monitoring

{% hint style="warning" %}
Monitoring is not live for all users at the moment. If you'd like early access to test it out, please fill out this form: [https://tally.so/r/n99eNX](https://tally.so/r/n99eNX).
{% endhint %}

Monitoring is an essential player in maintaining data quality. Within Secoda, you can configure essential monitors to be alerted about changes to your data. Automatically schedule and create thresholds with the ability to track the history of runs and visualize performance of your monitors.

Choose from the following monitor types:

* **Nullness** - The percentage of values in a column that are null
* **Cardinality** - The number of distinct values of a given column
* **Uniqueness** - The percentage of values in a column that are unique
* **Freshness** - The time elapsed since last update
* **Row Count** - The number of rows over time
* **Maximum** - The highest value of a numeric column
* **Mean** - The arithmetic mean of a numeric column
* **Minimum** - The lowest value of a numeric column

The monitor will alert if any of these values are higher or lower than expected.

## How to create monitors

1. Navigate to the table or column that you'd like to add a monitor for
2.  Click into the "Monitors" tab > "New Monitor"&#x20;

    <figure><img src="../.gitbook/assets/Screenshot 2023-09-20 at 11.21.50 AM.png" alt=""><figcaption></figcaption></figure>
3.  Select one or multiple resources that you'd like to add the Monitor for.

    <div align="left">

    <figure><img src="../.gitbook/assets/Screenshot 2023-09-20 at 11.26.00 AM.png" alt="" width="188"><figcaption><p>Select resource</p></figcaption></figure>

    </div>
4.  Select which monitor type(s) (can be more than one) and click "Add Monitors".&#x20;



    <div align="left">

    <figure><img src="../.gitbook/assets/Screenshot 2023-09-20 at 11.55.04 AM.png" alt="" width="188"><figcaption><p>Monitor types</p></figcaption></figure>

    </div>
5. Once created, you can find it under the "Monitors" tab in the Catalog
6. Click into the monitor to further edit and see the history of the monitor's runs
   * Edit Configuration details like Schedule, Threshold and Sensitivity&#x20;
     * Schedule - Choose between Daily, Every 12, 6 or 3 hours, or Hourly
     * Threshold - Automatic or Manual
     * Sensitivity - More or less sensitive threshold

<div align="left">

<figure><img src="../.gitbook/assets/Screenshot 2023-09-20 at 11.33.40 AM (1).png" alt="" width="153"><figcaption><p>Configuration details</p></figcaption></figure>

</div>

## How to manage monitors

View Status, Last and Next Run details, and a Chart Visualization of the monitor's historical performance

<div align="left">

<figure><img src="../.gitbook/assets/Screenshot 2023-09-20 at 11.58.03 AM.png" alt=""><figcaption></figcaption></figure>

</div>

The lighter green surrounding the main line represent the threshold limits - once the threshold is passed, it'll show a red dot indicating an incident

<figure><img src="../.gitbook/assets/Kapture 2023-09-21 at 12.13.04.gif" alt=""><figcaption></figcaption></figure>

Scroll down to see Run history, and filter for triggered Incident Reports. Here you can see any Downstream Resources that may be impacted by the incident.

<figure><img src="../.gitbook/assets/Kapture 2023-09-21 at 12.21.17.gif" alt=""><figcaption></figcaption></figure>

You can either Acknowledge or Resolve the incident by click these buttons below. The incident will be automatically resolved if the numbers go back into a good state (within the threshold).

<div align="left">

<figure><img src="../.gitbook/assets/Screenshot 2023-09-21 at 12.29.23 PM.png" alt="" width="282"><figcaption></figcaption></figure>

</div>

## Monitoring notifications

Ensure that you receive notifications about your monitors by going into your Notification settings. Check off where you'd like to be notified, whether that's in Slack, by email, and/or in the app.

<div align="left">

<figure><img src="../.gitbook/assets/Screenshot 2023-09-20 at 3.17.05 PM.png" alt=""><figcaption><p>Monitor notifications</p></figcaption></figure>

</div>
