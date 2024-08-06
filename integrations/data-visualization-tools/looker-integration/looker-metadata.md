---
description: List of all the metadata that Secoda pulls from Looker
---

# Looker Metadata Extracted

### What does Secoda extract from Looker?

{% hint style="info" %}
NOTE: Preview of Looker resources is available in Secoda if permissions are granted.&#x20;
{% endhint %}

* Dashboard
  * Name
  * Description
  * Tags
  * Last Updated Timestamp
  * External Usage
  * Folder
* Look
  * Name
  * Description
  * URL
  * Folder
* Explores
  * Name
  * Description
  * Tags
  * Fields (including Dimensions and Measures)
    * Description
    * Tags
    * SQL
* Views&#x20;
  * Name
  * Description
  * Tags
  * Dimensions
    * Description
    * Tags
    * SQL
  * Measures
    * Description
    * Tags
    * SQL
* Lineage
  * Looker Dashboard -> Looker Look
  * Looker Explore <-> Looker Look
  * Looker View <-> Looker Explore (including the Field level relationships)
  * Looker Views and Fields <-> Tables and Columns from other sources

{% hint style="info" %}
To determine lineage from Looker, we use the relationships and dependencies provided from the Looker APIs as well as our own Query parser to determine lineage to sources outside of Looker.
{% endhint %}

