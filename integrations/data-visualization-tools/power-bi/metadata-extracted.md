---
description: List of all the metadata that Secoda pulls from Power BI
---

# Power BI Metadata Extracted

### What does Secoda extract from PowerBI?&#x20;

* Groups
  * Name
* Reports
  * Name
  * Description
  * Owners
  * Usage (Number of views in PowerBI)
  * URL
  * Tags
  * Preview
* Tiles
  * Name
  * Description
  * Owners
  * URL
  * Tags
* Pages
  * Name
  * Tags
* Datasets
  * Name
* Tables
  * Name
  * Tags
* Measures
  * Name
* Dashboards
  * Name
  * Description
  * Owners
  * URL
  * Tags
  * Preview
* DAX
* Dataflows
  * Name
  * Description
  * Owner

{% hint style="info" %}
You must fully enable metadata scanning in order for DAX expressions to be returned. For more information, see [Enable tenant settings for metadata scanning](https://learn.microsoft.com/en-us/power-bi/admin/service-admin-metadata-scanning-setup#enable-tenant-settings-for-metadata-scanning).
{% endhint %}

* Pages (Pages are referred to as Charts in Secoda)
  * Page Name
* Lineage
  * PowerBI Table <-> PowerBI Report
  * PowerBI Tile <-> PowerBI Dashboard
  * PowerBI Tile <-> PowerBI Report

{% hint style="info" %}
To determine lineage from PowerBI, we use the relationships and dependencies provided from the PowerBI APIs. If using Non Admin APIs we will not be able to show lineage to other resources (ex Snowflake tables), but lineage within PowerBI will be visible.
{% endhint %}
