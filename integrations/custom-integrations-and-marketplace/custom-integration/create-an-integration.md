# Create a Custom Integration

### Using an API Request to Create the Integration

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

This step should only be done once, as once the integration is created, you can use the integration ID to reference it.

### Using the UI to Create the Integration

Navigate over to [https://app.secoda.co/integrations](https://app.secoda.co/integrations) and click the New Integration button. Scroll to the bottom right to see the Custom Integration option.

![](https://secoda-public-media-assets.s3.amazonaws.com/screencapture-app-secoda-co-integrations-new-2023-06-09-14\_47\_01.png)

You'll then be able to name your integration, and add any associated teams. By default, the integration will be named Untitled, and associate with the General team.

![](https://secoda-public-media-assets.s3.amazonaws.com/Screenshot%202023-06-09%20at%202.48.41%20PM.png)

Once you've made the integration, you can alter some settings to determine the behaviour of your integrations. You can learn more about this in the [Integration Settings](../../integration-settings.md) page.&#x20;
