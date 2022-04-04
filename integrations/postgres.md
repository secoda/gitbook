# Postgres

### **Getting Started** <a href="#h_080d959898" id="h_080d959898"></a>

There are three steps to get started using Postgres with Postgres:

1. Create a database user
2. Connect Postgres to Secoda
3. Whitelist Secoda IP Address

#### **Create a Database User** <a href="#h_b3f5c96bd0" id="h_b3f5c96bd0"></a>

The username and password you’ve already created for your cluster is your admin password, which you should keep for your own usage. For Secoda, and any other 3rd-parties, it is best to create distinct users.

To create a new user, you’ll need to log into the Postgres database directly and run the following SQL commands:

```
-- Create a user named "secoda" that Secoda will use when connecting to your Postgres database. CREATE USER secoda PASSWORD '<enter password here>'; -- Complete this query for any schemas you would like Secoda to extract from GRANT SELECT ON ALL TABLES IN SCHEMA <schema_name> TO secoda;
```

When connecting to Postgres in Secoda, use the username/password you’ve created here instead of your admin account.

#### **Connect Postgres to Secoda** <a href="#h_bd556b4862" id="h_bd556b4862"></a>

After creating a Postgres user, the next step is to connect Secoda:

1. In the Secoda App, select ‘Add Integration’ on the Integrations tab
2. Search for and select ‘Postgres’
3. Enter your Postgres credentials
4. Click 'Connect'

### **Security** <a href="#h_fb194eceed" id="h_fb194eceed"></a>

VPCs keep servers inaccessible to traffic from the internet. With VPC, you’re able to designate specific web servers access to your servers. In this case, you will be whitelisting the Secoda IPs to read from your data warehouse.

Allow Secoda to read into your Postgres database using\
`35.175.75.15/32`
