---
description: List of all the metadata that Secoda pulls from Google Data Studio
---

# Looker Studio Metadata Extracted

### What does Secoda extract from Looker Studio?

* Reports
  * Report Name
  * Report Description
  * Report Last Updated Time
  * Report URL
* Charts
  * Chart Name
  * Chart URL
* Tables
  * Table Name
* Lineage&#x20;
  * Google Data Studio Dashboard <-> Looker Studio Chart
  * Google Data Studio Dashboard <-> Looker Studio Table
  * Google Data Studio Dashboard <-> Tables from other sources

{% hint style="info" %}
To determine lineage from Looker Studio, we use the relationships and dependencies provided from Looker Studio as well as our own Query parser to determine lineage to sources outside of Looker Studio.
{% endhint %}
