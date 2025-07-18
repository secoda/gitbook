---
description: An overview of the Snowflake integration with Secoda
---

# Snowflake

{% content-ref url="snowflake-metadata/" %}
[snowflake-metadata](snowflake-metadata/)
{% endcontent-ref %}

## **Getting Started with Snowflake** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

There are four steps to connect Snowflake with Secoda.

1. Create Role for Secoda
2. Create User for Secoda
3. Whitelist [Secoda IP Address](./#h_e7eac6e3f5)
4. Connect Snowflake to Secoda in the Secoda UI

You **must** be either an `ACCOUNTADMIN`, or have `MANAGE GRANTS` privileges in order to run the commands necessary to connect.

We recommend naming the User, Role, and Warehouse, `SECODA_USER`, `SECODA_ROLE`, `SECODA_WAREHOUSE` respectively. However, naming them this way is not necessary to integrate.

### **Step 1: Create Role for Secoda** <a href="#h_f22c4a805b" id="h_f22c4a805b"></a>

Navigate to Worksheets, select a database, and run the following commands in that database. You'll need to run these commands for all of the databases that you'd like Secoda to import metadata from.

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

\[Optional] If you are using Snowflake Dynamic Tables, to bring in those tables, you have to grant `MONITOR` permissions to the SECODA role on all of those tables.

```
GRANT MONITOR ON TABLE database.schema.some_dynamic_table TO ROLE SECODA;
```

This step has to be repeated for every single dynamic table that you wish to bring into Secoda.

\[Optional] If you are using Snowflake Snowpies, to bring in those pipes, you have to grant `MONITOR USAGE` permissions to the SECODA role and `MONITOR` permissions on all of those pipes. The stages that the pipes reference must also be granted access privileges.&#x20;

```
GRANT MONITOR USAGE ON ACCOUNT TO ROLE SECODA;
GRANT MONITOR ON PIPE database.schema.some_pipe TO ROLE SECODA;
GRANT USAGE ON ALL STAGES IN DATABASE identifier($database_name) TO ROLE SECODA;
```

\[Optional] If you are using Snowflake Streamlit, to bring in those apps, you have to grant `MONITOR` permissions to the SECODA role on all of those apps.

```
GRANT USAGE ON ALL STREAMLITS IN DATABASE identifier($database_name) TO ROLE SECODA;
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
If you would like to enable the [Push to Snowflake](../../push-metadata-to-source.md) feature, the SECODA\_USER must be the owner of the tables, have INSERT privileges on the table, and MODIFY privileges on the schema and database.
{% endhint %}

#### Key-Pair Authentication

If you would like you use key-pair authentication instead of a password you will need to:

[Configure the key-pair in Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth). Once the key is created, you can run the following command to connect the key to the `SECODA_USER`.

<pre><code><strong>ALTER USER SECODA_USER SET RSA_PUBLIC_KEY='my_public_key';
</strong></code></pre>

### **Step 3: Whitelist Secoda IP Addresses** <a href="#h_7ee8142011" id="h_7ee8142011"></a>

If you create a network policy with Snowflake, add the following [Secoda IP addresses](../../../faq.md#what-are-the-ip-addresses-for-secoda) to the “Allowed IP Addresses” list.

### **Step 4: Connect Snowflake to Secoda** <a href="#h_7ee8142011" id="h_7ee8142011"></a>

1. In the Secoda App, select `Add Integration` on the Integrations page. Search for and select “Snowflake”.
2. Add your credentials as follows:
   * User - The name of the User created in Step 2.
   * Password - The Password set in Step 2.
     * Alternatively you can select the key-pair authentication and enter the private key and passphrase created in step 2.
   * Account - This is the Account ID of your cluster.
   * Warehouse - The Warehouse set in Step 1.

#### **How do I find my Account ID?**

You can find the Account ID in the Snowflake URL. The account ID is usually a substring of the URL, before `snowflakecomputing.com`. **If your Snowflake URL does not contain `snowflakecomputing.com`, see** [**here**](./#account-id-is-not-part-of-url) **to determine your Account ID.**

The account ID will likely be the business name, as well as the cloud region, if Snowflake is cloud hosted. See below for some examples.

1.  URL: `https://secoda.snowflakecomputing.com`

    ACCOUNT ID: `secoda`
2.  URL: `https://secoda.us-east-1.snowflakecomputing.com`

    ACCOUNT ID: `secoda.us-east-1`
3.  URL: `https://secoda.west-europe.azure.snowflakecomputing.com`

    ACCOUNT ID: `secoda.west-europe.azure`

### Troubleshooting

#### Account ID is not part of URL

Snowflake has made some recent changes where URLs can be different than the standard format above. In these cases, you can find the correct account id by:

1. Clicking on the account selector in Snowflake
2. Hovering over the specific account you want to connect to\
   \
   <img src="https://secoda-public-media-assets.s3.amazonaws.com/660640ab-8e40-41a1-be24-6da71bc4b39f.png" alt="" data-size="original">\\
3. Then clicking the copy account URL button on the 3rd section that shows the accounts details (organization id,\
   \
   ![](https://secoda-public-media-assets.s3.amazonaws.com/f461ba8b-ea39-402c-849a-e84b96d73a16.png)

This should create a URL ending with `snowflakecomputing.com`and you can follow the steps abvoe to determine the account id.

#### Account usage not authorized

In order to resolve this error, please run the following command:

`GRANT imported privileges on database SNOWFLAKE to ROLE SECODA;`

#### Could not connect to Snowflake backend after 0 attempt(s)

This error could be the result of an incorrect Account ID. Please double check that your Account ID is properly added.

**No active warehouse selected in the current session**

This error can be due to the warehouse name not being fully uppercase. Updating the warehouse name to all uppercase letters should resolve this issue.
