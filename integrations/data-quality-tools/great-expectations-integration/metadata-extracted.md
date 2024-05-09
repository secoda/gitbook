---
description: List of all the metadata that Secoda pulls from Great Expectations
---

# Great Expectations Metadata Extracted

### What does Secoda extract from Great Expectations?

* Expectation Suite
  * Name
* Expectation
  * Name
  * Columns
* Validation
  * Name
  * Columns
  * Status
  * Error
  * Created At
  * Result
* Lineage
  * Expectations <-> Tables from other sources
  * Validations <-> Tables from other sources

{% hint style="warning" %}
Only validation files within last 30 days are extracted if there was no prior extraction. Subsequent syncs check the timestamp of the validations files and if it's after the last extraction, the new results will be extracted.
{% endhint %}
