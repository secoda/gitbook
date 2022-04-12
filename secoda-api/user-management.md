# User Management

#### Invite a New User

| Endpoint                 | [https://api.secoda.co/user/invite](https://api.secoda.co/user/invite) |
| ------------------------ | ---------------------------------------------------------------------- |
| Method                   | POST                                                                   |
| Accepted Body Parameters | email, role                                                            |
|                          |                                                                        |

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
