---
description: An overview of the Azure Cosmos DB integration with Secoda
---

# Azure Cosmos DB

{% content-ref url="metadata-extracted.md" %}
[metadata-extracted.md](metadata-extracted.md)
{% endcontent-ref %}

### Getting Started with Azure Cosmos DB

To integrate Azure Cosmos DB with Secoda, follow these three steps:

1. Create a Cosmos DB Read-Only Key
2. Whitelist Secoda IP Addresses
3. Connect Azure Cosmos DB to Secoda

#### 1. Create a Cosmos DB Read-Only Key

* Navigate to the Azure portal.
* Go to your Cosmos DB account.
* Under 'Settings', select 'Keys'.
* Create a read-only key.

#### 2. Whitelist Secoda IP Address

* In Azure Cosmos DB, go to 'Networking'.
* Either set public network access to `all networks` or under the `select network` add the [Secoda IP address](../../../faq.md#what-are-the-ip-addresses-for-secoda) to the firewall whitelist.

#### 3. Connect Azure Cosmos DB to Secoda

* Visit [Secoda's Integrations page](https://app.secoda.co/integrations).
* Click "New Integration".
* Search for "Azure Cosmos DB" and select it.
* Enter your Cosmos DB endpoint and the read-only key.
* Click "Test Connection".
* Once successful, click "Submit".
* Choose the data you want to import into Secoda.
* Click "Run Initial Extraction".

### Datatype Conversion
