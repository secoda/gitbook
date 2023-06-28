# Tableau Metadata

### What does Secoda extract from Tableau?

NOTE: Preview of Tableau resources in available in Secoda.&#x20;

#### Published Datasource

Published Datasources are referred to as Tables in Secoda.

* Name
* Description
* Columns

#### Embedded Datasource

Embedded Datasources are referred to as Tables in Secoda.&#x20;

* Name
* Columns

#### Workbook

Workbooks are referred to as Dashboards in Secoda.

* Name
* Description
* Owners
* URL
* Updated At
* Number of Views

**Dashboard**

* Name
* Description
* Owners
* URL
* Updated At

#### Sheet

Sheets are referred to as Charts in Secoda.&#x20;

* Name
* URL
* Owners

#### Field

Fields are referred to as Columns in Secoda.

* Name
* Description
* Type

#### Custom SQL Table

Custom SQL Tables are referred to as Queries in Secoda.

#### Lineage

To determine lineage from Tableau, we parse the queries that we extract from Tableau using the APIs along with the lineage returned by Tableau directly

* Tableau Datasources <-> Tables from other sources
* Tableau Fields <-> Columns from other sources
* Tableau Datasources <-> Tableau Workbooks
* Tableau Workbooks <-> Tableau Sheets
* Tableau Dashboards <-> Tableau Sheets
* Tableau Workbooks <-> Tableau Dashboards

