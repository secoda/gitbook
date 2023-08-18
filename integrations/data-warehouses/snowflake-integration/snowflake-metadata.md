---
description: List of all the metadata that Secoda pulls from/pushes to Snowflake
---

# Metadata Extracted

## Metadata pulled

Secoda pulls the following metadata from Snowflake:

* Tables
  * Name
  * Description
  * Owners
  * Last Updated Timestamp
  * Schema
  * Database
  * Frequent Users
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
  * Value distribution
  * Statistic Value Count
  * Percent Filled&#x20;
  * Unique
* Creation Query
* Common Queries
* Lineage
  * Column -> Column relationships
  * Table -> Table relationships
  * Table -> Dashboard relationships
  * ETL Job -> Table relationships
* Preview of first 50 rows (Optional)

## Metadata pushed

If enabled, Secoda pushes the following metadata to Snowflake:

* Tables - Description
* Columns - Description

It only looks at the tables that have been published and all of their columns. If a table isn't published in Secoda and you run a sync, it will not push back to the source.

{% hint style="warning" %}
Please ensure ensure the `SECODA` role has `INSERT` table privileges, as well as `MODIFY` schema and database. You can check what privileges the role has by running `SHOW GRANTS TO ROLE SECODA`.
{% endhint %}
