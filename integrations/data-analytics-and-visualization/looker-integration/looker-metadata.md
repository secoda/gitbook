---
description: List of all the metadata that Secoda pulls from Looker
---

# Looker Metadata

### What does Secoda extract from Looker?

NOTE: Preview of Looker resources in available in Secoda.&#x20;

#### Dashboard

* Name
* Description
* Tags
* Last Updated Timestamp
* External Usage
* Folder

#### Look

Looks are referred to as Charts in Secoda.

* Name
* Description
* URL
* Folder

#### Explore

Explores are referred to as Tables in Secoda.

* Name
* Description
* Tags
* Fields - Dimensions and Measures -> Fields are referred to as Columns in Secoda.

#### View

Views are referred to as Tables in Secoda.

* Name
* Description
* Tags
* Fields - Dimensions and Measures -> Fields are referred to as Columns in Secoda.

#### Lineage

To determine lineage from Looker, we use the relationships and dependencies provided from the Looker APIs as well as our own Query parser to determine lineage to sources outside of Looker.

* Looker Dashboard -> Looker Look
* Looker Explore <-> Looker Look
* Looker View <-> Looker Explore (including the Field level relationships)
* Looker Views and Fields <-> Tables and Columns from other sources
