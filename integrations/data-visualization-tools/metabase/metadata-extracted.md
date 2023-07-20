# Metadata Extracted

### What does Secoda extract from Metabase?

* Collections (Collections are referred to as Dashboard Groups in Secoda)
  * Collection Name
* Dashboard
  * Dashboard Name
  * Dashboard Description
  * Dashboard Owners
  * Dashboard Last Updated Timestamp
  * Dashboard URL
* Cards (Cards are referred to as Charts in Secoda)
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
