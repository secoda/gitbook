---
description: An overview of the Airflow integration with Secoda
---

# Airflow

{% content-ref url="metadata-extracted.md" %}
[metadata-extracted.md](metadata-extracted.md)
{% endcontent-ref %}



### **Getting Started with Airflow** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

There are three ways to connect Airflow to Secoda:

1. **API** method: Secoda uses the Airflow Rest API to pull the metadata from your Airflow instance
2. **Astronomer** method: Secoda uses the Astronomer REST API to pull the metadata from your Astronomer instance.
3. **Plugin** method: using Secoda's Airflow plugin, you can add callbacks to certain DAGs and tasks so DAG metadata and lineage gets pushed to Secoda.

### 1. API

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

1. In the Secoda App, select ‘Connect Integration’ on the Integrations tab
2. Search for and select ‘Airflow’
3. Enter your Airflow user and password. This information is kept encrypted.
4. Click 'Connect'

#### Security <a href="#h_4e3c0bcf41" id="h_4e3c0bcf41"></a>

VPCs keep servers inaccessible to traffic from the internet. With VPC, you’re able to designate specific web servers access to your servers. In this case, you will be whitelisting the Secoda IPs to read from your Airflow instance.

Allow Secoda to access your Airflow API from the [Secoda IP Address](../../../faq.md#what-are-the-ip-addresses-for-secoda).

### 2. Astronomer

There are three steps to getting started with Astronomer

1. Retrieve your access token
2. Retrieve the deployment URL
3. Connect Astronomer to Secoda

**Retrieve your access token**

Follow the steps in [Create a Workspace API token](https://www.astronomer.io/docs/astro/workspace-api-tokens#create-a-workspace-api-token) to create your token. Make sure to save the token on creation in order to use it later in this setup.

**Retrieve your deployment URL**

Your Deployment URL is the [host](https://swagger.io/docs/specification/2-0/api-host-and-base-path/) you use to call the Airflow API.

Run the following command to retrieve the URL for your Deployment Airflow UI:

```
astro deployment inspect -n <deployment_name> metadata.airflow_api_url
```

Alternatively, you can retrieve your Deployment URL by opening the Airflow UI for your Deployment on Astro and copying the URL of the page up to `/home`. For example, if the home page of your Deployment Airflow UI is hosted at `clq52c95r000208i8c7wahwxt.astronomer.run/dz3uu847/home`, your Deployment URL is `clq52c95r000208i8c7wahwxt.astronomer.run/dz3uu847`.

**Connect Astronomer to Secoda**

After retrieving the access token and deployment URL, the next step is to connect Secoda:

1. In the Secoda App, select ‘Connect Integration’ on the Integrations tab
2. Search for and select ‘Airflow’
3. Select the "Astronomer" option
4. Enter your Astronomer deployment URL and access token. This information is kept encrypted.
5. Click 'Connect'

### 3. Plugin

This method will push metadata from your Airflow instance to Secoda. Then on an extraction, Secoda will process all the pushed metadata instead of directly pulling from the API.

**Create an API Key**

Navigate to your workspace settings on Secoda. Click on the “API” to get a list of your API Keys.

Click on “Generate New API Key” button and then write down the generated key. Please keep this key somewhere safe and do not share with others. This key will have the same access to your Secoda workspace as the user who created it.

#### Create an Airflow Integration

Navigate to the integrations page and create a new Airflow integration. Change the connection type tab to "Push" and then click Submit. Copy the integration ID from the URL of the page and write it down.

#### Install Secoda Airflow Provider

Install `secoda-airflow` package using pip:

```
pip install secoda-airflow
```

After the installation, navigate to your Airflow connections settings and create a new Secoda connection. Fill in the form with these details

* Connection ID: `secoda_default`
* Connection Type: `Secoda Hook`
* Host: `{Your Secoda Domain}/api/v1/`
  * The Secoda Domain is the domain you access Secoda with
* Password:  enter your API key from first step&#x20;
* Extra JSON: enter your integration ID in the following format

```
{"integration_id": "id from step 2"}
```

Save the connection. The Secoda provider is set up!

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

#### Run an extraction in Secoda

After your DAGs have run with the new callbacks, please navigate to your Airflow integration in Secoda and run an extraction to process all of the callbacks.&#x20;

To automate this step, please set your integration schedule to run extractions right after your Airflow runs have finished.

Alternatively, consider adding a run integration API request to the end of your DAG. That way the extraction will run as part of the DAG process. See below for a sample request.&#x20;

Endpoint: `{Your Secoda Domain}/api/v1/databuilder/jobs/`

Method: `POST`

Payload:

```
{
    "integration_id": "Your Airflow Integration ID",
    "type": "metadata
}
```
