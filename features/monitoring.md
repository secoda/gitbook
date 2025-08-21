---
description: Create data monitors for visibility into the health of your data stack
---

# Monitors

### Introduction

Monitoring plays a crucial role in maintaining data quality by allowing you to configure alerts for changes in your data. Automatically schedule monitors and set thresholds to track run history and visualize monitor performance.

Admins and Editors can access existing Monitors from the Monitors page accessible via the side panel. Here, you can view all monitors and incidents across the platform and create new ones.

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

To learn about how our current customers are using Monitors in Secoda to improve their data quality, check out this list of [monitoring-use-cases.md](monitoring/monitoring-use-cases.md "mention").

{% hint style="info" %}
**Note:** Read permissions for the source data (in addition to the metadata) are required for the monitoring feature.
{% endhint %}

### Types of monitors

Select from a variety of Monitors to suit your needs:

**Tables**

* **Row Count** - The number of rows over time
* **Freshness** - The time elapsed since last update

**Columns**

* **Cardinality** - The number of distinct values of a given column
* **Maximum** - The highest value of a numeric column
* **Minimum** - The lowest value of a numeric column
* **Mean** - The arithmetic mean of a numeric column
* **Null Percentage** - The percentage of values in a column that are null
* **Unique Percentage** - The percentage of values in a column that are unique
* [**Custom SQL**](monitoring.md#custom-sql-monitors) - Define a monitor by writing your own SQL query

**Pipelines**

* **Job duration** - Average length of job runs
* **Job error rate** - Percentage of failed job runs
* **Job success rate -** Percentage of successful job runs

**Snowflake**

* **Cost -** Daily total cost
* **Query Volume -** Daily queries run
* **Compute Credits -** Daily compute credits consumed
* **Storage Usage -** Total storage usage

The monitor will alert if any of these values are higher or lower than expected.

### Creating monitors

Monitors can be created via the **Monitors** section in the sidebar or through the **Monitors tab** on the resource page:

1. Navigate to "**Monitors**" and click "**Create monitor."**

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/9aca8ba5-cbcf-4995-93d0-0f89a8429658.png" alt=""><figcaption></figcaption></figure>

2. Choose the monitor type and select the integration. If adding a new Monitor from the resource itself, the integration will be pre-selected.

<figure><img src="../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

3. Select one or multiple resources that you'd like to add the monitor to.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/aa102bfb-7046-457a-a27c-29034cca940a.png" alt=""><figcaption></figcaption></figure>

4. Adjust the **Threshold** and **Schedule** to your preferred configuration.

* **Schedule Options:** Daily, Every 12, 6 or 3 hours, or Hourly
* **Threshold:** Automatic or Manual
  * Note: For Automatic thresholds to be set, it can take 4 days for hourly, 6 days for multiple times a day, and 8-9 days for daily monitors.

5. Once configured, click add monitor and it show now show up within the list of monitors. You can view and edit the configurations from the sidebar on the monitor page

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/1c9e6d48-4f85-4648-a70d-042cb01ed60f.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Note:** You can only add a monitor type which each of the columns support.

For example, if you have 3 numeric columns selected, you can add a "MIN" or "MAX" monitor, but you cannot do it if even one string column is selected in the modal.
{% endhint %}

{% hint style="info" %}
**Note:** The monitor status is `Pending` during the time it is queued to run for the first time.
{% endhint %}

#### Custom SQL Monitors

A user is be able to create a monitor that runs custom SQL to create an output. The only requirement is that the final output of the custom SQL must be a single value.

Follow the same steps as above, but choose "Custom SQL" as the Monitor type. After creating, click into it so that you can add your desired query in the right side panel.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/f1c3d6ac-41ea-4965-af82-eabe7b4c5e5c.png" alt=""><figcaption></figcaption></figure>

#### WHERE clause

Standard monitors such as nullness, row count, etc can be modified with custom SQL that’s added as a WHERE clause within the standard SQL.

<div align="center"><figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/0e0b3170-52c0-43f1-882b-b3747af5f804.png" alt="" width="277"><figcaption><p>Adding WHERE clause</p></figcaption></figure></div>

### Managing monitors

View **Status**, **Last** and **Next Run** details, and a **Chart Visualization** of the monitor's historical performance.

<div align="left"><figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/f470b8d4-08eb-47ce-b27d-24b1bb09a2d1.png" alt=""><figcaption></figcaption></figure></div>

#### Thresholds and Incidents

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

#### Annotations

The **Monitoring Annotations** feature provides a way to mark specific data points within monitoring incidents, giving teams a deeper context and helping refine automatic thresholds over time. This feature includes a **Normal** button, which allows users to indicate that a particular data point is not an anomaly, but rather expected behavior.

**Using Monitoring Annotations with the Normal Button**

1. Navigate to the Incident that you wish to annotate.
2. Select the **Normal** button for the data point that you want to classify as expected.
3. This action marks the data point as typical, contributing to the accuracy of Secoda's automatic thresholding over time.

By tagging data points through Monitoring Annotations, you help Secoda’s monitoring become more attuned to your data’s unique patterns, reducing false alerts and improving the identification of true anomalies.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/90a0dd5c-8350-41e5-b118-e8ce9c66f46d.gif" alt=""><figcaption><p>Monitor Annotations</p></figcaption></figure>

#### Errors

You may receive an error on your Monitors for various reasons. The Error will appear under Status. You are able to click into the error to see exactly what went wrong with the Monitor. In the example below, a Custom SQL monitor was chosen but a query was never provided, causing it to error out.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/268a5907-a2bc-4b80-9d2d-ff8edbbab26b.gif" alt=""><figcaption></figcaption></figure>

### Monitoring permissions

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

### Monitoring notification rules

Configure intelligent notification rules to ensure the right people receive alerts at the right time. Notification rules provide granular control over when, how, and to whom monitoring alerts are sent, helping teams respond efficiently to data quality issues.

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

#### Creating Notification Rules

Navigate to **Settings > Notifications > Monitoring Rules** to create and manage your notification rules. Each rule defines:

1. **Trigger Conditions:** When the rule activates
2. **Recipients:** Who receives notifications
3. **Delivery Channels:** How notifications are sent

#### Trigger Conditions

**Monitor Status Triggers:**

* **Incident Created:** New monitoring incidents
* **Incident Resolved:** When incidents are resolved
* **Monitor Error:** Monitor execution failures
* **Threshold Breached:** Specific threshold violations

**Filtering Options:**

* **Severity Levels:** Critical, Warning, Info
* **Resource Filters:** Specific tables, columns, or tags
* **Integration Type:** Filter by data source
* **Teams:** Scope to team-owned resources

#### Recipients and Delivery

**Recipient Types:**

* **Individual Users:** Direct email or username targeting
* **Teams:** All members of designated teams
* **Resource Owners:** Automatic owner notifications
* **Role-Based:** Users with specific workspace roles

**Delivery Channels:**

* **Slack:** DMs, channel posts, or threaded replies
* **Email:** HTML templates with incident summaries
* **In-App:** Real-time notifications in Secoda interface

By implementing focused notification rules, teams ensure critical data quality issues receive appropriate attention while avoiding alert fatigue.

Notifications for monitor incidents are issued only after the first occurrence following a successful run. The same incident will not trigger new alerts unless the issue has been resolved and another incident occurs. This policy minimizes repetitive alerts and ensures that notifications remain meaningful and actionable.

**Configuring Slack Channel Notifications**

Admins can direct monitoring notifications to specific Slack channels, distinct from other notification settings. This ensures that the right team members are alerted promptly. For detailed steps on setting this up, visit [here](../extensions/slack-connection/#steps-for-setting-up-slack).

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/138d2dd7-a4f6-4adf-a404-ff041566eabe.png" alt=""><figcaption><p>Example Slack notification</p></figcaption></figure>

**Email Monitoring Notifications**

Email notifications provide direct links to the relevant sections in Secoda. As shown in the image below, clicking the "Open Secoda" link takes you to the Inbox notification, while other links direct you to specific incidents or tables.

### Monitors as code

You can declare Secoda monitors directly in your dbt model YAML files. These monitors are managed entirely through code and cannot be modified through the Secoda UI. Changes are applied when the dbt integration syncs with Secoda.

#### Monitor Configuration Formats

Monitors can be specified using two formats:

**List Format (Default Configuration)**

```yaml
monitors:
  - mean
  - max
  - null_percentage
```

When using list format, each monitor uses these default settings:

* Automatic thresholds (sensitivity: 5)
* Daily schedule (runs once per day at UTC midnight)
* Both upper and lower bounds
* Auto-generated monitor name

**Dictionary Format (Custom Configuration)**

```yaml
monitors:
  mean: {}  # Empty dict for default configuration (same defaults as list format)
  null_percentage:
    name: "Custom Null Check"
    thresholds:
      sensitivity: 8
      bounds: lower
```

**Array Format (Multiple Monitors per Metric Type)**

You can also create multiple monitors for the same metric type using array syntax:

```yaml
monitors:
  custom_sql:
    - key: daily_record_count
      name: "Daily Record Count"
      query: "SELECT COUNT(*) FROM orders WHERE date = CURRENT_DATE"
      thresholds:
        method: manual
        min: 1000
        max: 10000
    - key: average_order_value
      name: "Average Order Value"
      query: "SELECT AVG(total_amount) FROM orders WHERE date = CURRENT_DATE"
      thresholds:
        method: automatic
        sensitivity: 7
    - key: cancelled_orders_ratio
      name: "Cancelled Orders Ratio"
      query: "SELECT COUNT(CASE WHEN status = 'cancelled' THEN 1 END) * 100.0 / COUNT(*) FROM orders"
      thresholds:
        method: manual
        min: 0
        max: 5
  row_count:
    name: "Single Row Count Monitor"  # Single config still works
```

{% hint style="info" %}
**Recommendation**: When using array format, it's recommended to add a `key` field with a unique string identifier for each monitor (e.g., `daily_record_count`, `average_order_value`). This key should remain constant and helps maintain monitor identity across configuration changes.
{% endhint %}

You can mix both formats across different models and columns, but each individual `monitors` section must use either list or dictionary format, not both. Use list format for simplicity when default settings are sufficient, and dictionary format when you need to customize any monitor settings.

#### Available Monitor Types

**Table-Level Monitors**

* `row_count`: Tracks number of rows
* `freshness`: Monitors last update time (Snowflake/Redshift only)
* `custom_sql`: Execute custom SQL queries

**Column-Level Monitors**

* `mean`: Average value
* `max`: Maximum value
* `min`: Minimum value
* `cardinality`: Number of unique values
* `null_percentage`: Percentage of null values
* `unique_percentage`: Percentage of unique values

#### Configuration Options

Here are all available configuration properties with their default values:

```yaml
monitors:
  metric_name:
    # Threshold Configuration
    thresholds:
      method: automatic   # or manual
      min: null           # required if method is manual
      max: null           # required if method is manual
      sensitivity: 5      # scale 1-10, used for automatic method
      bounds: both        # or upper or lower
    
    # Schedule Configuration
    schedule:
      cadence: daily     # or hourly
      hour_utc: 0        # hour of day (0-23) for daily cadence
      frequency: 1       # run frequency in hours for hourly cadence
    
    # General Configuration
    name: ""             # custom monitor name
    description: ""      # optional description
    query: null          # required for custom_sql monitors
```

#### Complete Example

```yaml
version: 2
models:
  - name: stg_orders
    meta:
      secoda:
        monitors:
          custom_sql:
            query: "SELECT AVG(amount) FROM analytics.dbt_prod.stg_orders"
            schedule:
              cadence: hourly
          row_count:
            name: "Orders Volume Monitor"
            thresholds:
              method: manual
              min: 50
              max: 500
    columns:
      - name: order_amount
        meta:
          secoda:
            monitors:
              - mean
              - max
              - null_percentage
      - name: status
        meta:
          secoda:
            monitors:
              unique_percentage: {}
              cardinality:
                thresholds:
                  method: manual
                  min: 3
                  max: 10
```

### Monitoring integrations

The following integrations support monitoring

1. BigQuery
2. Snowflake
3. Redshift
4. PostgreSQL
5. Databricks
6. SingleStore
7. Synapse
8. Microsoft SQL Server (MSSQL)
9. Trino
10. Oracle
11. MotherDuck
12. ClickHouse

### Best practices

To optimize the effectiveness of data monitoring and manage resource utilization, consider these best practices:

1. **Selective Monitoring:** Focus on the most critical data elements. Prioritize columns and tables that are essential for your business operations to avoid unnecessary strain on resources.
2. **Optimize Frequency:** Set monitoring frequencies that balance timeliness and resource consumption. For many applications, configuring monitors to run **daily** is sufficient to catch issues without incurring excessive costs.
3. **Regular Reviews:** Periodically review data quality monitoring configurations. This ensures that your monitoring strategies stay aligned with evolving business needs and data landscapes.
4. **Workflow Integration:** Embed monitoring alerts into your team’s daily workflows using tools like Slack or email (see [#monitoring-notifications](monitoring.md#monitoring-notifications "mention")). This ensures that the right personnel are promptly notified, enabling swift action.
5. **Documentation and Training:** Keep detailed documentation of your monitor setups and procedures. Train your team on the importance of monitoring and the actions required when specific alerts are triggered.
6. **Trend Analysis:** Leverage historical data from your monitoring activities to identify trends and patterns. This analysis can help refine your data management practices and predictive monitoring over time.

By following these guidelines, you can ensure your monitoring processes are both efficient and effective, providing critical insights while maintaining control over costs and resource use.
