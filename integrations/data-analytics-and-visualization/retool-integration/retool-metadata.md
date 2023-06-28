# Retool Metadata

### What does Secoda extract from Retool?

#### Folder

Folders are referred to as Dashboard Groups in Secoda.

* Name
* Updated At
* URL

#### Global Widget

Global Widgets are referred to as Dashboards in Secoda.

* Name
* Description
* Updated At
* URL
* Folder

#### App

Apps are referred to as Dashboards in Secoda.

* Name
* Description
* Updated At
* URL
* Folder

**Query**

#### Lineage

To determine lineage from Retool, we parse the queries that we extract from Retool using the APIs.&#x20;

* Retool Query <-> Retool App
* Retool Query <-> Tables from other sources
  * Note: These lineage relationships will pass through the Query to the Apps that that Query connects to.&#x20;

