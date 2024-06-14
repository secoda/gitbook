---
description: List of all the metadata that Secoda pulls from Airflow
---

# Airflow Metadata Extracted

### What does Secoda extract from Airflow?

Whether you are using the Airflow APIs or the Secoda Plug in, the following information is extracted from Airflow.&#x20;

* DAGs
  * Name
  * Description
  * Owners
  * URL
  * Runs
    * Name (ID of the Run)
    * Status
    * Created At (Timestamp)
    * Ended At (Timestamp)
* Tasks
  * Name
  * Description
  * Started At (Timestamp)
  * Ended At (Timestamp)

If you're using the Secoda Plugin for Airflow, Secoda will also extract:

* Queries
* Lineage&#x20;
  * Secoda will parse the SQL query in each DAG to determine the source and target resources and build lineage

{% hint style="info" %}
Lineage and Queries will only work if the Operators used in the DAGS expose SQL queries. It will work best with Snowflake and BigQuery Operators.&#x20;
{% endhint %}
