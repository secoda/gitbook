---
description: List of all the metadata that Secoda pulls from dbt Core
---

# Metadata Extracted

## What does Secoda extract from dbt Core?

* Models:&#x20;
  * Description&#x20;
  *
  * URL&#x20;
  * Compiled SQL&#x20;
* Columns:&#x20;
  * Description&#x20;
  * Tags&#x20;
  * Updated Time
* Tests:&#x20;
  * Name&#x20;
  * Description&#x20;
  * URL&#x20;
  * Tags&#x20;
  * Status&#x20;
  * Error&#x20;
  * Compiled code
* Metrics (Referred to as Dictionary terms in Secoda) on dbt v1.5 or less:
  * Name&#x20;
  * Type&#x20;
  * Dimensions&#x20;
  * Time Grains
* Lineage:
  * dbt Jobs <-> external Tables
  * dbt Exposures <-> external Tables
* Groups (Groups are referred to as `USER_GROUPS` in Secoda)
* Contracts (dbt Contracts are referred to as `TEST` in Secoda)
* Exposures (dbt Exposures are referred to as `DASHBOARD` in Secoda)
  1. The exposures can be a dashboard, notebook, analysis, ml, or application, but we currently only support dashboards.
* Semantic layer metrics (Referred to as Dictionary terms in Secoda) on dbt v1.6+:
  * Name
  * Type (Simple, Ration, Derived)
