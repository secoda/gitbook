---
description: List of all the metadata that Secoda pulls from/pushes to Snowflake
---

# Metadata Extracted

### Metadata pulled

Secoda pulls the following metadata from Redshift:

* Tables
  * Name
  * Description
  * Schema
  * Database
  * External Usage (Popularity)
  * External Updated At
* Views&#x20;
  * Name
  * Description
  * Schema
  * Database
  * External Usage (Popularity)
  * External Updated At
* Columns
  * Name
  * Description
  * Type
  * Foreign Key
  * Primary Key
* Column Profile
  * Min
  * Max
  * Median
  * STD Deviation
  * Value Distribution
  * Statistic Value Count
  * Percent Filled&#x20;
  * Unique
* Creation Query
* Common Queries
* Lineage
  * Redshift Column <-> Redshift Column
  * Redshift View <-> Redshift View
  * Redshift Table <-> Redshift Table
  * Redshift Table <-> Redshift View
  * Redshift Table <-> Dashboards from other sources
  * Redshift Table <-> Tables from other sources
  * Redshift Table, Views <-> Jobs from other sources
* Preview of first 50 rows (Optional)

### Metadata pushed

If enabled, Secoda pushes the following metadata to Redshift:

* Tables
  * Description
* Columns
  * Description
