---
description: An overview of the Trino integration with Secoda
---

# Trino

{% content-ref url="trino-metadata-extracted.md" %}
[trino-metadata-extracted.md](trino-metadata-extracted.md)
{% endcontent-ref %}

## Get Started With Trino

There are three steps to connect Trino with Secoda:

1. Create a Trino User
2. Connect Trino to Secoda
3. Whitelist Secoda IP Address

#### **Create a Trino User**

Depending on your setup, this could be through LDAP, a file-based system, etc. For the purpose of this guide, we'll assume you're using a file-based system for simplicity, but we will also provide instructions for setting up JWT authentication.

* **For File-based Authentication:**
  * Edit the user file (e.g., etc/password) to include a new user entry for Secoda.
  * Add a line like `secoda:<password>` in the file, replacing `<password>` with a strong password.
  * Ensure that this user has the necessary permissions to access the data in Trino.
* **For JWT Authentication:**
  * You will need to configure Trino to accept JWT for authentication. This involves setting up a JWT provider and configuring Trino to validate JWT tokens against your provider.
  * Generate a JWT token that includes a claim identifying the user as Secoda. The exact claim required will depend on your Trino configuration.
  * Ensure that the JWT token grants the necessary permissions for Secoda to access the data in Trino.

#### **(Optional) Query History Config**

If you store the query history from Trino in a table, you can specify the location of this query history table and the relevant columns. Copy the following JSON and replace the values with your configuration. Use this in the  **Query History Config** field on your Trino integration.

```json
{
  "query_table": "prod.analytics.query_history",
  "start_time_column": "start_time", 
  "end_time_column": "end_time",
  "query_column": "query_text",
  "user_column": "user"
}
```

{% hint style="info" %}
The `query_table` must be the full path, i.e, database.schema.table.

The `user_column` in your `query_table` should contain emails as the value. This is not a requirement.&#x20;
{% endhint %}

#### **Connect Trino to Secoda**&#x20;

After creating a Trino user, the next step is to connect Trino to Secoda:

1. In the Secoda App, navigate to the 'Integrations' tab.
2. Click on ‘Add Integration’.
3. Search for and select ‘Trino’.
4. Enter the details for your Trino environment, including the username and password or JWT token for the user you created.
5. Click 'Connect'.

#### **Whitelist Secoda IP Address**&#x20;

For Secoda to access your Trino environment, you may need to whitelist its IP address. This process will vary depending on your network setup and where your Trino environment is hosted. Generally, you will need to update your firewall or network security group rules to allow incoming connections from Secoda’s IP address to your Trino cluster.

Remember to follow your organization's security policies and best practices when configuring these settings.
