---
description: This page walks through the Secoda and Oracle integration that Secoda supports
---

# Oracle Integration

## **Getting Started with Oracle** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

There are three steps to get started using Oracle with Secoda:

1. Create a database user
2. Whitelist Secoda IP Address
3. Connect Oracle to Secoda

#### **Create a Database User** <a href="#h_4dd83bd377" id="h_4dd83bd377"></a>

The username and password you’ve already created for your database is your admin password, which you should keep for your own usage. For Secoda, and any other 3rd-parties, it is best to create distinct users.

To create a new user, you’ll need to log into the Oracle database directly and run the following SQL commands:

```
-- Create a secoda user
CREATE USER secoda IDENTIFIED BY '<password>';

-- Provide SELECT access to secoda users
BEGIN
   FOR table IN (SELECT owner, table_name FROM all_tables WHERE owner='<schema>') LOOP
      EXECUTE IMMEDIATE 'grant select on '||table.owner||'.'||table.table_name||' to secoda';
   END LOOP;
END; 
```

#### **Whitelist Secoda IP Address** <a href="#h_dc83b40ac9" id="h_dc83b40ac9"></a>

VPCs keep servers inaccessible to traffic from the internet. With VPC, you’re able to designate specific web servers access to your servers. In this case, you will be whitelisting the Secoda IPs to read from your data warehouse.

Allow Secoda to read into your Oracle database from `35.175.75.15/32` and `34.230.160.245/32`

****

#### **Connect Oracle to Secoda** <a href="#h_dc83b40ac9" id="h_dc83b40ac9"></a>

After creating a Oracle user, the next step is to connect Secoda:

1. In the Secoda App, select "New Integration" from [https://app.secoda.co/integrations](https://app.secoda.co/integrations)
2. Search for and select "Oracle"
3. Enter your Oracle credentials
4. Click "Test Connection"
5. Click "Submit"
6. Select the schemas you'd like to import and click "Submit"
7. Click "Run Initial Extraction"
