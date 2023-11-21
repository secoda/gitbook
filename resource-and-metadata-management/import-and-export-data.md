---
description: Edit the metadata or bring in new dictionary terms through this feature.
---

# Import and Export Metadata



{% hint style="info" %}
If you are hoping to bring in net new resources from an Integration without connecting the integration in the App, you'll need to use the [Custom Integrations](../integrations/custom-integration/) feature. If you are looking to edit existing resources, dictionary terms, documents, etc, you're in the right place!
{% endhint %}

{% embed url="https://www.loom.com/share/8290f98c95ba465c803421d0772f8972" %}

### E**xport metadata from Secoda** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

To export data descriptions out of Secoda, you can go to the [import settings](https://app.secoda.co/settings/import) in **Settings → Import & Export** data. Below is the screenshot for the settings. When exporting you can choose the type of resource you'd like to export. After clicking the export button, an **Artifact** will be prepared with your resources. Once it's prepared click the "Download Artifact" button.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/image%20(13)%20(2).png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/image%20(16)%20(2).png" alt=""><figcaption></figcaption></figure>

Once you export your data , you can view and edit your descriptions in CSV format or Google Sheets and upload the changes to Secoda. Below is an overview of the results from exporting your data:

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/image%20(5)%20(1).png" alt=""><figcaption></figcaption></figure>

Once you are ready to upload your new metadata, you can use the import button to upload your new CSV into Secoda.

### **Importing metadata into Secoda**

If you have set up a documentation tool (Excel, G-Sheet etc.) at your organization, you can migrate your metadata to Secoda following these steps.

1. Prepare your CSV
2. Update metadata in CSV
3. Import metadata to Secoda

#### 1. Prepare your CSV <a href="#h_da2aba5589" id="h_da2aba5589"></a>

You can either export your data from Secoda to a CSV, use the template linked below, or create your own CSV using the guidance provided. The file must be in CSV format.

{% file src="../.gitbook/assets/import.csv" %}
A CSV file with the headings for importing into Secoda.
{% endfile %}

* The file must have the following **required** columns:
  * **id -** Leave this blank if it's a new resource (i.e dictionary term)
  * **title -** The name of the resource
  * **entity\_type** - Can be any of the following - table, column, dashboard, chart, job, dictionary\_term, document, collection, question, or event
* The file can have the following **optional** columns:
  * **description** - This is one-liner description of the resource
  * **definition** - Mark down friendly documentation of the resource
  * **pii** - This is the [Governance](../readme/best-practices/data-governance.md) tag and can be set to TRUE, FALSE
  * **verified -** This is the [Verified](tags/verified-tag.md) tag and can be set to TRUE, FALSE
  * **published -** This is the published status and can be set to TRUE, FALSE
  * **collections -** List of associated collection names, i.e \['Marketing', 'Engineering']
  * **owners** - List of associated owner emails, i.e, \['andrew@secoda.co', 'etai@secoda.co']
  * **tags -** List of associated tag names, i.e, \['production']
  * **property** - This heading is a placeholder for any custom properties you'd like to add to the resource. Please remove it if you don't plan on any custom properties for your resource. To customize it, replace **property** with the name of your custom property and add the values of that property to the relevant rows. If you'd like to add several custom properties, add a new column for each one, with the name of the custom property as the column heading.&#x20;

#### 2. Upload metadata to Secoda <a href="#h_1114a0b4bd" id="h_1114a0b4bd"></a>

Log into [Secoda](https://app.secoda.co) and go into the [import settings](https://app.secoda.co/settings/import) through **Settings > Import & Export.** Click the "Select File" button under the Import section and select your CSV file and click "Upload". The import will start and show logs until it's completed.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/image%20(12)%20(2).png" alt=""><figcaption></figcaption></figure>

#### 3. Verify metadata <a href="#h_47949f1af3" id="h_47949f1af3"></a>

Go to a data resource and confirm that the metadata has been correctly imported. If you have any questions or issues please contact support@secoda.co

{% hint style="info" %}
Not using Secoda to manage your data documentation yet? Sign up for free [here](http://app.secoda.co/) 👈
{% endhint %}
