---
description: An overview of the Databricks integration with Secoda
---

# Databricks

{% content-ref url="metadata-extracted.md" %}
[metadata-extracted.md](metadata-extracted.md)
{% endcontent-ref %}

## **Getting Started with Databricks** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

There are three steps to get started using Databricks with Secoda:

1. Create an access token
2. Connect Databricks to Secoda
3. Whitelist Secoda IP Address

**Note:** You can run Databricks on Secoda using AWS or GCP.

### Create an access token

In your Databricks console go to the **User Settings** and generate a new access token. Save the value to be used to connect Databricks to Secoda in the second step.

![](https://secoda-public-media-assets.s3.amazonaws.com/image%20\(12\)%20\(1\).png)

### Connect Databricks to Secoda

Go to [https://app.secoda.co/integrations/new](https://app.secoda.co/integrations/new) and select the Databricks integration.

Enter in the following credentials:

* **Host:** This is the URL of your Databricks workspace, i.e, [dbc-dc31b5a2-597d.cloud.databricks.com](https://dbc-dc31b5a2-597d.cloud.databricks.com/)
* **Databricks Workspace Id:** The numerical id of your workspace, located in the url of your Databricks instance, after the "/?o=". `https://<instance_id>.cloud.databricks.com/?o=<workspace_id>`.\\

![](https://secoda-public-media-assets.s3.amazonaws.com/Screen%20Shot%202022-08-31%20at%2011.32.53%20AM.png)

* **Access Token:** The access token you generated in the first step
* **\[Optional] Warehouse ID (Recommended) or Cluster ID:** This is the resource what SQL queries will run on. For the optimal experience, use a [Databricks serverless SQL warehouse](https://docs.databricks.com/en/admin/sql/serverless.html).

After entering in the information into Secoda, click "Test Connection". After the connection is successful your can Submit and run the initial extraction.

### Whitelist Secoda IP Address

If your Databricks instance is behind a firewall, you'll have to whitelist [Secoda's IP address](../../../faq.md#what-are-the-ip-addresses-for-secoda) to allow for metadata extractions.&#x20;
