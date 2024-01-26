---
description: An overview of the Snowflake integration with Secoda
---

# Snowflake

{% content-ref url="snowflake-metadata/" %}
[snowflake-metadata](snowflake-metadata/)
{% endcontent-ref %}

## **Getting Started with Snowflake** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

There are four steps to connect Snowflake with Secoda.&#x20;

1. Create Role for Secoda
2. Create User for Secoda
3. Whitelist [Secoda IP Address](./#h\_e7eac6e3f5)
4. Connect Snowflake to Secoda in the Secoda UI

You **must** be either an `ACCOUNTADMIN`, or have `MANAGE GRANTS` privileges in order to run the commands necessary to connect.&#x20;

We recommend naming the User, Role, and Warehouse, `SECODA_USER`, `SECODA_ROLE`, `SECODA_WAREHOUSE` respectively. However, naming them this way is not necessary to integrate.

### **Step 1: Create Role for Secoda** <a href="#h_f22c4a805b" id="h_f22c4a805b"></a>

Navigate to Worksheets, select a database, and run the following commands in that database. You'll need to run these commands for all of the databases that you'd like Secoda to import metadata from.&#x20;

```
CREATE ROLE SECODA;
GRANT imported privileges on database SNOWFLAKE to ROLE SECODA;
GRANT USAGE ON WAREHOUSE "<warehouse>" TO ROLE SECODA;

// ====== Existing Tables & Schemas
begin;

set database_name = <database name>;
// Usage on database object
GRANT USAGE ON DATABASE identifier($database_name) TO ROLE SECODA;

// Usage on existing schemas
GRANT USAGE,MONITOR ON ALL SCHEMAS IN DATABASE identifier($database_name)  TO ROLE SECODA;

// References for INFORMATION_SCHEMA to existing tables
GRANT SELECT ON ALL TABLES IN DATABASE identifier($database_name)  TO ROLE SECODA;
GRANT SELECT ON ALL VIEWS IN DATABASE identifier($database_name)  TO ROLE SECODA;

// ====== Future Tables & Schemas

// Read access to all schemas created in the future (but not current ones)
GRANT USAGE,MONITOR ON FUTURE SCHEMAS IN DATABASE identifier($database_name)  TO ROLE SECODA;

// Reference for INFORMATION_SCHEMA to all tables created in the future (but not current ones)
GRANT SELECT ON FUTURE TABLES IN DATABASE identifier($database_name)  TO ROLE SECODA;

commit;
```

### Step 2: Create User for Secoda

```
CREATE USER SECODA_USER
  MUST_CHANGE_PASSWORD = FALSE
  DEFAULT_ROLE = SECODA
  PASSWORD = "my_strong_password"; *-- Do not use this password *

GRANT ROLE SECODA TO USER SECODA_USER;

// This sets the default role, required for metadata extractions
ALTER USER SECODA_USER SET DEFAULT_ROLE=SECODA
```

{% hint style="info" %}
If you would like to enable the [Push to Snowflake](../../../features/push-metadata-to-source.md) feature, the SECODA\_USER must be the owner of the tables, have INSERT privileges on the table, and MODIFY privileges on the schema and database.&#x20;
{% endhint %}

### **Step 3: Whitelist Secoda IP Addresses** <a href="#h_7ee8142011" id="h_7ee8142011"></a>

If you create a network policy with Snowflake, add the following [Secoda IP addresses](../../../faq.md#what-are-the-ip-addresses-for-secoda) to the “Allowed IP Addresses” list.

### **Step 4: Connect Snowflake to Secoda** <a href="#h_7ee8142011" id="h_7ee8142011"></a>

1. In the Secoda App, select `Add Integration` on the Integrations page. Search for and select “Snowflake”.
2. Add your credentials as follows:&#x20;
   * User - The name of the User created in Step 2.
   * Password - The Password set in Step 2.
   * Account - This is the Account ID of your cluster.&#x20;
   * Warehouse - The Warehouse set in Step 1.&#x20;

#### **How do I find my Account ID?**

You can find the Account ID in the Snowflake URL. The account ID is usually a substring of the URL, before `snowflakecomputing.com`.  The account ID will likely be the business name, as well as the cloud region, if Snowflake is cloud hosted. See below for some examples.&#x20;

1.  URL: `https://secoda.snowflakecomputing.com`

    ACCOUNT ID: `secoda`
2.  URL: `https://secoda.us-east-1.snowflakecomputing.com`

    ACCOUNT ID: `secoda.us-east-1`
3.  URL: `https://secoda.west-europe.azure.snowflakecomputing.com`

    ACCOUNT ID: `secoda.west-europe.azure`&#x20;

### Troubleshooting

#### Account usage not authorized

In order to resolve this error, please run the following command:

`GRANT imported privileges on database SNOWFLAKE to ROLE SECODA;`

#### Could not connect to Snowflake backend after 0 attempt(s)

This error could be the result of an incorrect Account ID. Please double check that your Account ID is properly added.&#x20;
