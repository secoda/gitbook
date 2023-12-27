---
description: List of all the metadata that Secoda pulls from/pushes to BigQuery
---

# Metadata Extracted

### Metadata pulled

Secoda pulls the following metadata from BigQuery:

* Tables/Views
  * Name
  * Description
  * Last Updated Timestamp
  * Schema
  * Database
  * Frequent users
* Fields (Fields are referred to as Columns in Secoda)
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
* Stored Procedures (Stored Procedures are referred to as Creation Queries in Secoda)
* Queries (Popularity)
* Lineage
  * BQ Column <-> BQ Column
  * BQ Table <-> BQ Table
  * BQ Column <-> BQ View
  * BQ Table <-> Tables from other sources
  * BQ Table <-> Dashboards from other sources
  * BQ Table, Views <-> Runs from other sources
* Preview of first 50 rows (Optional)

### Metadata pushed

If enabled, Secoda pushes the following metadata to BigQuery:

* Tables
  * Description
* Columns
  * Description
