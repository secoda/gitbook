---
description: >-
  Secoda's PII identifier finds PII columns, tables or dashboards in your data
  in Secoda.
---

# PII Identifier

PII (Personally Identifiable Information) tags are used to identify data assets that contain personal information that could be used to identify an individual. PII tags can be used to help organizations protect personal data and comply with data privacy regulations such as GDPR and CCPA.

## **How to Tag PII in Secoda** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

{% hint style="info" %}
You can automate this process by creating an [automations.md](../../features/automations.md "mention"). Check out the template in the UI to get started!
{% endhint %}

You can easily find and tag PII data in Secoda. To do so, go to [**Settings**](../../readme/secoda-as-an-admin/settings.md) **-> Features -> PII scanning**

<figure><img src="../../.gitbook/assets/Screenshot 2025-06-24 at 12.35.08 PM.png" alt=""><figcaption></figcaption></figure>

Once you're in the PII scanning tab, you can see all the tables and columns that Secoda has identified that may contain PII data. You can select or deselect any of these columns or tables before applying the PII tag.

Secoda identifies PII columns based on a set of keywords that match column names. Some examples include first name, last name, address etc. If you'd like to customize these key words, you can do so by clicking on the settings button by the PII columns. Note, keywords are case and space sensitive.

## Governance Metadata

After tagging your data with the PII tag, these will populate in the **Governance** metadata column in your Catalog.

<figure><img src="../../.gitbook/assets/Screenshot 2025-06-24 at 12.37.59 PM.png" alt=""><figcaption></figcaption></figure>

## PII and Previews

Secoda offers the ability to [Preview](../../features/data-previews.md) the first 50 rows of a table. If permissions are granted for Preview, any column of the table that is marked as PII **will not show** as part of the Preview.

We recommend setting up the permissions for each Integration according to the governance policies for your organizational structure. Preview and Queries can be disabled for the workspace, or available to specific User Groups/Users. More information about how to set up permissions for Queries and Previews can be found in their respective documentation. Information about roles within Secoda can be found [here](../../user-management/roles.md).

## Removing PII Tags

There are several ways to remove a PII tag:&#x20;

1. You can click the PII value and select "Not PII".
2. You can select a number of resources (e.g., columns) in a table view with the checkmarks, choose the "Set PII" action, and select "Not PII".&#x20;
3. You can use Automations with the edit action "Remove PII". &#x20;

## Benefits of Using PII tags

1. **Enhanced data privacy**: By using PII tags, organizations can identify and protect personal data, helping to ensure that it is only accessed by authorized personnel and used in accordance with data privacy regulations.
2. **Improved data governance**: PII tags can help organizations establish clear policies and procedures for handling personal data and ensure that they are being followed. This can improve data governance and reduce the risk of data breaches or privacy violations.
3. **Enhanced data security**: PII tags can help organizations identify and secure personal data, reducing the risk of unauthorized access or misuse.
4. **Improved compliance**: By using PII tags, organizations can demonstrate compliance with data privacy regulations and reduce the risk of fines or other penalties.

{% hint style="info" %}
Not using Secoda to manage your data documentation yet? Sign up for free [here](http://app.secoda.co/) 👈
{% endhint %}
