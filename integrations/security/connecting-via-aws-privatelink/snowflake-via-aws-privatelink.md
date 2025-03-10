# Snowflake via AWS PrivateLink

{% hint style="info" %}
This documentation applies to Secoda single-tenant and multi-tenant customers. For self-hosted customers refer to the Snowflake documentation [https://docs.snowflake.com/en/user-guide/admin-security-privatelink](https://docs.snowflake.com/en/user-guide/admin-security-privatelink).
{% endhint %}

**Steps to enable Secoda’s access to your Snowflake instance via AWS PrivateLink**

1\. Submit a support ticket to Snowflake requesting third-party access for Secoda. You will need to include Secoda’s AWS account ID, which will be provided by your account manager.

2\. Execute the following query in your Snowflake instance: `SELECT system$get_privatelink_config();`. Share the output of this query with the Secoda team.

3\. The Secoda team will use the provided information to set up a VPC endpoint, enabling connection to your Snowflake instance.

4\. Once Secoda confirms the connection, you will be able to access Snowflake through Secoda using a PrivateLink account identifier, formatted like this: \<account id>.\<region>.privatelink.

5\. Important: If you have network policies in Snowflake restricting access, you will need to add Secoda’s private IP range to the allowed list.
