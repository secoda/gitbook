---
description: >-
  Streamline your data discovery by applying tailored filters to efficiently
  navigate and manage resources in Secoda.
---

# Filters

## **Overview**&#x20;

Filters are powerful tools in Secoda that enhance your ability to efficiently explore and access metadata. This guide explains how to set up and effectively use filters in both the Catalog and Search functions.

**Note:** Consider saving your filters with [#search-views](search.md#search-views "mention") to streamline your workflow, particularly if you frequently revisit specific datasets. Saved views can be quickly accessed, reducing the time spent reapplying the same filters.

## **Filtering your Search**

Use Secoda's [search.md](search.md "mention") function to apply filters and narrow down your results. This is particularly useful when searching for specific data characteristics across your entire database.

### Filter categories

In Secoda, you can apply filters based on the following categories:

| Type                     | Filters                                                                                                     |
| ------------------------ | ----------------------------------------------------------------------------------------------------------- |
| Resource characteristics | Type, Integration, Related                                                                                  |
| Metadata properties      | Title, Description, Tags, Status, Priority, Published, Collections, Owners, Governance, Verification, Teams |
| Temporal filters         | Created time, Updated time, Externally updated time                                                         |
| Source filters           | Metadata source, Group, Schema, Database, Table                                                             |

### Build filters with operators

Once you add a filter, refine it with operators. The filter type itself cannot be changed, but you can modify other components of the filter to tweak your query. For example, a filter for "Owner is ainslie@secoda.co" can be adjusted as follows:

* Clicking on "is" allows you to change the operator to "is not" or "is not set".
* Clicking on "ainslie@secoda.co" will display a selectable list to modify the owner.

We support the following operators in Secoda, which will show up depending on the type of filter and selections:

* _is, is not,_ and _is not set_ when one option is included in the filter.
* _is any of, is not_ and _is not set_ when multiple options are included in the filter.
* _is on or before_ or _after_ for date-related filters.

<figure><img src="../.gitbook/assets/Kapture 2024-05-20 at 17.28.39.gif" alt=""><figcaption><p>Advanced filtering in Search</p></figcaption></figure>

### Create views

Once you've applied at least one filter to your search, a 'Save View' button will appear in the top right corner. Clicking this button takes you to the View editor with the applied filters. This feature helps in managing customized data views efficiently. Learn more about [#search-views](search.md#search-views "mention").

### **Tips for Advanced Filtering**

* **Combining Filters:** Learn how to combine multiple filters for more precise data retrieval. For instance, you can combine filters for 'Owners' and 'Status' to track recent changes by specific team members.
* **Using Boolean Operators:** Incorporate operators such as _IS, IS NOT_ for complex searches that require a combination of conditions.

## **Use Case: Filtering for Undocumented Resources**

Filters can be used to identify resources that have not yet been documented in the workspace.

For example, to find resources without descriptions:

1. Click into the **Catalog**.
2. Navigate to the 'Description' metadata column.
3. Select 'Blank' to filter and display resources that lack descriptions.

Next you can apply descriptions in bulk using the [ai-description-editor.md](../resource-and-metadata-management/add-documentation/ai-description-editor.md "mention")!
