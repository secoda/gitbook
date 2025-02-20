---
description: List of all the metadata that Secoda pulls from ClickHouse
---

# ClickHouse Metadata Extracted

#### Metadata pulled <a href="#metadata-pulled" id="metadata-pulled"></a>

Secoda pulls the following metadata from ClickHouse:

* Tables
  * Name
  * Description
  * Schema
  * Database
  * External Usage (Popularity)
  * External Updated At
  * Byte Size
  * Rows
* Views
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
  * Percent Filled
  * Unique
* Creation Query
* Common Queries
* Lineage
  * ClickHouse Column <-> ClickHouse Column
  * ClickHouse View <-> ClickHouse View
  * ClickHouse Table <-> ClickHouse Table
  * ClickHouse Table <-> ClickHouse View
  * ClickHouse Table <-> Dashboards from other sources
  * ClickHouse Table <-> Tables from other sources
  * ClickHouse Table, Views <-> Jobs from other sources
* Preview of first 50 rows (Optional)
