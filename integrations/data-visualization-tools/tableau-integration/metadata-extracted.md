---
description: List of all the metadata that Secoda pulls from Tableau
---

# Tableau Metadata Extracted

### What does Secoda extract from Tableau?

{% hint style="info" %}
NOTE: Preview of Tableau resources is available in Secoda if permissions are granted.&#x20;
{% endhint %}

* Published Datasources
  * Name
  * Description
  * Columns
  * Owners
* Embedded Datasource
  * Name
  * Columns
  * Owners
* Workbooks&#x20;
  * Name
  * Description
  * Owners
  * URL
  * Updated At
  * Number of Views
* Dashboard
  * Name
  * Description
  * Owners
  * URL
  * Updated At
  * Number of Views
* Sheets
  * Name
  * URL
  * Owners
  * Number of Views
* Fields
  * Name
  * Description
  * Type
* Custom SQL Table (Custom SQL Tables are referred to as Queries in Secoda)
* Lineage
  * Tableau Datasources <-> Tables from other sources
  * Tableau Fields <-> Columns from other sources
  * Tableau Datasources <-> Tableau Workbooks
  * Tableau Workbooks <-> Tableau Sheets
  * Tableau Dashboards <-> Tableau Sheets
  * Tableau Workbooks <-> Tableau Dashboards

{% hint style="info" %}
To determine lineage from Tableau, we parse the queries that we extract from Tableau using the APIs along with the lineage returned by Tableau directly
{% endhint %}
