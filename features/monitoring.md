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

{% hint style="info" %}
Note: Read permissions for the source data (in addition to the metadata) are required for the monitoring feature.&#x20;
{% endhint %}

## How to create monitors

1. Navigate to the table or column that you'd like to add a monitor for
2.  Click into the "Monitors" tab > "New Monitor"

    <figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/40ae73c2-f895-4d69-a17a-4fc1736ca827.png" alt=""><figcaption></figcaption></figure>
3.  Select one or multiple resources that you'd like to add the Monitor for.

    <div align="left">

    <figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/eef8e012-ac15-4c7c-94bf-c1c0f156ac6f.png" alt="" width="188"><figcaption><p>Select resource</p></figcaption></figure>

    </div>
4.  Select which monitor type(s) (can be more than one) and click "Add Monitors".

    <div align="left">

    <figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/ae1144cb-8b55-4e25-8af8-634777628335.png" alt="" width="188"><figcaption><p>Monitor types</p></figcaption></figure>

    </div>
5. Once created, you can find it under the "Monitors" tab in the Catalog
6. Click into the monitor to further edit and see the history of the monitor's runs
   * Edit Configuration details like Schedule, Threshold and Sensitivity
     * Schedule - Choose between Daily, Every 12, 6 or 3 hours, or Hourly
     * Threshold - Automatic or Manual
     * Sensitivity - More or less sensitive threshold

<div align="left">

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/f4f4df5c-d851-428e-a672-9f0da1cd7df7.png" alt="" width="153"><figcaption><p>Configuration details</p></figcaption></figure>

</div>

{% hint style="info" %}
Note: You can only add a monitor type which each of the columns support.

For example, if you have 3 numeric columns selected, you can add a "MIN" or "MAX" monitor, but you cannot do it if even one string column is selected in the modal.
{% endhint %}

## How to manage monitors

View Status, Last and Next Run details, and a Chart Visualization of the monitor's historical performance

<div align="left">

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/e499d48e-1cbe-49ba-bb49-1b19226ed312.png" alt=""><figcaption></figcaption></figure>

</div>

The lighter green surrounding the main line represent the threshold limits - once the threshold is passed, it'll show a red dot indicating an incident

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/88d0fea1-144d-4b61-94c0-903bc22d6275.gif" alt=""><figcaption></figcaption></figure>

Scroll down to see Run history, and filter for triggered Incident Reports. Here you can see any Downstream Resources that may be impacted by the incident.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/3270f4bf-bc58-41aa-a5c8-06b5e4a401e4.gif" alt=""><figcaption></figcaption></figure>

You can either Acknowledge or Resolve the incident by click these buttons below. The incident will be automatically resolved if the numbers go back into a good state (within the threshold).

<div align="left">

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/c64a75ec-8256-4980-8e90-5e322f7fd72b.png" alt="" width="282"><figcaption></figcaption></figure>

</div>

## Monitoring notifications

Ensure that you receive notifications about your monitors by going into your Notification settings. Check off where you'd like to be notified, whether that's in Slack, by email, and/or in the app.

<div align="left">

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/4be1ef82-00c9-46ba-a9de-b6639784c8e7.png" alt=""><figcaption><p>Monitor notifications</p></figcaption></figure>

</div>

## Video resource

{% embed url="https://www.loom.com/share/03c92029f9cd4de4ae11653a2cea6c0c?sid=202df101-4494-44f7-8594-b0606f3cf5d9" %}
