---
description: >-
  Manual Lineage allows you to easily create lineage between any Resources in
  Secoda.
---

# Manual Lineage

## What is Manual Lineage?

You can read all about automated Lineage in Secoda [here](../data-lineage.md). Manual Lineage allows you to manually add lineage in addition to any lineage that is automatically brought into Secoda.&#x20;

### When to use Manual Lineage:

* Primary Keys and/or Foreign Keys are not defined on database tables
* Product APIs are not able to provide lineage details
* Parsed queries are not able to determine lineage
* To create lineage to Resources that are native to Secoda, such as [Dictionary Terms](../metrics/), [Documents](../docs/), [Questions](../data-requests/asking-questions-from-slack.md), and [Collections](../collections-1.md)

## How to use Manual Lineage

Open up the data asset you would like to add lineage to in Secoda, you can do this via the Catalog, or via Search

* Select the Lineage tab on the data asset, and click the `Add Node` button to manually add a new node to the Lineage diagram. A new Lineage Node modal will open up.
* From the new Lineage Node, use the search bar to search for the Resource you want to add to the Lineage diagram.&#x20;
* Connect the new Lineage Node to any desired Lineage Node on the diagram, and click `Save` to save your changes.

<figure><img src="../../.gitbook/assets/Screen Shot 2023-04-04 at 3.20.43 PM (1).png" alt=""><figcaption></figcaption></figure>

The new connection you have created is bi-directional on data assets. In the example above, this means if you navigate to the `Regional` dashboard's lineage diagram, you will see that the table `stg_payments` is now part of the lineage diagram.

## Video Resource

{% embed url="https://www.loom.com/share/a7681568611243e69720a62d9ce879d5" %}
