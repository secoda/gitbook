---
description: List of all the metadata that Secoda pulls from Dagster
---

# Dagster Metadata Extracted

### What does Secoda extract from Dagster?

* Asset
  * Description
  * Asset type
* Asset groups
  * Name
* Jobs
  * Name
  * Description
  * URL
  * Tags
  * Runs
    * Name (ID of the run)
    * Status
    * Created date (Timestamp)
    * Finished date (Timestamp)
* Step
  * Title
  * Start time
  * Finish time
* Repository
  * Title
* Location
  * Title
* Lineage
  * Repository <-> Asset
  * Asset <-> Job

{% hint style="info" %}
Dagster Lineage in Secoda is generated through [asset dependencies](https://docs.dagster.io/concepts/assets/software-defined-assets#assets-with-dependencies). We are not currently syncing [external dependencies](https://docs.dagster.io/concepts/assets/software-defined-assets#defining-external-asset-dependencies), so you should not expect to see lineage downstream to BI tools, tables, etc.
{% endhint %}
