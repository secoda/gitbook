---
description: List of all the metadata that Secoda pulls from Mode
---

# Metadata Extracted

### What does Secoda extract from Mode?

{% hint style="info" %}
NOTE: Preview of Mode resources is available in Secoda if permissions are granted.&#x20;
{% endhint %}

* Spaces
  * Space Name
* Report&#x20;
  * Report Name
  * Report Description
  * Report Owners
  * Report URL
* Dataset
  * Dataset name
  * Dataset Description
  * Dataset Owner
* Field
  * Field Name
  * Field Type
* Charts
  * Chart Name
  * Chart Description
  * Chart URL
* Queries
* Lineage
  * Mode Chart <-> Mode Report
  * Mode Query <-> Mode Chart
  * Mode Query <-> Mode Dataset
  * Mode Dataset <-> Mode Chart
  * Mode Chart <-> Tables from other sources

{% hint style="info" %}
To determine lineage from Mode, we use the relationships and dependencies provided from the Mode APIs as well as our own Query parser to determine lineage to sources outside of Mode.
{% endhint %}
