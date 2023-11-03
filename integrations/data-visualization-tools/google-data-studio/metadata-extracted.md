# Metadata Extracted

### What does Secoda extract from Google Data Studio?

* Reports
  * Report Name
  * Report Description
  * Report Last Updated Time
  * Report URL
* Charts
  * Chart Name
  * Chart URL
* Tables
  * Table Name
* Lineage&#x20;
  * Google Data Studio Dashboard <-> Google Data Studio Chart
  * Google Data Studio Dashboard <-> Google Data Studio Table
  * Google Data Studio Dashboard <-> Tables from other sources

{% hint style="info" %}
To determine lineage from Google Data Studio, we use the relationships and dependencies provided from Google Data Studio as well as our own Query parser to determine lineage to sources outside of Google Data Studio.
{% endhint %}
