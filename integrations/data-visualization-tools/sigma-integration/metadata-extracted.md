---
description: List of all the metadata that Secoda pulls from Sigma
---

# Metadata Extracted

### What does Secoda extract from Sigma?

NOTE: Preview of Sigma resources is available in Secoda if permissions are granted.&#x20;

* Workbooks (Workbooks are referred to as Dashboards in Secoda)
  * Workbook Name
  * Workbook Updated At
  * Workbook Owners
  * Workbook URL
* Pages (Pages are referred to as Dashboards in Secoda)
  * Page Name
  * Page URL
* Elements (Elements are referred to as Charts in Secoda)
  * Element Name
  * Element URL
* Badges (Badges are referred to as Tags in Secoda)
  * Name
* Queries
* Lineage
  * Sigma Element <-> Sigma Workbook
  * Sigma Query <-> Sigma Element
  * Sigma Query <-> Sigma Workbook
  * Sigma Page -> Sigma Workbook
  * Sigma Element -> Sigma Page
  * Sigma Query <-> Tables from other sources
    * Note: These lineage relationships will pass through the Query to the Workbooks and Elements that that Query connects to.&#x20;

{% hint style="info" %}
To determine lineage from Sigma, we parse the queries that we extract from Sigma using the APIs.&#x20;
{% endhint %}
