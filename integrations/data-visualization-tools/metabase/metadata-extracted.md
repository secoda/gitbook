---
description: List of all the metadata that Secoda pulls from Metabase
---

# Metabase Metadata Extracted

### What does Secoda extract from Metabase?

{% hint style="info" %}
NOTE: Preview of Metabase resources is available in Secoda if permissions are granted. [Interactive embedding ](https://www.metabase.com/docs/latest/embedding/interactive-embedding#enabling-interactive-embedding-in-metabase)will need to be enabled for Metabase Previews in Secoda to work.
{% endhint %}

* Collections
  * Collection Name
* Dashboard
  * Dashboard Name
  * Dashboard Description
  * Dashboard Owners
  * Dashboard Last Updated Timestamp
  * Dashboard URL
* Cards
  * Card Name
  * Card Description
  * Card URL
* Queries
* Lineage
  * Metabase Card <-> Metabase Dashboard
  * Metabase Query <-> Metabase Card
  * Metabase Query <-> Metabase Dashboard
  * Metabase Card <-> Tables from other sources

{% hint style="info" %}
To determine lineage from Metabase, we use the relationships and dependencies provided from the Metabase APIs as well as our own Query parser to determine lineage to sources outside of Metabase.
{% endhint %}
