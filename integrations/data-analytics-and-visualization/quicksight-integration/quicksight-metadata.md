# QuickSight Metadata

### What does Secoda extract from QuickSight?

#### Analysis

Analyses are referred to as Dashboards in Secoda.

* Name
* Updated At
* URL

#### Sheet

Sheets are referred to as Charts in Secoda.

* Name
* URL

#### Dataset

Datasets are referred to as Tables in Secoda.

* Name

#### Column

* Name
* Type

#### Dashboard

* Name
* Updated At
* URL

#### Lineage

To determine lineage from QuickSight, we use the relationships and dependencies provided from the QuickSight APIs.

* QuickSight Dataset <-> QuickSight Analysis
* QuickSight Sheet <-> QuickSight Analysis
* QuickSight Dashboard <-> QuickSight Analysis
* QuickSight Dataset <-> Tables from other sources

