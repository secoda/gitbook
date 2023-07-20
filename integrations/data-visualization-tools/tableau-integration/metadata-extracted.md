# Metadata Extracted

### What does Secoda extract from Tableau?

NOTE: Preview of Tableau resources is available in Secoda if permissions are granted.&#x20;

* Published Datasources (Published Datasources are referred to as Tables in Secoda)
  * Name
  * Description
  * Columns
* Embedded Datasource (Embedded Datasources are referred to as Tables in Secoda)
  * Name
  * Columns
* Workbooks (Workbooks are referred to as Dashboards in Secoda)
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
* Sheets (Sheets are referred to as Charts in Secoda)&#x20;
  * Name
  * URL
  * Owners
* Fields (Fields are referred to as Columns in Secoda)
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
