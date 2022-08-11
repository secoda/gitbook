---
description: How to manage users with the Secoda API
---

# Managing invitations

## Invite a New User

| Endpoint                 | `https://api.secoda.co/user/invite/` |
| ------------------------ | ------------------------------------ |
| Method                   | POST                                 |
| Accepted Body Parameters | email, role                          |

{% hint style="info" %}
The **Endpoint** field for self-hosted instances is `<host`\_`url>/api/v1/dictionary/invite/`\
``\
``For example, https://secoda.company.com/api/v1/user/invite/
{% endhint %}

*   Sample Response

    ```json
    {
       "msg":"Invitation sent to kash@secoda.co"
    }
    ```
*   Python Example

    ```python
    import requests

    headers = {
        "Authorization": "Bearer <Your Key>"
    }
    response = requests.post(
    	"<https://api.secoda.co/user/invite/>",
    	headers=headers,
    	json={
    		'email': 'kash@secoda.co',
    		'role': 'Admin'
    	}
    )
    print(response.json())
    ```



    {% hint style="info" %}
    Not using Secoda to manage your data documentation yet? Sign up for free [here](https://app.secoda.co) 👈
    {% endhint %}
