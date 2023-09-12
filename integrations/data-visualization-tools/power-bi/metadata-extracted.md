# Metadata Extracted

### What does Secoda extract from PowerBI?

* Groups (Groups are referred to as Dashboard Groups in Secoda)
  * Group Name
* Reports (Reports are referred to as Charts in Secoda)
  * Report Name
  * Report Description
  * Report Owners
  * Report Usage (Number of views in PowerBI)
  * Report URL
* Tiles (Tiles are referred to as Charts in Secoda)
  * Tile Name
  * Tile Description
  * Tile Owners
  * Tile URL
* Datasets (Datasets are referred to as Schemas in Secoda)
  * Dataset Name
* Tables
  * Table Name
* Measures (Measures are referred to as Columns in Secoda)
  * Measure Name
* Dashboards
  * Dashboard Name
  * Dashboard Description
  * Dashboard Owners
  * Dashboard URL
* Pages (Pages are referred to as Charts in Secoda)
  * Page Name
* Lineage
  * PowerBI Table <-> PowerBI Report
  * PowerBI Tile <-> PowerBI Dashboard
  * PowerBI Tile <-> PowerBI Report

{% hint style="info" %}
To determine lineage from PowerBI, we use the relationships and dependencies provided from the PowerBI APIs.
{% endhint %}
