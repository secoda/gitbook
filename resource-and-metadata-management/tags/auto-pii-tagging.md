---
description: >-
  Secoda's PII identifier finds PII columns, tables or dashboards in your data
  in Secoda.
---

# PII Identifier

PII (Personally Identifiable Information) tags are used to identify data assets that contain personal information that could be used to identify an individual. PII tags can be used to help organizations protect personal data and comply with data privacy regulations such as GDPR and CCPA.

## Benefits of Using PII tags

1. **Enhanced data privacy**: By using PII tags, organizations can identify and protect personal data, helping to ensure that it is only accessed by authorized personnel and used in accordance with data privacy regulations.
2. **Improved data governance**: PII tags can help organizations establish clear policies and procedures for handling personal data and ensure that they are being followed. This can improve data governance and reduce the risk of data breaches or privacy violations.
3. **Enhanced data security**: PII tags can help organizations identify and secure personal data, reducing the risk of unauthorized access or misuse.
4. **Improved compliance**: By using PII tags, organizations can demonstrate compliance with data privacy regulations and reduce the risk of fines or other penalties.

## **How to Auto Tag PII in Secoda** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

By going to the data tab, you can find and auto tag PII data in Secoda easily. To tag your PII data, go to **Settings -> Data**

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/0e18030a-19a6-48e5-be3a-389182a2df16.png" alt=""></figure>

Once you're in the Data tab, you can see all the tables and columns that Secoda has identified that may contain PII data. You can select or deselect any of these columns or tables before applying the PII tag.

{% hint style="info" %}
This process is currently not automated, so Admins will have to manually go into the Settings each time they'd like to run the PII identifier.
{% endhint %}

Secoda identifies PII columns based on a set of keywords that match column names. Some examples include first name, last name, address etc. If you'd like to customize these key words, you can do so by clicking on the settings button by the PII columns. Note, keywords are case and space sensitive.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/63d4c81d-b8a0-4aca-b7cb-f27c31299f55.gif" alt=""></figure>

## Governance Metadata

After tagging your data with the PII tag, these will populate in the **Governance** metadata column in your Catalog.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/Screenshot%202023-05-22%20at%203.56.25%20PM.png" alt=""></figure>

## PII and Previews

Secoda offers the ability to [Preview](../../features/data-previews.md) the first 50 rows of a table. If permissions are granted for Preview, any column of the table that is marked as PII **will not show** as part of the Preview.&#x20;

This behaviour does not extend to [Queries](../../features/queries/). If a query is run on a table, the results are shown exactly as returned from the Source. This means that if the query results are returned with data from columns marked as PII, the user making the query will be able to view the potentially sensitive information.&#x20;

We recommend setting up the permissions for each Integration according to the governance policies for your organizational structure. Preview and Queries can be disabled for the workspace, or available to specific User Groups/Users. More information about how to set up permissions for Queries and Previews can be found in their respective documentation. Information about roles within Secoda can be found [here](../../user-management/roles/).

## Removing PII Tags

{% embed url="https://www.loom.com/share/79ebe1fb5a774e73b74bcf02f5d7a6d6" %}

{% hint style="info" %}
Not using Secoda to manage your data documentation yet? Sign up for free [here](http://app.secoda.co/) 👈
{% endhint %}
