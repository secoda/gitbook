---
description: An overview of the Airflow integration with Secoda
---

# Airflow

{% content-ref url="metadata-extracted.md" %}
[metadata-extracted.md](metadata-extracted.md)
{% endcontent-ref %}

## **Getting Started with Airflow** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

There are two ways to connect Airflow to Secoda:

1. Pull method: Secoda uses the Airflow Rest API to pull the metadata from your Airflow instance
2. Push method: using Secoda's airflow provider, you can add callbacks to certain DAGs and tasks so they get pushed to Secoda.

### Pull Method

There are three steps to get started using Airflow with Secoda:

1. Enable the Airflow REST API
2. Connect Airflow to Secoda
3. Whitelist Secoda IP Address

#### **Enable the Airflow REST API** <a href="#h_5679925c3a" id="h_5679925c3a"></a>

Secoda uses the Airflow stable REST API, which is only available on Airflow v2.0+. For Secoda to retrieve metadata from Airflow, you need to enable your Airflow's REST API. To do this, edit your `airflow.cfg` file and change the line below to `airflow.api.auth.backend.basic_auth`\\

```
[api] auth_backend = airflow.api.auth.backend.deny_all
```

After changing this is what the line should look like:

```
[api] auth_backend = airflow.api.auth.backend.basic_auth
```

#### **Connect Airflow to Secoda** <a href="#h_2cd5acf282" id="h_2cd5acf282"></a>

After enabling the Airflow REST API, the next step is to connect Secoda:

1. In the Secoda App, select ‘Add Integration’ on the Integrations tab
2. Search for and select ‘Airflow’
3. Enter your Airflow user and password. This information is kept encrypted.
4. Click 'Connect'

#### Security <a href="#h_4e3c0bcf41" id="h_4e3c0bcf41"></a>

VPCs keep servers inaccessible to traffic from the internet. With VPC, you’re able to designate specific web servers access to your servers. In this case, you will be whitelisting the Secoda IPs to read from your Airflow instance.

Allow Secoda to access your Airflow API from the [Secoda IP Address](../../../faq.md#what-are-the-ip-addresses-for-secoda).

### Push Method

This method will push metadata from your Airflow instance to Secoda. Then on an extraction, Secoda will process all the pushed metadata instead of directly pulling from the API.

**Create an API Key**

Navigate to your workspace settings on Secoda. Click on the “API” to get a list of your API Keys.

Click on “Generate New API Key” button and then write down the generated key. Please keep this key somewhere safe and do not share with others. This key will have the same access to your Secoda workspace as the user who created it.

#### Create an Airflow Integration

Navigate to the integrations page and create a new Airflow integration. Change the connection type tab to "Pull" and then click submit. Copy the integration ID from the URL of the page and write it down.

#### Install Secoda Airflow Provider

Install `secoda-airflow` package using pip:

```
pip install secoda-airflow
```

After the installation, navigate to your Airflow connections settings and create a new Secoda connection. Fill in the form with these details

* Connection ID: `secoda_default`
* Connection Type: `Secoda Hook`
* Host: `https://api.secoda.co` (for EU region, please use `https://eapi.secoda.co`)
* Password:  enter your API key from first step&#x20;
* Extra JSON: enter your integration ID in the following format

```
{"integration_id": "id from step 2"}
```

Save the connection and now Secoda provider should be working.

#### Add Secoda callbacks to your DAGs

Here is an example DAG with Secoda callbacks.&#x20;

```
from airflow import DAG
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from airflow.utils.dates import days_ago

from secoda_airflow.callbacks import task_callbacks, dag_callbacks

SNOWFLAKE_CONN_ID = "snowflake"

query = """
CREATE OR REPLACE TABLE raw.test.customers_copy AS
SELECT * FROM raw.test.customers;
"""


default_args = {
    "owner": "airflow",
    "start_date": days_ago(1),
}

with DAG(
    "create_customers_copy_dag",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
    **dag_callbacks,
) as dag:
    run_query = SnowflakeOperator(
        task_id="run_query",
        snowflake_conn_id=SNOWFLAKE_CONN_ID,
        sql=query,
        **task_callbacks,
    )
```

You can also import individual callbacks from the `secoda_airflow.callbacks`

```
dag_success_callback
task_success_callback
dag_failure_callback
task_failure_callback
```

#### Run an extraction Secoda

After your DAGs have run with the new callbacks, please navigate to your Airflow integration on Secoda and run an extraction to process all of the callbacks. To automate this step, you could configure your extractions to run right after your Airflow runs have finished using a cron expression.
