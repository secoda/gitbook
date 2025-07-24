---
description: List of all the metadata that Secoda pulls from Dataform
---

# Dataform Metadata Extracted

{% hint style="info" %}
Dataform is a secondary integration that adds additional metadata on to your data warehouse or relational database tables. Before connecting Dataform make sure to connect a data warehouse or relational database first. These include BigQuery, Redshift, etc.
{% endhint %}

### What does Secoda extract from Dataform?

* Repositories
  * Name
* Release Configurations
  * Name
* Workflow Configurations
  * Name
  * Creat Time
  * Update Time
  * Cron Schedule (if present)
* Workflow Invocations
  * Name
  * Timing (start/end times)
  * State/Status
* Compilation Results
  * Name/ID
  * Associated Workflow Config
* Relations (Tables/Views)
  * Database/Schema
  * Name
  * Description
  * Column Names
  * Column Descriptions
  * Policy Tags
  * Tags
  * Dependencies (lineage information)
* Assertions(Tests)
  * Test Suites (grouped by database.schema)
  * Name
  * Select Query
  * Disabled Status
  * Tags
  * Dependencies (lineage information)
  * Job Runs&#x20;
    * Status&#x20;
    * Start Time&#x20;
    * End Time
    * failure reason
    * select\_query
