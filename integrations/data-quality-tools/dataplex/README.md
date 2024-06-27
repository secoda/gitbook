---
description: An overview of Dataplex integration with Secoda
---

# Dataplex

{% content-ref url="dataplex-metadata-extracted.md" %}
[dataplex-metadata-extracted.md](dataplex-metadata-extracted.md)
{% endcontent-ref %}

## Getting started with Dataplex

There are two steps to get started using Dataplex with Secoda

1. Create a GCP Service Account JSON key
2. Connect  Dataplex to Secoda

#### Create a GCP Service Account JSON key

* Login to [GCP console](https://console.cloud.google.com/) and go to the [Service Accounts page](https://console.cloud.google.com/iam-admin/serviceaccounts).&#x20;
* Click + **Create Service Account**
* Enter a name click **Create and Continue**
* In the **Grant this service account access to project** section add the `Data Catalog Viewer` role and `Dataplex Metadata Reader` role
* Click **Done**
* Search for the Service Account that was just created, click the three dots action menu and select **Manage keys**
* Click **Add key > Create new key**
* Select **JSON** and click **Create**
* Save the JSON key to be used later

#### Connect Dataplex to Secoda

After retrieving the Service Account JSON key, the next step is to connect it to Secoda:

1. In the Secoda App, select Add Integration on the Integrations tab
2. Search for and select Dataplex
3. Enter your Dataplex Service Account JSON key retreived above
4. Once successfully connected, a prompt will ask you to run the initial extraction

**Once Connected to Secoda**&#x20;

After the sync has completed successfully, resources that are decorated with additional metadata (e.g. tag templates) and fields will have the Dataplex icon. The fields will show up as custom properties in the resource sidebar.&#x20;

<figure><img src="../../../.gitbook/assets/Screenshot 2024-05-10 at 2.54.25 PM (2).png" alt=""><figcaption><p>Resource with Dataplex metadata</p></figcaption></figure>

