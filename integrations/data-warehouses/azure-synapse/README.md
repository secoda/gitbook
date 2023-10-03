---
description: An overview of the Azure Synapse integration with Secoda
---

# Azure Synapse

{% content-ref url="metadata-extracted.md" %}
[metadata-extracted.md](metadata-extracted.md)
{% endcontent-ref %}

## Getting Started with Azure Synapse

1. **Create Role for Secoda** To ensure controlled access within Azure Synapse, start by creating a dedicated role for Secoda:

```sql
CREATE ROLE SECODA;
```

2. **Create User for Secoda** In Azure Synapse, the process to create a user might be influenced by the Azure Active Directory and specific configurations in the Azure portal. Once the user is created, you can then grant the Secoda role to this user within Synapse:

```sql
CREATE LOGIN SECODA_USER WITH PASSWORD = 'YourSecurePassword';
GRANT ROLE SECODA TO USER SECODA_USER;
```

3. **Connect Azure Synapse to Secoda** To integrate Secoda with your Azure Synapse setup:

* In the Secoda App, go to the Integrations page and select "Add Integration".
* Search for and select "Azure Synapse".
* Provide the necessary credentials:
  * **User**: The username (as created above).
  * **Password**: The password for the user.
  * **Host**: Azure Synapse server host.
  * **Port**: (Specify the default port for Synapse or note that it might vary based on your specific setup.)

4. **Security: Whitelisting IPs** Whitelisting IP addresses in Azure typically involves managing Network Security Group rules or using Azure Firewall. Ensure that you add the IP address `35.175.75.15/32` to the list of allowed IPs. To do this, go to the Azure Portal, navigate to the appropriate resource (e.g., Azure Synapse), and manage its network settings to add the aforementioned IP address to the allow list.
