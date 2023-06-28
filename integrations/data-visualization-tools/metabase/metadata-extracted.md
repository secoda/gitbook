# Metabase Metadata

### What does Secoda extract from Metabase?

#### Collection

Collections are referred to as Dashboard Groups in Secoda.

* Name

#### Dashboard

* Name
* Description
* Owners
* Last Updated Timestamp
* URL

#### Card

Cards are referred to as Charts in Secoda.

* Name
* Description
* URL

#### Query

#### Lineage

To determine lineage from Metabase, we use the relationships and dependencies provided from the Metabase APIs as well as our own Query parser to determine lineage to sources outside of Metabase.

* Metabase Card <-> Metabase Dashboard
* Metabase Query <-> Metabase Card
* Metabase Query <-> Metabase Dashboard
* Metabase Card <-> Tables from other sources

