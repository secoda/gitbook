---
description: >-
  Manual Lineage allows you to easily create lineage between any Resources in
  Secoda.
---

# Manual Lineage

## What is Manual Lineage?

You can read all about automated Lineage in Secoda [here](../data-lineage.md). Manual Lineage allows you to manually add lineage in addition to any lineage that is automatically brought into Secoda.

### When to use Manual Lineage:

* Primary Keys and/or Foreign Keys are not defined on database tables
* Product APIs are not able to provide lineage details
* Parsed queries are not able to determine lineage
* To create lineage to Resources that are native to Secoda, such as [Dictionary Terms](broken-reference), [Documents](broken-reference/), [Questions](../ask-questions-in-secoda/asking-questions-from-slack.md), and [Collections](../collections-1.md)

## How to use Manual Lineage

#### Creating New Lineage

Open up the data asset you would like to add lineage to in Secoda, you can do this via the Catalog, or via Search

* Select the Lineage tab on the data asset, and click the `Add Node` button <mark style="color:red;">**(A)**</mark> to manually add a new node to the Lineage diagram. A new Lineage Node modal will open up.
* From the new Lineage Node, use the search bar <mark style="color:red;">**(B)**</mark> to search for the Resource you want to add to the Lineage diagram.
* Connect the new Lineage Node to any desired Lineage Node on the diagram <mark style="color:red;">**(C)**</mark>, and click `Save` to save your changes.

```
<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/Screen%20Shot%202023-04-04%20at%203.20.43%20PM.png" alt=""></figure>
```

The new connection you have created is bi-directional on data assets. In the example above, this means if you navigate to the `Regional` dashboard's lineage diagram, you will see that the table `stg_payments` is now part of the lineage diagram.

#### Deleting Manual Lineage

If you've made an accidental connection or want to make updates, you can delete manual lineage by:

* Select the `...` menu icon on the lineage node that has a connection which you would like to delete
* Select the `Remove` option from the menu

{% hint style="info" %}
Note: You can only delete manually created lineage, not automatic lineage brought in from the source.
{% endhint %}

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/Screen%20Shot%202023-04-05%20at%204.22.52%20PM.png" alt=""></figure>

## Video Resource

{% embed url="https://www.loom.com/share/a7681568611243e69720a62d9ce879d5" %}
