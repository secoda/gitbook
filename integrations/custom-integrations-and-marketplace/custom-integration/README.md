---
description: How to build a custom integration in Secoda using a CSV or JSONL file.
---

# CSV and JSONL Custom Integration

{% hint style="info" %}
This is different from our [Import and Export](../../../resource-and-metadata-management/import-and-export-data.md) feature which is meant to edit metadata on existing resources, or bring in new dictionary terms.&#x20;
{% endhint %}

The first step is to create a Custom Integration in Secoda. You can do this through the API, or through the UI. See the steps in the page below.&#x20;

{% content-ref url="create-an-integration.md" %}
[create-an-integration.md](create-an-integration.md)
{% endcontent-ref %}

You can adjust the preferences of your integration in the [Settings](../../integration-settings.md).&#x20;

Now to import your resources, you can create and upload either a CSV, or a JSONL file into Secoda. The files can be uploaded in the UI or using an API.&#x20;

{% content-ref url="import-your-resources/" %}
[import-your-resources](import-your-resources/)
{% endcontent-ref %}

Every time you upload a CSV or JSONL file through this method, it is considered a sync. You can then maintain (edit, delete, document) the resources pulled in from the extraction with the tips and tricks outlined below.&#x20;

{% content-ref url="maintain-your-resources.md" %}
[maintain-your-resources.md](maintain-your-resources.md)
{% endcontent-ref %}
