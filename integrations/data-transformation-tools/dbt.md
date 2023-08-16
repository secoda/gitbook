---
description: This page walks through the Secoda and dbt integration that Secoda supports
---

# dbt Cloud

## **Getting Started with dbt** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

{% hint style="info" %}
dbt is a secondary integration that adds additional metadata on to your data warehouse or relational database tables. Before connecting dbt make sure to connect a data warehouse or relational database first. These include Snowflake, BigQuery, Postgres, Redshift, etc.
{% endhint %}

There are three steps to get started using dbt with Secoda:

1. Retrieve your Account ID
2. Retrieve a Service Token
3. Connect dbt to Secoda

#### **Retrieve your Account ID** <a href="#h_89d08409d1" id="h_89d08409d1"></a>

You can determine your account ID by going to the Account Settings page of dbt Cloud console. In the URL, for example in the URL below, the account ID is `12345 https://cloud.getdbt.com/settings/accounts/12345/pages/projects`

<figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

#### **Retrieve a Service Token** <a href="#h_a2cb9baed8" id="h_a2cb9baed8"></a>

Secoda uses the dbt Cloud REST API, which is only available paying dbt Cloud customers. For Secoda to retrieve metadata from dbt, you need to generate a Service Token with. To do this, go to **Account Settings > Service Tokens** and click "New Token".&#x20;

The minimum permissions are **Member** of the selected projects for the Service Account. Once the projects have been selected Save the token and copy the generated token.

<figure><img src="../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

#### **Connect dbt to Secoda** <a href="#h_d49e98be3a" id="h_d49e98be3a"></a>

After enabling the dbt REST API, the next step is to connect Secoda:

1. In the Secoda App, select **Add Integration** on the Integrations tab
2. Search for and select the **dbt Cloud** integration
3. Enter your dbt account ID and Service Token. This information is kept encrypted.
4. Click **Connect**
