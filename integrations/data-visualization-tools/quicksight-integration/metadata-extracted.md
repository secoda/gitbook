---
description: List of all the metadata that Secoda pulls from QuickSight
---

# Metadata Extracted

### What does Secoda extract from QuickSight?

* Analyses
  * Analysis Name
  * Analysis Last Updated At
  * Analysis URL
* Sheets
  * Sheet Name
  * Sheet URL
* Datasets
  * Dataset Name
* Columns
  * Column Name
  * Column Type
* Dashboards
  * Dashboard Name
  * Dashboard Last Updated At
  * Dashboard URL
* Lineage
  * QuickSight Dataset <-> QuickSight Analysis
  * QuickSight Sheet <-> QuickSight Analysis
  * QuickSight Dashboard <-> QuickSight Analysis
  * QuickSight Dataset <-> Tables from other sources

{% hint style="info" %}
To determine lineage from QuickSight, we use the relationships and dependencies provided from the QuickSight APIs.
{% endhint %}
