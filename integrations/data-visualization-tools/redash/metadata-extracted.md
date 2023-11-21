---
description: List of all the metadata that Secoda pulls from Redash
---

# Metadata Extracted

### What does Secoda extract from Redash?

* Widgets (Widgets are referred to as Charts in Secoda)
  * Widget Name
  * Widget URL
* Dashboards
  * Dashboard Name
  * Dashboard Description
  * Dashboard Last Updated At
  * Dashboard Owners
  * Dashboard URL
* Queries
* Lineage
  * Redash Query <-> Redash Widget
  * Redash Query <-> Redash Dashboard
  * Redash Query <-> Tables from other sources
    * Note: These lineage relationships will pass through the Query to the Dashboards and Widgets that that Query connects to.&#x20;

{% hint style="info" %}
To determine lineage from Redash, we parse the queries that we extract from Redash using the APIs.&#x20;
{% endhint %}
