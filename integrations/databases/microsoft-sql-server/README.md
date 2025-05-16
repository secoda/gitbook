---
description: An overview of the Microsoft SQL Server integration with Secoda
---

# Microsoft SQL Server

{% content-ref url="metadata-extracted.md" %}
[metadata-extracted.md](metadata-extracted.md)
{% endcontent-ref %}

## **Getting Started with Microsoft SQL Server** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

There are three steps to get started using Microsoft SQL Server with Secoda:

1. Create a database user
2. Connect Microsoft SQL Server to Secoda
3. Whitelist Secoda IP Address

### **Create a Database User** <a href="#h_4dd83bd377" id="h_4dd83bd377"></a>

The username and password you’ve already created for your cluster is your admin password, which you should keep for your own usage. For Secoda, and any other 3rd-parties, it is best to create distinct users.

To create a new user, you’ll need to log into the Microsoft SQL Server database directly and run the following SQL commands:

```
-- Create a user named "secoda" that Secoda will use when connecting to your Microsoft SQL Server database. 
CREATE USER secoda PASSWORD  = '<enter password here>'; 

-- Complete this query for any databases you would like Secoda to extract from 
GRANT SELECT ON DATABASE <yourdbname> TO secoda;
```

When connecting to Microsoft SQL Server in Secoda, use the username/password you’ve created here instead of your admin account.

### **Connect Microsoft SQL Server to Secoda** <a href="#h_dc83b40ac9" id="h_dc83b40ac9"></a>

After creating a Microsoft SQL Server user, the next step is to connect Secoda:

1. In the Secoda App, select ‘Add Integration’ on the Integrations tab
2. Search for and select ‘Microsoft SQL Server’
3. Enter your Microsoft SQL Server credentials
4. Click 'Connect'

{% hint style="info" %}
You can now connect to the entire server and integrate all databases within it through a single integration. This enhancement simplifies management by allowing a single point of integration for multiple databases, which previously required separate integrations for each database.
{% endhint %}

### **Security** <a href="#h_c60cf20ba6" id="h_c60cf20ba6"></a>

VPCs keep servers inaccessible to traffic from the internet. With VPC, you’re able to designate specific web servers access to your servers. In this case, you will be whitelisting the Secoda IPs to read from your data warehouse.

Allow Secoda to read into your Microsoft SQL Server database using the [Secoda IP address](../../../faq.md#what-are-the-ip-addresses-for-secoda)

## Troubleshooting

If you are having errors connecting your Microsoft SQL, it might be because your Host IP Address is private. In this case, you'll need to set up an SSH Tunnel so that Secoda can access the Host. Instructions for setting up an SSH Tunnel can be found [here](https://docs.secoda.co/integrations/security/connecting-via-ssh-tunnel).

Once a tunnel has been created, make sure to choose the SSH Tunnel in the drop down list when inputting your credentials for the integration.
