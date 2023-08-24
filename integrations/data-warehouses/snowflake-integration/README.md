---
description: An overview for the Snowflake integration with Secoda
---

# Snowflake

{% content-ref url="snowflake-metadata/" %}
[snowflake-metadata](snowflake-metadata/)
{% endcontent-ref %}

## **Getting Started with Snowflake** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

There are four steps to connect Snowflake with Secoda. Make sure that you are running the commands in each step while logged in as an `ACCOUNTADMIN`, or an account that has `MANAGE GRANTS`. While we are using predefined user (`SECODA_USER`), role (`SECODA`), and warehouse (`SECODA_WAREHOUSE`)

1. Create Role for Secoda
2. Create User for Secoda
3. Connect Snowflake to Secoda
4. Whitelist IP Address

#### **Create Role for Secoda** <a href="#h_f22c4a805b" id="h_f22c4a805b"></a>

You need to run these commands rather than creating a role with the “Create Role” dialogue in the UI.

This role will be attached to Secoda’s user and it gives just enough permissions for reading metadata in your database. We recommend not reusing this role for other operations.

1. Click on to Worksheets;
2. Select a database under database objects
3. Change role to ACCOUNTADMIN
4. Create a new `SECODA` role and provide access to the `SNOWFLAKE` system tables using the following commands:

```
CREATE ROLE SECODA;
GRANT imported privileges on database SNOWFLAKE to ROLE SECODA;
GRANT USAGE ON WAREHOUSE "<warehouse>" TO ROLE SECODA;
```

1. Grant access to any existing and future databases, schemas and tables **for all the databases** you'd like Secoda to import metadata from:

```
// ====== Existing Tables & Schemas

// Usage on database object
GRANT USAGE ON DATABASE <database name> TO ROLE SECODA;

// Usage on existing schemas
GRANT USAGE,MONITOR ON ALL SCHEMAS IN DATABASE <database name> TO ROLE SECODA;

// References for INFORMATION_SCHEMA to existing tables
GRANT SELECT ON ALL TABLES IN DATABASE <database name> TO ROLE SECODA;
GRANT SELECT ON ALL VIEWS IN DATABASE <database name> TO ROLE SECODA;

// ====== Future Tables & Schemas

// Read access to all schemas created in the future (but not current ones)
GRANT USAGE,MONITOR ON FUTURE SCHEMAS IN DATABASE <database name> TO ROLE SECODA;

// Reference for INFORMATION_SCHEMA to all tables created in the future (but not current ones)
GRANT SELECT ON FUTURE TABLES IN DATABASE <database name> TO ROLE SECODA;
```

Create User for Secoda

Finally, you need to create the user that will be connected to Secoda. Be sure to use a strong, unique password.

```
CREATE USER SECODA_USER
  MUST_CHANGE_PASSWORD = FALSE
  DEFAULT_ROLE = SECODA
  PASSWORD = "my_strong_password"; *-- Do not use this password *

GRANT ROLE SECODA TO USER SECODA_USER;

// This sets the default role, required for metadata extractions
ALTER USER SECODA_USER SET DEFAULT_ROLE=SECODA
```

#### **Connect Snowflake to Secoda** <a href="#h_7ee8142011" id="h_7ee8142011"></a>

After creating a Snowflake warehouse, the next step is to connect Secoda.

1. In the Secoda App, select `Add Integration` on the Integrations page.
2. Search for and select “Snowflake”.
3. Add your credentials as follows: User - The user name (as created above). Password - The password for the user. Account - The account id of your cluster, not the URL (e.g. URL: `my-business.snowflakecomputing.com`, account-id: `my-business`. **Note:** If you are using Snowflake on AWS, the account id includes the region, for example, your URL might look like this: `my-business.us-east-1.snowflakecomputing.com/` and your account-id would be: `my-business.us-east-1`) Warehouse - The warehouse name.

### **Security** <a href="#h_58079a5dc2" id="h_58079a5dc2"></a>

#### **Whitelisting IPs** <a href="#h_e7eac6e3f5" id="h_e7eac6e3f5"></a>

If you create a network policy with Snowflake, add the following IP address to the “Allowed IP Addresses” list: `35.175.75.15/32`

### Troubleshooting

#### Account usage not authorized

In order to resolve this error, please run the following command:

`GRANT imported privileges on database SNOWFLAKE to ROLE SECODA;`

#### Could not connect to Snowflake backend after 0 attempt(s)

This error could be the result of an incorrect Account name. For Secoda, the Snowflake Account name is the Account ID of the cluster, which maps to a substring of the Snowflake URL.

For example, if the url is https://oya5096.us-east-1.snowflakecomputing.com, the account name would be `oya5096.us-east-1`. If the url is https://abc1234.west-europe.azure.snowflakecomputing.com then, the account name would be `abc1234.west-europe.azure`. Please ensure the **entire** [Account Locator](https://docs.snowflake.com/en/user-guide/admin-account-identifier#label-account-locator) is included.
