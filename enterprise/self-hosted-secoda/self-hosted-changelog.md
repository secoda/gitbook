---
description: >-
  Self-hosted images are updated less frequently than the Secoda SaaS platform.
  New updates and improvements to the Secoda self-hosted images are listed here.
---

# Self-Hosted Changelog

### v2024.4.0 (October 2, 2024)

**New Features**

* [**Data Quality Score**](https://docs.secoda.co/features/data-quality-score) **(DQS)**: A new public beta feature, automatically scoring data quality across key dimensions such as completeness, accuracy, and consistency at the column and table levels. Includes customizable thresholds and actionable insights for improving data quality.
* [**AI Personas**](https://docs.secoda.co/features/ai-assistant#personas): Introduced role-specific AI personas, allowing users to customize AI interactions for specific roles within their organization. Tailor persona configurations, personalize names and icons, and set resource permissions.
* **New Integrations:** Brand new integrations for [PagerDuty](https://docs.secoda.co/integrations/data-quality-tools/pager-duty), [GCS](https://docs.secoda.co/integrations/data-lakes/google-cloud-storage), [S3](https://docs.secoda.co/integrations/data-lakes/aws-s3), [Hex](https://docs.secoda.co/integrations/data-visualization-tools/hex), and [Matillion](https://docs.secoda.co/integrations/data-pipeline-tools/matillion).
* [**Queries Page**](https://docs.secoda.co/features/queries/extracted-queries)**:** Understand your most popular or slowest queries with the queries tab on resources and the Queries page.&#x20;

**Improvements**

* **Slack Workflow Enhancements**: Improved Slack workflows, making it easier to integrate Secoda with Slack for questions, incident management, and notifications. Slack now syncs bi-directionally with your content in Secoda.
* **UI and Navigation Enhancements**: Improvements to breadcrumbs and enhanced navigation across documentation and the query editor.
* **Monitor Sensitivity Control**: Enhanced controls for adjusting the threshold sensitivity of data monitors, giving users better flexibility over automatic threshold settings.
* **Monitoring Incident Auto-Resolution**: Incidents now auto-resolve when consecutive measurements fall within acceptable ranges, reducing manual intervention.
* **Jira Integration for Incidents**: Secoda users with Jira integrations can now push incidents directly to Jira, simplifying incident management workflows.
* **Filter Enhancements**: Improved suggested filters for faster and more accurate search results. In addition, the AI filter can use natural language to filter your resources.
* **Push to dbt:** Keep metadata synced between Secoda and your dbt repository with the GitHub integration.

For more detailed information on these updates, please visit [Secoda's changelog](https://feedback.secoda.co/changelog).

### v2024.3.2 (July 24, 2024)

This is a patch version update with miscellaneous bug fixes.&#x20;

* Limit the ability to create new workspaces to Admin's only
* Improvements to column selection when creating Monitors

### v2024.3.1 (July 13, 2024)

This is a patch version update with miscellaneous bug fixes.&#x20;

* Show `Verified` column as part of the Resource List

<figure><img src="../../.gitbook/assets/Screenshot 2024-07-24 at 12.25.05 PM.png" alt=""><figcaption></figcaption></figure>

* Improve selection of databases for [SQL Server](../../integrations/databases/microsoft-sql-server/) integration
* Show On Prem version in Workspace settings

### v2024.3.0 (July 2, 2024)

**New Integrations and Integration Improvements**

* [Airflow plugin ](../../integrations/data-pipeline-tools/airflow/#id-3.-plugin)
* [Astronomer](../../integrations/data-pipeline-tools/airflow/#id-2.-astronomer)
* [SQL Server Reporting Services](../../integrations/data-visualization-tools/sql-server-reporting-services/)
* [Monte Carlo](../../integrations/data-quality-tools/monte-carlo/)
* [Superset](../../integrations/data-visualization-tools/superset/)
* Integration of BigQuery table stats such as bytes and row count.
* SSH Tunnels support for Metabase.
* Extracted calculated fields and previews from Looker Studio.
* Introduced Databricks cluster or warehouse options.
* Enabled pulling table and view comments for Hive.
* Added capability to push metadata to Postgres.
* Display of the latest sync status in the integrations table.
* Added support for Snowflake Dynamic Tables and Key Pair Authentication for Snowflake.
* Added support for syncing updated\_at from Salesforce columns.
* Added SSH Tunnel Support for MongoDB.&#x20;

**Filtering, Search & Catalog**

* Enhanced [filtering](../../features/filters.md) functionality and more intuitive nested searches.
* New keyboard shortcuts to open and navigate filters.
* Enhanced search and filter capabilities within Member settings.
* Introduced powerful new [bulk editing](../../resource-and-metadata-management/add-documentation/bulk-editing-resources.md) tools.

**Lineage**

* Display only impacted columns when viewing column lineage.
* Export impact analysis feature.
* Lineage locking and auto-positioning to enhance navigation and usability of lineage graphs.

**AI & Monitoring**

* Implemented [AI access settings](../../features/ai-assistant/#ai-settings-for-admins).
* Improved Monitoring RBAC [permissions](../../features/monitoring.md#monitoring-permissions).
* Added creation date to Monitors.
* Added Monitor subscription capabilities.
* Added Monitoring support for Trino.
* Added Custom Instructions for AI.
* Added embedded AI Assistant in sidebar.

**Properties and Formatting**

* Added new [Related](../../resource-and-metadata-management/relating-resources.md) section in resource sidesheet.
* Added rich resource links and resource metadata popover in Editor.
* Improved copy + paste in the Editor.
* Addition of 'select all' to tags filter.
* Introduced grouped Tags.
* Updated viewer onboarding educational screens.

**Bug Fixes:**

* Fixed incident page crashing.
* Resolved TRUNCATE queries showing as creation query.
* Addressed Glue schema list not showing.
* Fixed Templates in collections page not opening.
* Corrected unchecked Tableau folders showing in Catalog.
* Fixed automation not updating descriptions.
* Addressed content moving in Editor table.
* Corrected row count abbreviation for billions not displaying correctly.
* Fixed Slack usernames not parsed when pushing Questions.
* Resolved Integration sync history display flickering.
* Fixed Refresh Layout button on Lineage graph not working.
* Resolved document's headings with empty ids "{#}".
* Fixed Table of content not clickable.
* Resolved Help Menu not closing when clicking outside of menu.
* Fixed query block in question getting cut off.
* Resolved being unable to resolve comments.
* Numerous other critical and minor bug fixes to enhance stability, performance, and user experience across the platform.

### v2024.2.3 (May 3, 2024)

This is a patch version update with miscellaneous bug fixes.&#x20;

**Catalog**

* Fixed resources not being nested on the sidebar catalog tree

**Queries**

* Fixed `TRUNCATE` queries showing as creation queries on BigQuery
* Fixed query block in questions being cut off

**Integrations**

* Fixed SSL certificate being too weak for Microsoft SQL Server integration
