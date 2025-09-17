---
description: Take a look into the usage of your workspace
---

# Analytics

Admins and Editors have access to the Analytics dashboard and overview pages which showcases how their Secoda workspace is being used. They also receive a weekly email that highlights the metrics in this analytics dashboard.

## Feature Overview

Secoda provides comprehensive overview pages for key features that give you insights into usage, performance, and health metrics. Each overview page includes interactive metric cards and time-series charts to help you monitor and understand your data operations.

### Monitors Overview

The Monitors Overview page provides a comprehensive view of your data monitoring health and incident management.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/d4b92872-de7b-44d7-914a-4efb94911fba.png" alt=""><figcaption></figcaption></figure>

* **Normal**: Number of monitors currently passing their checks
* **Failed**: Number of monitors that have failed their latest checks
* **Open Incidents**: Count of active incidents requiring attention
* **Acknowledged Incidents**: Count of incidents that have been acknowledged but not yet resolved

***

### Policies Overview

The Policies Overview page helps you track data governance compliance and policy enforcement across your organization.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/5f84fa53-a643-412e-8e42-59f65b810687.png" alt=""><figcaption></figcaption></figure>

* **OK**: Number of policies currently in compliance
* **Needs Remediation**: Number of policies requiring attention or action

***

### Automations Overview

The Automations Overview page provides insights into your automated data management processes and their effectiveness.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/2c17f85b-6d7d-4fb0-8497-9d905dbb1b42.png" alt=""><figcaption></figcaption></figure>

* **Automation Runs**: Total number of automation executions
* **Tasks Automated**: Count of individual tasks completed through automation



***

### Access Requests Overview

The Access Requests Overview page helps you manage and monitor data access workflows across your organization.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/3f2ee0be-9f6c-4fd9-a016-c8f8c9ec50e5.png" alt=""><figcaption></figcaption></figure>

* **Open**: Number of pending access requests awaiting review
* **Active**: Count of currently granted and active access permissions
* **Denied**: Number of requests that have been rejected
* **Closed**: Total of expired and cancelled requests

***

### Integrations Overview

The Integrations Overview page provides visibility into your data source connections and synchronization health.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/a485e44e-658c-43ec-a27d-35d3014096be.png" alt=""><figcaption></figcaption></figure>

* **Completed Sync**: Number of integrations with successful recent synchronizations
* **Failed Sync**: Count of integrations experiencing sync failures

***

## Reports

Create Reports to organize your Analytics widgets into separate themes. For example, you can have one Report that shows stats on your users, another on documentation, and another on Snowflake costs.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/9faa7247-5186-4050-813c-d38b39785413.png" alt=""><figcaption></figcaption></figure>

### Filtering

You are able to filter on the widgets in the dashboard. In the gif below, you can see how to filter on "Documented resources".

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/e82ff41a-0f9e-417e-aab9-2695d2dbecca.png" alt=""><figcaption></figcaption></figure>

### Identifying undocumented resources

Another important metric you can filter for here is **undocumented popular resources**. This would be an important metric to know about so that you can make sure to build out the documentation since your users are often visiting these resources.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/02963fdc-8fea-4050-9fd1-ece650bece2f.png" alt=""><figcaption></figcaption></figure>

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
* **Verified Resources:** Line chart for the percentage of resources that are verified.&#x20;

#### Tests

* **dbt Test Results**: Various charts showing test execution results and statistics including pass percentage, number of failures, and model coverage.

#### Costs

* **Snowflake Analytics**: Multiple widgets tracking costs, credits, query volume, and usage metrics.

Each widget can be customized with:

* Different time ranges (weekly, monthly, all-time)
* Various visualization types (line charts, bar charts, tables)
* Size adjustments (small, medium, large, full)
* Custom filters based on the metric type

