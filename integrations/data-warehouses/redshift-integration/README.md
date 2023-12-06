---
description: An overview of the Redshift integration with Secoda
---

# Redshift

{% content-ref url="redshift-metadata.md" %}
[redshift-metadata.md](redshift-metadata.md)
{% endcontent-ref %}

## Getting Started with Redshift

There are three steps to connect Redshift with Secoda:

1. Create a database user
2. Connect Redshift to Secoda
3. Whitelist Secoda IP Address

#### **Create a Database User** <a href="#h_b3c3711b1d" id="h_b3c3711b1d"></a>

The username and password you’ve already created for your cluster is your admin password, which you should keep for your own usage. For Secoda, and any other 3rd-parties, it is best to create distinct users. This will allow you to isolate queries from one another using [WLM](http://docs.aws.amazon.com/redshift/latest/dg/c\_workload\_mngmt\_classification.html) and perform audits easier.

To create a [new user](http://docs.aws.amazon.com/redshift/latest/dg/r\_Users.html), you’ll need to log into the Redshift database directly and run the following SQL commands:

Redshift doesn't allow for non-super users to access the system tables, which is where we pull the metadata from. Below is a workaround so you aren't giving Secoda superuser access. Secoda only uses the system tables for our metadata extraction, the extraction query can be viewed [here](https://www.notion.so/Redshift-4a22df9ed18b4a6cb35eefd418f65727).

```
-- Create a user named "secoda" that Secoda will use when connecting to your Redshift cluster.
CREATE USER secoda PASSWORD '<enter password here>';

-- Allows the non super user "secoda" to query metadata
-- Explaination of query here -> https://stackoverflow.com/questions/48567440/granting-permissions-on-redshift-system-tables-to-non-superusers
ALTER USER secoda SYSLOG ACCESS UNRESTRICTED;

-- Complete this query for any schemas you would like Secoda to extract
GRANT SELECT ON ALL TABLES IN SCHEMA <schema_name> TO secoda

GRANT SELECT ON svv_table_info TO secoda;
```

When connecting to Redshift in Secoda, use the username/password you’ve created here instead of your admin account.

#### **Connect Redshift to Secoda** <a href="#h_53d550377e" id="h_53d550377e"></a>

After creating a Redshift warehouse, the next step is to connect Secoda:

1. In the Secoda App, select ‘Add Integration’ on the Integrations tab
2. Search for and select ‘Redshift’
3. Enter your Redshift credentials
4. Click 'Connect'

### **Security** <a href="#h_317efbf748" id="h_317efbf748"></a>

VPCs keep servers inaccessible to traffic from the internet. With VPC, you’re able to designate specific web servers access to your servers. In this case, you will be whitelisting the [Secoda IPs](../../../faq.md#what-are-the-ip-addresses-for-secoda) to read from your data warehouse.

### **Best Practice** <a href="#h_61b5b414fd" id="h_61b5b414fd"></a>

#### **Networking** <a href="#h_88c5c0ac60" id="h_88c5c0ac60"></a>

Redshift clusters can either be in a **EC2 Classic subnet** or **VPC subnet**.

If your cluster has a field called `Cluster Security Groups`, proceed to [EC2 Classic](https://docs/connections/storage/catalog/redshift/#ec2-classic)

Or if your cluster has a field called `VPC Security Groups`, proceed to [EC2 VPC](https://segment.com/docs/connections/storage/catalog/redshift/#ec2-vpc)

#### **EC2-Classic** <a href="#h_3664c35de1" id="h_3664c35de1"></a>

1. Navigate to your Redshift Cluster settings: `Redshift Dashboard > Clusters > Select Your Cluster`
2. Click on the Cluster Security Groups
3. Open the Cluster Security Group
4. Click on “Add Connection Type”
5. Choose Connection Type CIDR/IP and authorize the [Secoda IPs](../../../faq.md#what-are-the-ip-addresses-for-secoda) to read into your Redshift Port

#### **EC2-VPC** <a href="#h_74f90aa17e" id="h_74f90aa17e"></a>

1. Navigate to your `Redshift Dashboard > Clusters > Select Your Cluster`
2. Click on the VPC Security Groups
3. Select the “Inbound” tab and then “Edit”
4. Allow Secoda to read into your Redshift Port using the [Secoda IP addresses](../../../faq.md#what-are-the-ip-addresses-for-secoda).

You can find more information on that [here](http://docs.aws.amazon.com/redshift/latest/mgmt/managing-clusters-vpc.html).

1. Navigate back to your Redshift Cluster Settings: `Redshift Dashboard > Clusters > Select Your Cluster`
2. Select the “Cluster” button and then “Modify”
3. Make sure the “Publicly Accessible” option is set to “Yes”
