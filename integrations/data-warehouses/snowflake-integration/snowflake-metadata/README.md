---
description: List of all the metadata that Secoda pulls from/pushes to Snowflake
---

# Snowflake Metadata Extracted

### Metadata pulled

Secoda pulls the following metadata from Snowflake:

* Tables
  * Name
  * Description
  * Last Updated Timestamp
  * External Usage (Popularity)
  * Schema
  * Database
  * Frequent Users
  * Tags
* Views
  * Name
  * Description
  * Last Updated Timestamp
  * External Usage
  * Schema
  * Database
  * Frequent Users
  * Tags
* Columns
  * Name
  * Description
  * Type
  * Foreign Key
  * Primary Key
  * Tags
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
  * Snowflake Column <-> Snowflake Column
  * Snowflake Table <-> Snowflake Table
  * Snowflake Table <-> Dashboards from other sources
  * Snowflake Table <-> Jobs from other sources
  * Snowflake Column <-> Snowflake View
  * Snowflake Table <-> Snowflake View
* Pipes
  * Name
  * Copy statement
  * Comment
  * Integration
  * Created on
  * Pattern
* Pipe usage history
  * Start time
  * End time
  * Bytes inserted
  * Files inserted
* Streamlit
  * Name
  * Comment
  * Url
* Preview of first 50 rows (Optional)

### Metadata pushed

If enabled, Secoda pushes the following metadata to Snowflake:

* Descriptions
* Tags

It only looks at the tables that have been published and all of their columns. If a table isn't published in Secoda and you run a sync, it will not push back to the source.

{% hint style="warning" %}
Please ensure ensure the `SECODA` role has `INSERT` table privileges, as well as `MODIFY` schema and database. You can check what privileges the role has by running `SHOW GRANTS TO ROLE SECODA`. The SECODA user must also be an owner of the tables.
{% endhint %}
