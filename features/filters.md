---
description: >-
  Streamline your data discovery by applying tailored filters to efficiently
  navigate and manage resources in Secoda.
---

# Filters

## **Overview**&#x20;

Filters are powerful tools in Secoda that enhance your ability to efficiently explore and access metadata. This guide explains how to set up and effectively use filters in both the Catalog and Search functions.

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

Consider saving your filters with [views.md](views.md "mention") to streamline your workflow, particularly if you frequently revisit specific datasets. Saved views can be quickly accessed, reducing the time spent reapplying the same filters.

### **Advanced Filtering Capabilities**

* **Nested Search in Filters:** We've added nested search capabilities to filters. For instance, you can directly search for a user's name without having to navigate through "Owners" first. This makes it quicker and more intuitive to find specific entries.
* **Keyboard Shortcuts for Filters:** To improve efficiency, you can now use the keyboard shortcut '(f)' to open filters and navigate through them with ease.
* **Combining Filters:** Combine multiple filters for more precise data retrieval. For instance, you can combine filters for 'Owners' and 'Status' to track recent changes by specific team members.
* **Using Boolean Operators:** Incorporate operators such as _IS, IS NOT_ for complex searches that require a combination of conditions.

## **Applying Filters in Catalog**

1. **Access Filters:**
   * Go to any section where Filters can be applied, such as the Catalog, Collections, Metrics, Dictionary, Documents, or Questions. For this example, we'll use the **Catalog**.
   * Click on the column header that corresponds to the metadata type you want to filter (e.g., Integration, Type, Owners).
2. **View Filtering Options:**
   * Upon clicking the column header, a menu will appear offering several actions:
     * **Sort Ascending/Descending:** Order the metadata based on the selected column.
     * **Add Filter:** Customize your view by selecting specific criteria. This option is particularly useful for narrowing down your data visibility according to specific requirements.
     * **Hide Column:** Remove the column from view if it's not relevant to your current analysis.
3. **Apply Filters:**
   * Select ‘Add Filter’ and choose the desired criteria from the list to refine your Catalog view.

## **Use Case: Filtering for Undocumented Resources**

Filters can be used to identify resources that have not yet been documented in the workspace.

For example, to find resources without descriptions:

1. Click into the **Catalog**.
2. Navigate to the 'Description' metadata column.
3. Select 'Blank' to filter and display resources that lack descriptions.

Next you can apply descriptions in bulk using the [ai-description-editor.md](../resource-and-metadata-management/add-documentation/ai-description-editor.md "mention")!
