# Mode Metadata

### What does Secoda extract from Mode?

NOTE: Preview of Mode resources in available in Secoda.&#x20;

#### Space

Spaces are referred to as Dashboard Groups in Secoda.

* Name

#### Report

Reports are referred to as Dashboards in Secoda.

* Name
* Description
* Owners
* URL

#### Chart

* Name
* Description
* URL

#### Query

#### Lineage

To determine lineage from Mode, we use the relationships and dependencies provided from the Mode APIs as well as our own Query parser to determine lineage to sources outside of Mode.

* Mode Chart <-> Mode Report
* Mode Query <-> Mode Chart
* Mode Query <-> Mode Dashboard
* Mode Chart <-> Tables from other sources

