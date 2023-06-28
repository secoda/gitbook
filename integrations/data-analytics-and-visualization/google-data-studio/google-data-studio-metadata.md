# Google Data Studio Metadata

### What does Secoda extract from Google Data Studio?

#### Report&#x20;

Reports are referred to as Dashboards in Secoda.

* Name
* Description
* Last Updated Time
* Owners
* URL

#### Chart

* Name
* URL

#### Table

* Name

#### Lineage

To determine lineage from Google Data Studio, we use the relationships and dependencies provided from Google Data Studio as well as our own Query parser to determine lineage to sources outside of Google Data Studio.

* Google Data Studio Dashboard <-> Google Data Studio Chart
* Google Data Studio Dashboard <-> Google Data Studio Table
* Google Data Studio Dashboard <-> Tables from other sources
