---
description: An overview of the Hive integration with Secoda
---

# Apache Hive

{% content-ref url="metadata-extracted.md" %}
[metadata-extracted.md](metadata-extracted.md)
{% endcontent-ref %}

## **Getting Started with Apache Hive**

**1. Create Role for Secoda**

To ensure controlled access, we'll begin by creating a dedicated role for Secoda in Hive:

```sql
sqlCopy code-- Create a new role for Secoda
CREATE ROLE SECODA;

-- Grant read permissions on database
GRANT SELECT ON DATABASE <database_name>.* TO ROLE SECODA;
```

**2. Create User for Secoda**

Creating a user in Hive will depend on the underlying authentication and user management system in place (like LDAP, Kerberos, etc.). Typically, a Hive admin would create users outside of Hive. Once they exist, you can grant roles to them within Hive:

```sql
sqlCopy code-- Grant the role to user
GRANT ROLE SECODA TO USER SECODA_USER;
```

**3. Connect Hive to Secoda**

To integrate Secoda with your Hive setup:

* In the Secoda App, select `Add Integration` on the Integrations page.
* Search for and select "Hive".
* Provide the necessary credentials:
  * `User`: The username (as created above).
  * `Password`: The password for the user.
  * `Host`: Hive Server2 host.
  * `Port`: This is usually 10000 but might vary based on your specific setup.

**4. Security: Whitelisting IPs**

The process of whitelisting IPs would be external to Hive. It typically occurs at the level of Hive Server2 or in the underlying infrastructure, such as firewalls or security groups if you're using a cloud platform. Ensure that you add the [Secoda IP address](../../../faq.md#what-are-the-ip-addresses-for-secoda) to the list of allowed IPs.

\


