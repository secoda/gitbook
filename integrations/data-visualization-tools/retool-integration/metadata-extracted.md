---
description: List of all the metadata that Secoda pulls from Retool
---

# Metadata Extracted

### What does Secoda extract from Retool?

{% hint style="info" %}
NOTE: Preview of Retool resources is available in Secoda if permissions are granted.&#x20;
{% endhint %}

* Folders
  * Folder Name
  * Folder Updated At
  * Folder URL
* Global Widgets
  * Global Widget Name
  * Global Widget Description
  * Global Widget Last Updated At
  * Global Widget URL
  * Global Widget Folder
* Apps
  * App Name
  * App Description
  * App Updated At
  * App URL
* Queries
* Lineage
  * Retool Query <-> Retool App
  * Retool Query <-> Tables from other sources
    * Note: These lineage relationships will pass through the Query to the Apps that that Query connects to.&#x20;

{% hint style="info" %}
To determine lineage from Retool, we parse the queries that we extract from Retool using the APIs.&#x20;
{% endhint %}
