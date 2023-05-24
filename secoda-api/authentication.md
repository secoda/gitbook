---
description: >-
  Navigate to your workspace settings on Secoda. Click on the “API” to get a
  list of your API Keys.
---

# Authentication

### **Step 1: Create an API Key**

Navigate to your workspace settings on Secoda. Click on the “API” to get a list of your API Keys.

Click on “Generate New API Key” button and then write down the generated key. Please keep this key somewhere safe and do not share with others. This key will have admin access to your Secoda workspace.

### Step 2: Authenticate Your Requests

To make an authenticated request to your Secoda workspace. Please include an `Authorization` header with your HTTP request with the following format `Bearer <Your API Key>`

### Step 3: Test Your Authentication

Make a request to the Secoda Health Check API endpoint `/healthcheck`. A successful response should look like this.&#x20;

```json
{
    "status": "OK"
}
```

### Request Examples

See below for example requests to the Secoda API.  You must replace `{{base_URL}}` with the [base URL](get-started/) for your workspace, and the Bearer with the API key generated using the instructions above. &#x20;

*   **Curl Example**

    ```bash
    curl '<https://{{base_URL}}/dictionary/terms>' -H 'Authorization: Bearer d736dd50-5d06-4d4f-bc3d-38a67cd46569'
    ```
*   **Javascript Example**

    ```jsx
    axios.get("<https://{{base_URL}}/dictionary/terms>", {
    	headers={
        "Authorization": "Bearer d736dd50-5d06-4d4f-bc3d-38a67cd46569" // replace the key with your own API Key
    	}
    })
    ```
*   **Python Example**

    ```python
    import requests

    requests.get("<https://{{base_URL}}/dictionary/terms>", headers={
        "Authorization": "Bearer d736dd50-5d06-4d4f-bc3d-38a67cd46569" # replace the key with your own API Key
    })
    ```



    {% hint style="info" %}
    Not using Secoda to manage your data documentation yet? Sign up for free [here](https://app.secoda.co) 👈
    {% endhint %}
