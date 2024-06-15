---
description: An overview of Confluent Cloud integration with Secoda
---

# Confluent Cloud

{% content-ref url="confluent-cloud-metadata-extracted.md" %}
[confluent-cloud-metadata-extracted.md](confluent-cloud-metadata-extracted.md)
{% endcontent-ref %}

## Getting started with Confluent Cloud

To integrate Confluent Cloud with Secoda, we need the following

1. Generate API Key and API Secret for Secoda to connect to Confluent Cloud and extract metadata
2. Schema Registry to extract schema metadata for Topics. This is an optional step.
3. Make a note of the bootstrap server, cluster and environment IDs&#x20;
4. Connect Confluent Cloud to Secoda using the API key, API secret, cluster and environment IDs and optionally connect the Schema Registry&#x20;

### Generate an API Key

1. Login to Confluent Cloud
2. Click on the cluster that needs to be connected to Secoda and click on the **API Keys** section under **Cluster Overview** on the left
3. Click on **Add Key** button to generate a new API key and secret. API key will be the username and API secret will be the password for connecting to Secoda

### Schema Registry

{% hint style="info" %}
This is an optional step. If provided, Secoda can extract metadata for the topic schemas.
{% endhint %}

1. Login to Confluent Cloud
2. Select the environment from **Environments** on the left. This should be the environment that contains the cluster for which API key and secret has been generated [here](./#generate-an-api-key)
3. On the right side, find the section **Stream Governance API** and copy the content under **Endpoint**. This is the Schema Registry URL.
4. Generate Schema Registry API key and make a note of both the API Key and secret. API Key will be the username for Schema Registry and API secret will be the password.

### Bootstrap Server, Cluster and Environment IDs

1. Login to Confluent Cloud
2. Select the environment from **Environments** on the left. This should be the environment that contains the cluster for which API key and secret has been generated [here](./#generate-an-api-key)
3. Environment ID can be found on the right side. Make a note of it.
4. Select the cluster and click on **Cluster Settings** under **Cluster Overview** on the left
5. Make a note of the **Cluster ID** in the section **Identification** and **Bootstrap server** in **Endpoints**

### Connect Confluent Cloud to Secoda

1. In Secoda, head to the **Integrations** page and click **New Integration**
2. Find **Confluent Cloud** under **Data Pipeline**
3. Fill in the connection form with all the necessary details
4. Click **Test Connection** to make sure everything is correct
5. Head to the **Sync History** tab on the side bar and click **Run sync**
