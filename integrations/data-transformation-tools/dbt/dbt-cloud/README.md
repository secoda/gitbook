---
description: An overview of the dbt Cloud integration with Secoda
---

# dbt Cloud

{% content-ref url="metadata-extracted.md" %}
[metadata-extracted.md](metadata-extracted.md)
{% endcontent-ref %}

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

![](https://secoda-public-media-assets.s3.amazonaws.com/befe8acc-e0ba-4e42-a1b7-217c3e3a62ee.png)

#### **Retrieve a Service Token** <a href="#h_a2cb9baed8" id="h_a2cb9baed8"></a>

Secoda uses the dbt Cloud REST API, which is only available paying dbt Cloud customers. For Secoda to retrieve metadata from dbt, you need to generate a Service Token with. To do this, go to **Account Settings > Service Tokens** and click "New Token".

The minimum permissions are **Analyst** of the selected projects for the Service Account. Once the projects have been selected Save the token and copy the generated token.

![](<../../../../.gitbook/assets/Screenshot 2025-04-01 at 3.24.16 PM.png>)

#### **Connect dbt to Secoda** <a href="#h_d49e98be3a" id="h_d49e98be3a"></a>

After enabling the dbt REST API, the next step is to connect Secoda:

1. In the Secoda App, select **Add Integration** on the Integrations tab
2. Search for and select the **dbt Cloud** integration
3. Enter your dbt account ID and Service Token. This information is kept encrypted.
4. Click **Connect**

## Chrome extension with dbt Cloud

The Chrome extensions pulls in the dbt metadata in the following scenarios:

* From the Develop tab, when opening a particular Model in the Editor
* When looking at Jobs or Runs (if it's been extracted)
* From the Explore tab, when looking at Models
* From the Explore tab, when clicking on Models within Lineage graphs&#x20;
