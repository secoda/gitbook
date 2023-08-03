---
description: This page explains how to integrate Fivetran with Secoda
---

# Fivetran

## Getting Started with Fivetran <a href="#h_21e27f5a15" id="h_21e27f5a15"></a>

&#x20;There are two steps to get started using Fivetran with Secoda:

1. Generate an API Key and an API Secret on Fivetran
2. Connect Fivetran to Secoda with your API Key and API Secret

{% hint style="info" %}
Secoda pulls the following metadata from the Fivetran API: jobs, run times, owners, destinations, and other general metadata around jobs.
{% endhint %}

### Generate an API Key

1. Login to Fivetran and head to the Settings/API Config section.
2. Generate an API Key and API Secret (make sure to copy the key and secret).

> Note: If you already have an API key and secret issued generating a new key will disable and replace the existing key.

### Fivetran API Key Permissions

When generating an API Key in Fivetran, Secoda will need **view** access on:

* Destinations
* Transformations in Destinations
* Connectors
* Users

### Connect to Fivetran

1. In Secoda, head to the **Integrations** page and click **New Integration**
2. Select **Fivetran**
3. Paste the API Key
4. Head to the **History** tab on the side bar and click **Run extraction**
