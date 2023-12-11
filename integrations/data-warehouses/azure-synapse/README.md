---
description: An overview of the Azure Synapse integration with Secoda
---

# Azure Synapse

{% content-ref url="metadata-extracted.md" %}
[metadata-extracted.md](metadata-extracted.md)
{% endcontent-ref %}

## Getting Started with Azure Synapse

1. **Create a Login** To ensure controlled access within Azure Synapse, start by creating a login for Secoda. This has to be done on the `master` database on your dedicated SQL pool. Then assign the `dbmanager` on `master` database to the `SECODA` user.&#x20;

```sql
CREATE LOGIN SECODA WITH PASSWORD 'YourSecurePassword';
CREATE USER SECODA FROM LOGIN SECODA;
EXEC sp_addrolemember 'dbmanager', 'SECODA';
```

2. **Create User for Secoda** Switch to the primary database in your dedicated SQL pool and create a Secoda user there as well. Then assign the `db_owner` role to it.

```sql
CREATE USER SECODA FROM LOGIN SECODA;
EXEC sp_addrolemember 'db_owner', 'SECODA';
```

3. **Connect Azure Synapse to Secoda** To integrate Secoda with your Azure Synapse setup:

* In the Secoda App, go to the Integrations page and select "Add Integration".
* Search for and select "Azure Synapse".
* Provide the necessary credentials:
  * **User**: The username (as created above).
  * **Password**: The password for the user.
  * **Host**: Azure Synapse server host.
  * **Port**: (Specify the default port for Synapse or note that it might vary based on your specific setup.)

4. **Security: Whitelisting IPs** Whitelisting IP addresses in Azure typically involves managing Network Security Group rules or using Azure Firewall. Ensure that you add the[ Secoda IP address](../../../faq.md#what-are-the-ip-addresses-for-secoda) to the list of allowed IPs. To do this, go to the Azure Portal, navigate to the appropriate resource (e.g., Azure Synapse), and manage its network settings to add the IP address to the allow list.
