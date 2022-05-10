---
description: How to manage dbt with the Secoda API
---

# DBT Integration

## Extract From Manifest File

| Endpoint | `https://api.secoda.co/integration/dbt/manifest/`  |
| -------- | -------------------------------------------------- |
| Method   | POST                                               |

*   Sample Response

    ```json
    {
       "message":"Successfully ran extraction for dbt"
    }
    ```
*   Python Example

    ```python
    import requests

    headers = {
        "Authorization": "Bearer <Your Key>"
    }
    response = requests.post(
    	"<https://api.secoda.co/integration/dbt/manifest/>",
    	files={"manifest_file": open("manifest.json", "rb")},
    	data={"integration_id": "km1dhjql3xgxy9p8"},
    	headers=headers
    )
    print(response.json())
    ```
