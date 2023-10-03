# Metadata Extracted

{% hint style="info" %}
dbt decorates the models with the following metadata. The models or tables aren't actually stored in dbt, they are created via dbt jobs, and stored in the connected database or data warehouse.
{% endhint %}

## What does Secoda extract from dbt Cloud?

* Models:&#x20;
  * Name&#x20;
  * Description&#x20;
  * Owner&#x20;
  * URL&#x20;
  * Compiled SQL&#x20;
  * Updated Time
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
