---
description: List of all the metadata that Secoda pulls from Sigma
---

# Metadata Extracted

### What does Secoda extract from Sigma?

{% hint style="info" %}
NOTE: Preview of Sigma resources is available in Secoda if permissions are granted.&#x20;
{% endhint %}

* Workbooks
  * Workbook Name
  * Workbook Updated At
  * Workbook Owners
  * Workbook URL
* Pages
  * Page Name
  * Page URL
* Elements
  * Element Name
  * Element URL
* Badges
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
