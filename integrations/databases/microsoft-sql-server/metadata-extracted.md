---
description: List of all the metadata that Secoda pulls from Microsoft SQL Server
---

# Metadata Extracted

Secoda pulls the following metadata from Microsoft SQL Server:

* Tables and Views
  * Name
  * Description
  * Schema
  * Database
* Columns
  * Name
  * Description
  * Type
  * Sort Order
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
* MS SQL Stored Procedures
  * Creates lineage between the tables that are in the stored procedure&#x20;
  * Adds the stored procedure under the Queries tab of the associated tables
* Lineage
  * MS SQL Table <-> MS SQL Table
  * MS SQL Column <-> MS SQL Column
  * MS SQL Column <-> MS SQL View
  * MS SQL Table <-> MS SQL Table
  * MS SQL Table/View <-> Tables from other sources
  * MS SQL Table/View <-> Dashboards from other sources
  * MS SQL Table/View <-> Jobs from other sources
* Preview on first 50 rows (Optional)
