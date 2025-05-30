---
description: Custom properties allow you add additional context to resources in Secoda.
---

# Custom Properties

## Overview

Custom properties allow you to enrich the metadata of your resources within Secoda, providing additional context and enhancing organization. This guide outlines the methods to add custom properties to individual resources and in bulk.

## (New) Adding Custom Properties to the catalog

To add a custom property to all resources by resource type, you can follow these steps.

1. Go to Settings > Properties.
2. Click the "Create property" button.
3. Select the label, type, and resource types that you'd like the property to be applied to.
4. Review your property and click "Confirm".

After this is completed, the custom property will appear up in the Catalog table and the pages for the visibility type(s) selected.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/2ed01729-ee98-45cf-91af-ff535b112638.gif" alt=""><figcaption></figcaption></figure>

## Bulk updating (New) Custom Properties

To efficiently update custom properties to multiple resources you can use the **Import CSV** functionality or the **API**:

1. **Import CSV file:** Ensure the custom properties are visible on the table you want to bulk update. Then click "Export page as CSV". This will be your template. Open the CSV export and modify the columns containing custom properties. "String" custom properties can contain up to 255 characters of text. "Select", "User", or "Resource" custom properties must contain an array of (v4) uuids. Then click "Import custom properties from CSV" and select the file you modified.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/fcb195ee-fdf4-4f2f-8b0d-7a96c8e9bb47.png" alt=""><figcaption><p>Export page as CSV</p></figcaption></figure>

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/fbe8be70-1a30-4635-825c-ff45e44798c7.png" alt=""><figcaption><p>Sample columns in CSV file</p></figcaption></figure>

2. **Use the API:** Create a custom script to update the custom properties.

{% content-ref url="broken-reference" %}
[Broken link](broken-reference)
{% endcontent-ref %}

***

## (Legacy) Adding Custom Properties to the properties sidebar

This feature is considered **legacy**, and we recommend adding custom properties to the catalog (above).

1. **Access the Resource:** Navigate to the specific resource (document, table, column, etc.) within Secoda.
2. **Add the Property:** Use the "+ Add Property" button located on the right side panel.
3. **Choose Property Type:** Select from Text, Checkbox, User, Tag, Resource, Date, Number, Select, and Multiselect Property types.
4. **Edit the Property:** Click into the value to edit the Property.
5. **Delete the Property:** Click into the Property type to Delete it.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/f593e100-1e1a-4a70-a78e-0681afd23a03.gif" alt=""><figcaption><p>Creating a Property</p></figcaption></figure>

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/65c7fa9e-d3e7-4959-b08d-c21e99c85b67.gif" alt=""><figcaption><p>Editing &#x26; Deleting a Property</p></figcaption></figure>

***

By following these instructions, you can tailor the metadata within your Secoda environment to meet your specific organizational needs, enhancing both the utility and accessibility of your data resources.

{% hint style="info" %}
Not using Secoda to manage your data documentation yet? Sign up for free [here](http://app.secoda.co/) 👈
{% endhint %}
