# Metadata Extracted

{% hint style="info" %}
dbt is a secondary integration that adds additional metadata on to your data warehouse or relational database tables. Before connecting dbt make sure to connect a data warehouse or relational database first. These include Snowflake, BigQuery, Postgres, Redshift, etc.
{% endhint %}

## What does Secoda extract from dbt Cloud?

* Models Metadata:&#x20;
  * Description&#x20;
  * Owner&#x20;
  * URL&#x20;
  * Compiled SQL&#x20;
  * Updated Time
* Columns Metadata:&#x20;
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
* Jobs:&#x20;
  * Name&#x20;
  * URL&#x20;
  * Job Runs&#x20;
    * Status&#x20;
    * Start Time&#x20;
    * End Time
* Metrics:
  * Name&#x20;
  * Type&#x20;
  * Dimensions&#x20;
  * Time Grains
