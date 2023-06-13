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

![](https://secoda-public-media-assets.s3.amazonaws.com/Group%20587%20\(3\)%20\(1\)%20\(1\)%20\(1\)%20\(1\)%20\(1\).png)

Once you're in the Data tab, you can see all the tables and columns that Secoda has identified that may contain PII data. You can select or deselect any of these columns or tables before applying the PII tag.

![](https://secoda-public-media-assets.s3.amazonaws.com/Group%20587%20\(2\).png)

{% hint style="info" %}
This process is currently not automated, so Admins will have to manually go into the Settings each time they'd like to run the PII identifier.
{% endhint %}

## Governance Metadata

After tagging your data with the PII tag, these will populate in the **Governance** metadata column in your Catalog.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/Screenshot%202023-05-22%20at%203.56.25%20PM.png" alt=""><figcaption></figcaption></figure>

## Removing PII Tags

{% embed url="https://www.loom.com/share/79ebe1fb5a774e73b74bcf02f5d7a6d6" %}

## How It Works

#### More information on how it works behind the scenes

Secoda identifies PII columns based on a set of keywords that match column names. Some examples include first name, last name, address etc.



{% hint style="info" %}
Not using Secoda to manage your data documentation yet? Sign up for free [here](http://app.secoda.co/) 👈
{% endhint %}
