# Upload your CSV

There are two ways to upload your CSV into Secoda, through an API request and through the UI.&#x20;

### Upload the CSV through an API Request

Upload the file to Secoda by making a request to the `https://api.secoda.co/integration/integrations/<integration-id>/import_metadata/`

```python
import requests

integration_id = "integration id from step 1"
headers = dict(
    Authorization="Bearer <your-api-token>"
)

requests.post(
    f"https://api.secoda.co/integration/integrations/{integration_id}/import_metadata/",
    files=dict(file=open("dump.csv", "rb")),
    headers=headers
)
```

Now if you open Secoda and navigate to the integration page, you should see an extraction running for your custom integration.

### Upload the CSV through the UI

Navigate to the Import tab from the Integration page. Click on Import to upload your CSV.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/Screenshot%202023-06-09%20at%203.18.16%20PM.png" alt=""><figcaption></figcaption></figure>

Success! Your first extraction has been completed. Now it's time to maintain your resources. Learn some tips and tricks on the next page!
