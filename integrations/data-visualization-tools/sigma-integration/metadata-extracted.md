# Sigma Metadata

### What does Secoda extract from Sigma?

#### Element

Elements are referred to as Charts in Secoda.

* Name
* URL

#### Workbook

Workbooks are referred to as Dashboards in Secoda.

* Name
* Updated At
* Owners
* URL

**Query**

#### Lineage

To determine lineage from Sigma, we parse the queries that we extract from Sigma using the APIs.&#x20;

* Sigma Element <-> Sigma Workbook
* Sigma Query <-> Sigma Element
* Sigma Query <-> Sigma Workbook
* Sigma Query <-> Tables from other sources
  * Note: These lineage relationships will pass through the Query to the Workbooks and Elements that that Query connects to.&#x20;

