---
description: >-
  To export data descriptions out of Secoda, you can go to Settings → Data →
  Export data. Below is the screenshot for the settings:
---

# Import & Export Metadata

### E**xport metadata from Secoda** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

To export data descriptions out of Secoda, you can go to the [import settings](https://app.secoda.co/settings/import) in **Settings → Import & Export** data. Below is the screenshot for the settings. When exporting you can choose the type of resource you'd like to export. After clicking the export button, an **Artifact** will be prepared with your resources. Once it's prepared click the "Download Artifact" button.

<figure><img src="../../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure>

Once you export your data , you can view and edit your descriptions in CSV format or Google Sheets and upload the changes to Secoda. Below is an overview of the results from exporting your data:

<figure><img src="../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

Once you are ready to upload your new metadata, you can use the import button to upload your new CSV into Secoda.

### **Importing metadata into Secoda**

If you have set up a documentation tool at your organization you can migrate your descriptions to Secoda following these steps.

1. Export metadat to a CSV
2. Update metadata in CSV
3. Import metadata to Secoda

#### 1. Export descriptions to a CSV <a href="#h_da2aba5589" id="h_da2aba5589"></a>

You can either export your data from Secoda to a csv, or start from scratch. The only requirements for importing are:

1. The file format must be csv
2. The file must have the following **required** columns:
   * **id -** Leave blank if it's a new resource, i.e dictionary term
   * **title -** The name of the resource
   * **entity\_type** - Can be table, column, dashboard, chart, job, dictionary\_term, document, collection, question, or event
3. The file can have the following **optional** columns:
   * **description**
   * **definition** - This is markdown documentation for the resource
   * **pii** - This is the PII tag and can be TRUE, FALSE, or blank
   * **verified -** This is the Verified tag and can be TRUE, FALSE, or blank
   * **published -** This is the status and can be TRUE, FALSE, or blank
   * **collections -** List of associated collection names, i.e \["Marketing", "Engineering"]
   * **owners** - List of associated owner emails, i.e, \["andrew@secoda.co", "etai@secoda.co"]
   * **tags -** List of associated tag names, i.e, \["production"]
   * **property -** Where "property" can be any custom property you'd like to add on a resource

#### 2. Upload metadata to Secoda <a href="#h_1114a0b4bd" id="h_1114a0b4bd"></a>

Log into [Secoda](https://app.secoda.co) and go into the [import settings](https://app.secoda.co/settings/import) through **Settings > Import & Export.** Click the "Select File" button under the Import section and select your csv file and click "Upload". The import will start and show logs until it's completed.

<figure><img src="../../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

#### 3. Verify metadata <a href="#h_47949f1af3" id="h_47949f1af3"></a>

Go to a data resource and confirm that the metadata has been correctly imported. If you have any questions or issues please contact support@secoda.co

{% hint style="info" %}
Not using Secoda to manage your data documentation yet? Sign up for free [here](http://app.secoda.co/) 👈
{% endhint %}
