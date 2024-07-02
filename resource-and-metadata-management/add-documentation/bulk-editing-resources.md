---
description: >-
  This section will go over how to edit data resources in bulk- descriptions,
  columns, tables, badges, tags, etc.
---

# Bulk Editing

## Introduction

Adding documentation manually to one resource at a time can be useful for small amounts of unique data. However, if you have large volumes of data requiring documentation, Secoda offers efficient solutions through both manual and automated bulk editing.

## **Bulk Editing**

1. **Navigate:**&#x20;
   * Go to any section where bulk edits are needed, such as the Catalog, Collections, Metrics, Dictionary, Documents, or Questions.&#x20;
   * For this example, we'll use the **Catalog**.
2. **Filter Resources:**&#x20;
   * Apply relevant [filters.md](../../features/filters.md "mention") to narrow down the resources you want to edit.&#x20;
   * For instance, filter by Integration=Tableau and Type=Dashboard to filter on Tableau dashboards.
3. **Select Resources:**
   * **Select All:** Click the checkbox in the upper left corner to select all visible resources.
   * **Select Individually:** Check boxes one by one for specific resources.
   * **Select a Range:** Click the first checkbox, hold the Shift key, and click the last checkbox in the range you want to edit.
4. **Execute Commands:**
   * View all available [#commands-options](bulk-editing-resources.md#commands-options "mention") by clicking the three-dot Commands button at the bottom of the screen. Options like Set PII and Verify might be suggested based on the context.
   * Choose the appropriate bulk update action from the menu and confirm your selection to apply changes.

### Commands options

* [propagating-metadata.md](propagating-metadata.md "mention")
* Set Collections
* Set tags
* Set owners
* Set published
* Set PII
* Verify
* Apply AI description
* Delete selected

### **Video resource**

To help you visualize the process of making bulk edits in Secoda, we've included a GIF that covers the essential steps: filtering resources, selecting them, choosing a command, and applying the changes.

As you can see below, we've filtered for PII resources, selected all, chose the Verify command, and applied the bulk changes.

<figure><img src="../../.gitbook/assets/Kapture 2024-04-30 at 16.04.21 (1).gif" alt=""><figcaption><p>Bulk Catalog Edits</p></figcaption></figure>

## **Bulk Editing with Automations**

* **Set Up Automation:** Learn how to use Automations in Secoda to handle bulk edits. For instance, you can create an Automation that applies the same definition to all columns named "customer\_id".
* **Guide:** [Read up on setting up Automations](../../features/automations.md) to bulk edit resources in Secoda.

## **Conclusion**&#x20;

Secoda’s bulk editing features are designed to simplify the process of updating large data sets, making it easy to maintain consistency and accuracy across your resources. Whether through automation or manual selection, these tools help you efficiently manage and document your data.

{% hint style="info" %}
Not using Secoda to manage your data documentation yet? Sign up for free [here](http://app.secoda.co/) 👈
{% endhint %}
