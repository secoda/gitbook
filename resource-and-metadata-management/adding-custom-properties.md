---
description: Custom properties allow you add additional context to resources in Secoda.
---

# Custom Properties

## Overview

Custom properties allow you to enrich the metadata of your resources within Secoda, providing additional context and enhancing organization. This guide outlines the methods to add custom properties to individual resources and in bulk.

## Adding Custom Properties to all resources

To add a custom property to all resources by resource type, you can follow these steps.&#x20;

1. Go to Settings > Properties.
2. Click the "Create property" button.&#x20;
3. Select the label, type, and resource types that you'd like the property to be applied to.
4. Review your property and click "Confirm".

After this is completed, the custom property will show up in the Catalog table and the pages for all of the resources of the resource type(s) selected.&#x20;

<figure><img src="../.gitbook/assets/Kapture 2024-10-22 at 18.00.31.gif" alt=""><figcaption></figcaption></figure>

## Adding Custom Properties to individual resources

**Via Side Panel:**

1. **Access the Resource:** Navigate to the specific resource (document, table, column, etc.) within Secoda.
2. **Add the Property:** Use the "+ Add Property" button located on the right side panel.
3. **Choose Property Type:** Select from Text, Checkbox, User, Tag, Resource, Date, Number, Select, and Multiselect Property types.
4. **Edit the Property:** Click into the value to edit the Property.
5. **Delete the Property:** Click into the Property type to Delete it.

<figure><img src="../.gitbook/assets/Kapture 2024-06-05 at 13.58.01.gif" alt=""><figcaption><p>Creating a Property</p></figcaption></figure>

<figure><img src="../.gitbook/assets/Kapture 2024-06-05 at 13.58.39 (1).gif" alt=""><figcaption><p>Editing &#x26; Deleting a Property</p></figcaption></figure>

**For all Columns in a Specific Table:**

1. **Navigate to the Table:** Go to the table where you want to add properties to columns.
2. **Add the Property:** Use the designated button as shown in the image below to add properties directly to all columns within the table. This will create additional columns in the table's catalog, similar to the Description and Type columns.

<figure><img src="../.gitbook/assets/Screenshot 2024-07-02 at 4.32.04 PM.png" alt=""><figcaption><p>Custom Property on Table Columns</p></figcaption></figure>

## Bulk Update of Custom Properties

To efficiently update custom properties to multiple resources you can use the **Import & Export** functionality or the **API**:

1. **Use Import & Export Feature:** Prepare a CSV for importing metadata into Secoda. Include an additional column for each custom property you wish to add. This method is ideal for updating properties across various resources simultaneously.

{% content-ref url="import-and-export-data.md" %}
[import-and-export-data.md](import-and-export-data.md)
{% endcontent-ref %}

2. **Use the API:** Create a python script that updates the custom&#x20;

{% content-ref url="../secoda-api.md" %}
[secoda-api.md](../secoda-api.md)
{% endcontent-ref %}



By following these instructions, you can tailor the metadata within your Secoda environment to meet your specific organizational needs, enhancing both the utility and accessibility of your data resources.



{% hint style="info" %}
Not using Secoda to manage your data documentation yet? Sign up for free [here](http://app.secoda.co/) 👈
{% endhint %}
