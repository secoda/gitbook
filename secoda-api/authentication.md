---
description: >-
  Navigate to your workspace settings on Secoda. Click on the “API” to get a
  list of your API Keys.
---

# Authentication

## **Step 1: Create an API Key**

Navigate to your workspace settings on Secoda. Click on the “API” to get a list of your API Keys.

Click on “Generate New API Key” button and then write down the generated key. Please keep this key somewhere safe and do not share with others. This key will have admin access to your Secoda workspace.

#### Step 2: Authenticate Your Requests

To make an authenticated request to your Secoda workspace. Please include an `Authorization` header with your HTTP request with the following format `Bearer <Your API Key>`

*   **Curl Example**

    ```bash
    curl '<https://public-api.secoda.co/dictionary/terms>' -H 'Authorization: Bearer d736dd50-5d06-4d4f-bc3d-38a67cd46569'
    ```
*   **Javascript Example**

    ```jsx
    axios.get("<https://public-api.secoda.co/dictionary/terms>", {
    	headers={
        "Authorization": "Bearer d736dd50-5d06-4d4f-bc3d-38a67cd46569" // replace the key with your own API Key
    	}
    })
    ```
*   **Python Example**

    ```python
    import requests

    requests.get("<https://public-api.secoda.co/dictionary/terms>", headers={
        "Authorization": "Bearer d736dd50-5d06-4d4f-bc3d-38a67cd46569" # replace the key with your own API Key
    })
    ```



    {% hint style="info" %}
    Not using Secoda to manage your data documentation yet? Sign up for free [here](https://app.secoda.co) 👈
    {% endhint %}
