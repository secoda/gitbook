---
description: List of all the metadata that Secoda pulls from Looker
---

# Metadata Extracted

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
* Fields - Dimensions and Measures&#x20;
* Views&#x20;
  * Name
  * Description
  * Tags
* Lineage
  * Looker Dashboard -> Looker Look
  * Looker Explore <-> Looker Look
  * Looker View <-> Looker Explore (including the Field level relationships)
  * Looker Views and Fields <-> Tables and Columns from other sources

{% hint style="info" %}
To determine lineage from Looker, we use the relationships and dependencies provided from the Looker APIs as well as our own Query parser to determine lineage to sources outside of Looker.
{% endhint %}
