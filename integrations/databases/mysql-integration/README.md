# MySQL

{% content-ref url="metadata-extracted.md" %}
[metadata-extracted.md](metadata-extracted.md)
{% endcontent-ref %}

## **Getting Started with MySQL** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

There are three steps to get started using MySQL with Secoda:

1. Create a database user
2. Connect MySQL to Secoda
3. Whitelist Secoda IP Address

#### **Create a Database User** <a href="#h_b3f5c96bd0" id="h_b3f5c96bd0"></a>

The username and password you’ve already created for your cluster is your admin password, which you should keep for your own usage. For Secoda, and any other 3rd-parties, it is best to create distinct users.

To create a new user, you’ll need to log into the MySQL database directly and run the following SQL commands:

```
-- Create a user named "secoda" that Secoda will use when connecting to your MySQL database. 
CREATE USER 'secoda'@'localhost' IDENTIFIED BY '<enter password here>'; 

-- Complete this query for any databases you would like Secoda to extract from
GRANT SELECT ON <database_name>.* TO 'secoda'@'localhost';

-- Complete this query for any schemas you would like Secoda to extract from
GRANT SELECT ON <schema_name>.* TO 'secoda'@'localhost';
```

When connecting to MySQL in Secoda, use the username/password you’ve created here instead of your admin account.

#### **Connect MySQL to Secoda** <a href="#h_bd556b4862" id="h_bd556b4862"></a>

After creating a MySQL user, the next step is to connect Secoda:

1. In the Secoda App, select ‘Add Integration’ on the Integrations tab
2. Search for and select "MySQL"
3. Enter your MySQL credentials
4. Click 'Connect'

### **Security** <a href="#h_fb194eceed" id="h_fb194eceed"></a>

VPCs keep servers inaccessible to traffic from the internet. With VPC, you’re able to designate specific web servers access to your servers. In this case, you will be whitelisting the Secoda IPs to read from your data warehouse.

Allow Secoda to read into your MySQL database using\
`35.175.75.15/32`
