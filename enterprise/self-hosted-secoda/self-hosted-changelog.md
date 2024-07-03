---
description: >-
  Self-hosted images are updated less frequently than the Secoda SaaS platform.
  New updates and improvements to the Secoda self-hosted images are listed here.
---

# Self-Hosted Changelog

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
