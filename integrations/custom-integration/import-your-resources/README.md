# Import your Resources

Before being able to import your resources, you'll need to generate them in the correct format. See below for some tips and tricks on how to do this!

{% content-ref url="create-your-csv.md" %}
[create-your-csv.md](create-your-csv.md)
{% endcontent-ref %}

{% content-ref url="create-your-jsonl-file.md" %}
[create-your-jsonl-file.md](create-your-jsonl-file.md)
{% endcontent-ref %}

You can upload these resources into Secoda through the UI, or through an API request.

### Upload through the UI

Navigate to the Integrations page, click on Custom Integration, and you'll see the ability to select and upload the relevant files.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/6b45de04-6904-4738-bd11-086b6b1b8dea.png" alt=""><figcaption></figcaption></figure>

### Upload through the API

Alternatively, you can upload the file to Secoda by making a request to the following endpoints.

For the CSV, you can send the file to:

`https://api.secoda.co/integration/integrations/<integration-id>/import_metadata/`

For the JSONL, you can send the file(s) to:

`https://api.secoda.co/integration/integrations/<integration-id>/import_jsonl_metadata`\
\
This endpoint will accept both a `resources.jsonl` and `lineage.jsonl` file.&#x20;

Now if you open Secoda and navigate to the integration page, you should see an extraction running for your custom integration.
