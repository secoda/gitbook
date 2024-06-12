---
description: List of all the metadata that Secoda pulls from Postgres
---

# Postgres Metadata Extracted

### Metadata pulled

Secoda pulls the following metadata from Postgres:

* Tables and Views
  * Name
  * Description
  * Last Updated Timestamp
  * Schema
  * Database
* View Definition (Table Creation Query)
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
* Lineage
  * Postgres Table <-> Postgres Table
  * Postgres View <-> Postgres Table
  * Postgres View <-> Postgres Column
  * Postgres Column <-> Postgres Column
  * Postgres Table/View <-> Tables from other sources
  * Postgres Table/View <-> Dashboards from other sources
  * Postgres Table/View <-> Jobs from other sources
* Preview of first 50 rows (Optional)

### Metadata pushed <a href="#metadata-pushed" id="metadata-pushed"></a>

If enabled, Secoda pushes the following metadata to Postgres:

* Tables
  * Description
* Columns
  * Description
