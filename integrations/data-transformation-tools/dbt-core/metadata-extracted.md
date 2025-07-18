---
description: List of all the metadata that Secoda pulls from dbt Core
---

# dbt Core Metadata Extracted

## What does Secoda extract from dbt Core?

{% hint style="info" %}
dbt is a secondary integration that adds additional metadata on to your data warehouse or relational database tables. Before connecting dbt make sure to connect a data warehouse or relational database first. These include Snowflake, BigQuery, Postgres, Redshift, etc.
{% endhint %}

* Models:&#x20;
  * Description&#x20;
  * URL&#x20;
  * Compiled SQL&#x20;
* Columns:&#x20;
  * Description&#x20;
  * Tags&#x20;
  * Updated Time
* Tests:&#x20;
  * Name&#x20;
  * Description&#x20;
  * URL&#x20;
  * Tags&#x20;
  * Status&#x20;
  * Error&#x20;
  * Compiled code
* Metrics (Referred to as Dictionary terms in Secoda) on dbt v1.5 or less:
  * Name&#x20;
  * Type&#x20;
  * Dimensions&#x20;
  * Time Grains
* Lineage:
  * dbt Jobs <-> external Tables
  * dbt Exposures <-> external Tables
* Groups (Groups are referred to as `USER_GROUPS` in Secoda)
* Contracts (dbt Contracts are referred to as `TEST` in Secoda)
* Exposures
  * name&#x20;
  * description
  * tags
  * owners (from meta.owner)
  * url
  * type
    * The exposure type can be a dashboard, notebook, analysis, ml, or application
  * depends\_on&#x20;
* Monitors
  * See [#monitors-as-code](../../../features/monitoring.md#monitors-as-code "mention")on how to implement monitors in your model yml
