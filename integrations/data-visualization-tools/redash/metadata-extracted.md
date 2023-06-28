# Redash Metadata

### What does Secoda extract from Redash?

#### Widget

Widgets are referred to as Charts in Secoda.

* Name
* URL

#### Dashboard

* Name
* Description
* Updated At
* Owners
* URL

**Query**

#### Lineage

To determine lineage from Redash, we parse the queries that we extract from Redash using the APIs.&#x20;

* Redash Query <-> Redash Widget
* Redash Query <-> Redash Dashboard
* Redash Query <-> Tables from other sources
  * Note: These lineage relationships will pass through the Query to the Dashboards and Widgets that that Query connects to.&#x20;

