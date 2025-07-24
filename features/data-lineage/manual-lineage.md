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
* To create lineage to Resources that are native to Secoda, such as [Dictionary Terms](broken-reference/), [Documents](broken-reference/), [Questions](../ask-questions-in-secoda.md), [Metrics](../metrics.md) and [Collections](../collections-1.md)

## How to use Manual Lineage

#### Creating New Lineage

1. Click into a resource that you would like to add a lineage node to in Secoda. You can do this via the Catalog, or via Search.
2. Click into the Lineage tab and hover over the resource you'd like to link a node to. Click on the blue plus button to manually add a new node to the Lineage diagram. A new Lineage Node modal will open up.
3. From the new Lineage Node, use the search bar to search for the Resource you want to add to the Lineage diagram.
4. Connect the new Lineage Node to any desired Lineage Node on the diagram, and click `Save` to save your changes.

The new connection you have created is bi-directional on Catalog resources. That means, if you connect a dashboard to a column (for example), you can go to that dashboard and see the connection there as well.

<figure><img src="../../.gitbook/assets/Screenshot 2025-07-17 at 5.15.52 PM.png" alt=""><figcaption></figcaption></figure>

#### Deleting Manual Lineage

If you've made an accidental connection or want to make updates, you can delete manual lineage by:

* Select the `...` menu icon on the lineage node that has a connection which you would like to delete
* Select the `Remove` option from the menu

{% hint style="info" %}
Note: You can only delete manually created lineage, not automatic lineage brought in from the source.
{% endhint %}

## Video Resource

{% embed url="https://www.loom.com/share/c30f3f9a09954c9993fa84a03425370b?sid=83b0b27f-abcd-46ce-96f8-e9b23ba1fddc" %}
