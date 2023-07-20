# Metadata Extracted

### What does Secoda extract from Sigma?

* Elements (Elements are referred to as Charts in Secoda)
  * Element Name
  * Element URL
* Workbooks (Workbooks are referred to as Dashboards in Secoda)
  * Workbook Name
  * Workbook Updated At
  * Workbook Owners
  * Workbook URL
* Queries
* Lineage
  * Sigma Element <-> Sigma Workbook
  * Sigma Query <-> Sigma Element
  * Sigma Query <-> Sigma Workbook
  * Sigma Query <-> Tables from other sources
    * Note: These lineage relationships will pass through the Query to the Workbooks and Elements that that Query connects to.&#x20;

{% hint style="info" %}
To determine lineage from Sigma, we parse the queries that we extract from Sigma using the APIs.&#x20;
{% endhint %}
