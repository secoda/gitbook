# Databricks Integration

## **Getting Started with Databricks** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

There are three steps to get started using Databricks with Secoda:

1. Create an access token
2. Connect Databricks to Secoda
3. Whitelist Secoda IP Address

### Create an access token

In your Databricks console go to the **User Settings** and generate a new access token. Save the value to be used to connect Databricks to Secoda in the second step.

![](<../.gitbook/assets/image (12) (1).png>)

### Connect Databricks to Secoda

Go to [https://app.secoda.co/integrations/new](https://app.secoda.co/integrations/new) and select the Databricks integration.

Enter in the following credentials:

* **Host:** This is the URL of your Databricks workspace, i.e, [dbc-dc31b5a2-597d.cloud.databricks.com](https://dbc-dc31b5a2-597d.cloud.databricks.com/)
* **Databricks Workspace Id:** The numerical id of your workspace, located in the url of your Databricks instance, after the "/?o=". `https://<instance_id>.cloud.databricks.com/?o=<workspace_id>`.\\

![](<../.gitbook/assets/Screen Shot 2022-08-31 at 11.32.53 AM (1).png>)

* **Access Token:** The access token you generated in the first step

After entering in the information into Secoda, click "Test Connection". After the connection is successful your can Submit and run the initial extraction.

### Whitelist Secoda IP Address

If your Databricks instance is behind a firewall, you'll have to whitelist Secoda's IP address to allow for metadata extractions. The IP addresses you need to whitelist are `35.175.75.15` and `3.122.13.89`
