# Metadata Extracted

### What does Secoda extract from Mode?

NOTE: Preview of Mode resources is available in Secoda if permissions are granted.&#x20;

* Spaces (Spaces are referred to as Dashboard Groups in Secoda)
  * Space Name
* Report (Reports are referred to as Dashboards in Secoda)
  * Report Name
  * Report Description
  * Report Owners
  * Report URL
* Charts
  * Chart Name
  * Chart Description
  * Chart URL
* Queries
* Lineage
  * Mode Chart <-> Mode Report
  * Mode Query <-> Mode Chart
  * Mode Query <-> Mode Dashboard
  * Mode Chart <-> Tables from other sources

{% hint style="info" %}
To determine lineage from Mode, we use the relationships and dependencies provided from the Mode APIs as well as our own Query parser to determine lineage to sources outside of Mode.
{% endhint %}
