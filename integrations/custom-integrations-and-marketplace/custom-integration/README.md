---
description: How to build a custom integration in Secoda using a CSV or JSONL file.
---

# File Upload

{% hint style="warning" %}
File Upload is different from the [Import and Export](../../../resource-and-metadata-management/import-and-export-data.md) feature which is meant to edit metadata on existing resources, or bring in new dictionary terms.&#x20;
{% endhint %}

There are three steps to uploading a file as a custom integration in Secoda.&#x20;

1. Create an Integration
2. Prepare your files
3. Upload the resources

### 1. Create an Integration

Navigate over to the Integrations page and click the **Connect Integration** button. Scroll to the bottom to find the **Custom Integrations** option, and select **File Upload**.&#x20;

You'll then be able to name your integration, and add any associated teams. By default, the integration will be named Untitled, and associate with the General team.

You can adjust the preferences of your integration in the [Settings](../../integration-settings.md).&#x20;

#### Using an API Request

Use the Secoda [Integrations API endpoint](https://api.secoda.co/api/schema/redoc/#tag/Integrations/paths/\~1integration\~1integrations/post) to create an integration. Code snippet below.&#x20;

```python
import requests

headers = dict(
    Authorization="Bearer <your-api-token>"
)
integration_type = "custom"

response = requests.post(
    "https://api.secoda.co/integration/integrations/",
    json=dict(type=integration_type, name="My Custom Integration", credentials={}),
    headers=headers
).json()
print("Integration ID", response.get("id"))
```

### 2. Prepare your files

Learn more about the expected format for the CSV or JSONL file.&#x20;

{% content-ref url="create-your-csv.md" %}
[create-your-csv.md](create-your-csv.md)
{% endcontent-ref %}

{% content-ref url="create-your-jsonl-file.md" %}
[create-your-jsonl-file.md](create-your-jsonl-file.md)
{% endcontent-ref %}

### 3. Upload your resources

Under the Import tab, you will see the option to select and upload a CSV or JSONL file. Each upload is considered a sync.

#### Using an API Request

The endpoint for uploading a CSV is [here](https://api.secoda.co/api/schema/redoc/#tag/Integrations/paths/\~1integration\~1integrations\~1%7Bintegration\_id%7D\~1import\_metadata/post). For a JSONL file, you can upload both a `resources.jsonl` and `lineage.jsonl` file in the same request, to the endpoint [here](https://api.secoda.co/api/schema/redoc/#tag/Integrations/paths/\~1integration\~1integrations\~1%7Bintegration\_id%7D\~1import\_jsonl\_metadata/post).

Each request is considered a sync.

{% hint style="info" %}
For some best practices in maintaining your resources for File Upload custom integrations, see [here](maintain-your-resources.md).&#x20;
{% endhint %}
