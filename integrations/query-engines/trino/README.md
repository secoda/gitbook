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

**Create a Trino User**&#x20;

Depending on your setup, this could be LDAP, a file-based system, etc. For the purpose of this guide, we'll assume you're using a file-based system for simplicity.

To create a new user for Secoda, you’ll need to add a new entry in your user management system. Here's an example for a file-based system:

1. Edit the user file (e.g., `etc/password`) to include a new user entry for Secoda.
2. Add a line like `secoda:<password>` in the file, replacing `<password>` with a strong password.
3. Ensure that this user has the necessary permissions to access the data in Trino.

**Connect Trino to Secoda**&#x20;

After creating a Trino user, the next step is to connect Trino to Secoda:

1. In the Secoda App, navigate to the 'Integrations' tab.
2. Click on ‘Add Integration’.
3. Search for and select ‘Trino’.
4. Enter the details for your Trino environment, including the username and password for the user you created.
5. Click 'Connect'.

**Whitelist Secoda IP Address** For Secoda to access your Trino environment, you may need to whitelist its IP address. This process will vary depending on your network setup and where your Trino environment is hosted. Generally, you will need to update your firewall or network security group rules to allow incoming connections from Secoda’s IP address to your Trino cluster.

Remember to follow your organization's security policies and best practices when configuring these settings.
