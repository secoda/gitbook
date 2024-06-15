---
description: List of all the metadata that Secoda pulls from Apache Kafka
---

# Apache Kafka Metadata Extracted

### What does Secoda extract from Apache Kafka?

* Topics
  * Name
  * Segment Size in bytes
  * Compression Type
  * Cleanup Policy
  * Retention in ms
  * Max Message Size in bytes
  * Number of partitions
  * Is Internal
  * Replication Factor
* Consumer Groups
  * Name
  * Members Count
  * Replication Factor
  * Topics
  * Topic Partitions
    * Partition ID
    * Current Offset
    * Lag
* Schema
  * Name
  * Description
  * Type
  * Fields
* Lineage
  * Topic <--> Consumer Group
