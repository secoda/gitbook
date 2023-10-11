---
description: >-
  To export data descriptions out of Secoda, you can go to Settings → Data →
  Export data. Below is the screenshot for the settings:
---

# Import and Export Metadata

### E**xport metadata from Secoda** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

To export data descriptions out of Secoda, you can go to the [import settings](https://app.secoda.co/settings/import) in **Settings → Import & Export** data. Below is the screenshot for the settings. When exporting you can choose the type of resource you'd like to export. After clicking the export button, an **Artifact** will be prepared with your resources. Once it's prepared click the "Download Artifact" button.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/image%20(13)%20(2).png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/image%20(16)%20(2).png" alt=""><figcaption></figcaption></figure>

Once you export your data , you can view and edit your descriptions in CSV format or Google Sheets and upload the changes to Secoda. Below is an overview of the results from exporting your data:

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/image%20(5)%20(1).png" alt=""><figcaption></figcaption></figure>

Once you are ready to upload your new metadata, you can use the import button to upload your new CSV into Secoda.

### **Importing metadata into Secoda**

If you have set up a documentation tool (Excel, G-Sheet etc.) at your organization, you can migrate your descriptions to Secoda following these steps.

1. Prepare your CSV
2. Update metadata in CSV
3. Import metadata to Secoda

#### 1. Prepare your CSV <a href="#h_da2aba5589" id="h_da2aba5589"></a>

You can either export your data from Secoda to a csv, or start from scratch. The only requirements for importing are:

1. The file format must be csv
2. Download the csv template and follow the instructions below

{% file src="https://secoda-public-media-assets.s3.amazonaws.com/36b84e5e-13ea-41ae-84fd-878b308d66e4.csv" %}
CSV template with filled in example in row 1
{% endfile %}

* The file must have the following **required** columns:&#x20;
  * **id -** Leave this blank if it's a new resource (i.e dictionary term)
  * **title -** The name of the resource
  * **entity\_type** - Can be any of the following - table, column, dashboard, chart, job, dictionary\_term, document, collection, question, or event
* The file can have the following **optional** columns:
  * **description** - This is one-liner description of the resource
  * **definition** - This is for longer readmes to add additional context, that has markdown capabilities
  * **pii** - This is the PII tag and can be TRUE, FALSE, or left blank
  * **verified -** This is the Verified tag and can be TRUE, FALSE, or left blank
  * **published -** This is the status and can be TRUE, FALSE, or left blank
  * **collections -** List of associated collection names, i.e \['Marketing', 'Engineering']
  * **owners** - List of associated owner emails, i.e, \['andrew@secoda.co', 'etai@secoda.co']
  * **tags -** List of associated tag names, i.e, \['production']
  * **property -** Where "property" can be any custom property you'd like to add on a resource, keep in same \['\_\_\_\_'] format

#### 2. Upload metadata to Secoda <a href="#h_1114a0b4bd" id="h_1114a0b4bd"></a>

Log into [Secoda](https://app.secoda.co) and go into the [import settings](https://app.secoda.co/settings/import) through **Settings > Import & Export.** Click the "Select File" button under the Import section and select your csv file and click "Upload". The import will start and show logs until it's completed.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/image%20(12)%20(2).png" alt=""><figcaption></figcaption></figure>

#### 3. Verify metadata <a href="#h_47949f1af3" id="h_47949f1af3"></a>

Go to a data resource and confirm that the metadata has been correctly imported. If you have any questions or issues please contact support@secoda.co

{% hint style="info" %}
Not using Secoda to manage your data documentation yet? Sign up for free [here](http://app.secoda.co/) 👈
{% endhint %}
