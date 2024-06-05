---
description: Edit the properties or bring in new dictionary terms through this feature.
---

# Import and Export Resources

## Overview

This guide provides a step-by-step process for exporting and importing metadata using CSV files in Secoda. This allows for bulk editing and updating of metadata to ensure consistency and prevent duplication across your data resources.

{% hint style="info" %}
If your goal is to introduce net new resources from an integration without connecting the integration in the app, you should utilize the  [Custom Integrations](../integrations/custom-integrations-and-marketplace/custom-integration/) feature. If you are looking to edit existing resources, such as dictionary terms, documents, etc., the following instructions will guide you through the process.&#x20;
{% endhint %}

## Video resource

{% embed url="https://www.loom.com/share/8290f98c95ba465c803421d0772f8972" %}

## E**xporting resources from Secoda** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

To export resources from Secoda:

1. **Navigate to Settings:** Go to [Settings](https://app.secoda.co/settings/import) → Import & Export data.
2. **Select Resource Type:** Choose the type of resource you wish to export.&#x20;
3. **Download the Export:** Once the Artifact is prepared as a Bulk export of your resources, click the "Download Artifact" button.

<figure><img src="../.gitbook/assets/Screenshot 2024-06-05 at 12.28.49 PM.png" alt=""><figcaption></figcaption></figure>

Below is an example of the results from exporting your data:

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/image%20(5)%20(1).png" alt=""><figcaption></figcaption></figure>

## Preparing Your CSV for Import

Before importing new or updated metadata into Secoda:

1. **Edit Your CSV:** After exporting, you can edit your descriptions and other properties in CSV format or Google Sheets.
2. **Set Up Your CSV:** Use the exported data as a base, the provided template in the UI, or create your own CSV adhering to the required structure:

**Required Columns:**

* **id:** Leave this blank for new resources.
* **title:** The name of the resource.
* **entity\_type:** Possible values include table, column, dashboard, chart, job, dictionary\_term, document, collection, question, or event.

**Optional Columns:**

* **description:** A brief description of the resource.
* **definition:** Markdown-friendly documentation of the resource.
* **pii:** Governance tag (TRUE or FALSE).
* **verified:** Verified status (TRUE or FALSE).
* **published:** Published status (TRUE or FALSE).
* **collections:** List of associated collection names, e.g., \['Marketing', 'Engineering'].
* **owners:** List of associated owner emails that should correspond to existing users in Secoda, e.g., \['brittany@secoda.co'].
* **tags:** List of associated tag names, e.g., \['production'].
* **custom properties:** If applicable, replace 'property' with the name of your custom property and add values accordingly. Add separate columns for multiple custom properties. Please remove it if you don't plan on adding any custom properties for your resource.

## Importing Updated Metadata into Secoda

1. **Access Import Settings:** Log into Secoda, navigate to Settings > Import & Export.
2. **Upload CSV File:** Click "Select File" under the Import section, choose your prepared CSV file, and click "Upload". Monitor the import process through the displayed logs.

<figure><img src="../.gitbook/assets/Screenshot 2024-06-05 at 12.31.29 PM.png" alt=""><figcaption></figcaption></figure>

## Verifying Imported Properties

After importing, it's crucial to verify that all properties have been correctly updated:

1. **Check Data Resource:** Visit a data resource within Secoda to confirm that the properties reflect the recent imports.
2. **Resolve Issues:** If there are discrepancies or if you encounter issues, please contact support@secoda.co.

By following these steps, you can efficiently manage the metadata of your resources in Secoda, ensuring data integrity and streamlined operations across your organization.

{% hint style="info" %}
Not using Secoda to manage your data documentation yet? Sign up for free [here](http://app.secoda.co/) 👈
{% endhint %}
