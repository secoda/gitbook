# Create an Integration

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

This step should only be done once, as once the integration is created, you can use the integration ID to reference it.&#x20;

### Using the UI to Create the Integration

Navigate over to [https://app.secoda.co/integrations](https://app.secoda.co/integrations) and click the New Integration button. Scroll to the bottom right to see the Custom Integration option.&#x20;

<figure><img src="../../.gitbook/assets/screencapture-app-secoda-co-integrations-new-2023-06-09-14_47_01.png" alt="" width="375"><figcaption></figcaption></figure>

You'll then be able to name your integration, and add any associated teams. By default, the integration will be named Untitled, and associate with the General team.&#x20;

<figure><img src="../../.gitbook/assets/Screenshot 2023-06-09 at 2.48.41 PM.png" alt="" width="375"><figcaption></figcaption></figure>

Once you've made the integration, you can alter some settings to determine the behaviour of your integrations. Learn how to do this at the next page.&#x20;
