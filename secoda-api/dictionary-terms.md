---
description: How to manage dictionary terms with the Secoda API
---

# Dictionary Terms

## List All Dictionary Terms

| Endpoint | https://api.secoda.co/dictionary/ |
| -------- | --------------------------------- |
| Method   | GET                               |

*   Sample Response

    ```json
    {
       "page":1,
       "results":[
          {
             "id":"0krl0y8cvt92uvo2",
             "neo4j_id":"0krl0y8cvt92uvo2",
             "created_at":"2022-01-09T22:16:49Z",
             "updated_at":"2022-01-09T22:16:49Z",
             "definition":"This is the definition of [Google](<https://google.com>)",
             "sql":"SELECT * FROM tickets.users",
             "owner":"kash@secoda.co",
             "tags":[
                
             ],
             "related_tables":[
                
             ],
             "related_dashboards":[
                
             ],
             "badges":[
                
             ]
          },
          {
             "id":"term_7o7y2s75ktirezg6_payment_count",
             "neo4j_id":"term_7o7y2s75ktirezg6_payment_count",
             "created_at":"2022-01-09T03:05:04Z",
             "updated_at":"2022-01-09T03:05:04Z",
             "definition":"The number of payments",
             "sql":"payment_id",
             "owner":"None",
             "tags":[
                
             ],
             "related_tables":[
                
             ],
             "related_dashboards":[
                
             ],
             "badges":[
                
             ]
          },
          {
             "id":"9d41j5f0gfp5298f",
             "neo4j_id":"9d41j5f0gfp5298f",
             "created_at":"2021-12-10T18:27:11Z",
             "updated_at":"2021-12-10T18:27:11Z",
             "definition":"% of users that use a feature",
             "sql":"",
             "owner":"kash@secoda.co",
             "tags":[
                "ck7mwwfea59bbn7r"
             ],
             "related_tables":[
                
             ],
             "related_dashboards":[
                
             ],
             "badges":[
                {
                   "category":"status",
                   "badge_name":"published"
                }
             ]
          },
          {
             "id":"797bm69tm3dd16lh",
             "neo4j_id":"797bm69tm3dd16lh",
             "created_at":"2021-12-10T18:25:45Z",
             "updated_at":"2021-12-10T18:25:45Z",
             "definition":"\\\\# of workspaces that connect data / \\\\# of workspaces",
             "sql":"SELET * FROM activation_rate",
             "owner":"None",
             "tags":[
                
             ],
             "related_tables":[
                
             ],
             "related_dashboards":[
                
             ],
             "badges":[
                {
                   "category":"status",
                   "badge_name":"published"
                }
             ]
          },
          {
             "id":"nponkba2gi2l7ntb",
             "neo4j_id":"nponkba2gi2l7ntb",
             "created_at":"2021-12-01T05:12:38Z",
             "updated_at":"2021-12-01T05:12:38Z",
             "definition":"This is the definition of **active users**",
             "sql":"SELECT * FROM active_users",
             "owner":"None",
             "tags":[
                
             ],
             "related_tables":[
                
             ],
             "related_dashboards":[
                
             ],
             "badges":[
                {
                   "category":"status",
                   "badge_name":"published"
                }
             ]
          },
          {
             "id":"ktdi7s908j2l6hti",
             "neo4j_id":"ktdi7s908j2l6hti",
             "created_at":"2021-12-15T14:55:14Z",
             "updated_at":"2021-12-15T14:55:14Z",
             "definition":"This is how we calculate MRR and it is **important** to Secoda",
             "sql":"SELECT * FROM tickets.user",
             "owner":"andrew@secoda.co",
             "tags":[
                "39x8pqpw0pi92wh6",
                "2w1dot2hn6ksmskj"
             ],
             "related_tables":[
                
             ],
             "related_dashboards":[
                
             ],
             "badges":[
                {
                   "category":"status",
                   "badge_name":"draft"
                }
             ]
          }
       ]
    }
    ```
*   Python Example

    ```python
    import requests

    headers = {
        "Authorization": "Bearer <Your Key>"
    }
    response = requests.get(
    	"<https://api.secoda.co/dictionary>",
    	headers=headers
    )
    print(response.json())
    ```

***

### Create a New Dictionary Term

| Endpoint                 | [https://api.secoda.co/dictionary/](https://api.secoda.co/dictionary/) |
| ------------------------ | ---------------------------------------------------------------------- |
| Method                   | POST                                                                   |
| Accepted Body Parameters | name, definition, sql, owner                                           |

*   Sample Response

    ```json
    {
       "msg":"Successfully created dictionary term"
    }
    ```
*   Python Example

    ```python
    import requests

    headers = {
        "Authorization": "Bearer <Your Key>"
    }
    response = requests.post(
    	"<https://api.secoda.co/dictionary/>",
    	headers=headers,
    	json={
    		'name': 'Get Users'
    		'definition': 'This is the definition of [Google](<https://google.com>)',
    		'sql': 'SELECT * FROM tickets.users',
    		'owner': "kash@secoda.co"
    	}
    )
    print(response.json())
    ```

***

### Get Specific Dictionary Term

| Endpoint | [https://api.secoda.co/dictionary/](https://api.secoda.co/dictionary/)<:id> |
| -------- | --------------------------------------------------------------------------- |
| Method   | GET                                                                         |

*   Sample Response

    ```json
    {
       "id":"0krl0y8cvt92uvo2",
       "neo4j_id":"0krl0y8cvt92uvo2",
       "created_at":"2022-01-09T22:16:49Z",
       "updated_at":"2022-01-09T22:16:49Z",
       "tags":[
          
       ],
       "definition":"This is the definition of [Google](<https://google.com>)",
       "sql":"SELECT * FROM tickets.users",
       "owner":"kash@secoda.co",
       "related_tables":[
          
       ],
       "related_dashboards":[
          
       ],
       "badges":[
          
       ]
    }
    ```
*   Python Example

    ```python
    import requests

    headers = {
        "Authorization": "Bearer <Your Key>"
    }
    response = requests.get(
    	"<https://api.secoda.co/dictionary/0krl0y8cvt92uvo2>",
    	headers=headers
    )
    print(response.json())
    ```

***

### Update Dictionary Term

| Endpoint                 | [https://api.secoda.co/dictionary/](https://api.secoda.co/dictionary/)<:id> |
| ------------------------ | --------------------------------------------------------------------------- |
| Method                   | PUT                                                                         |
| Accepted Body Parameters | name, definition, sql, owner                                                |

*   Sample Response

    ```json
    {
       "msg":"Successfully updated dictionary term"
    }
    ```
*   Python Example

    ```python
    import requests

    headers = {
        "Authorization": "Bearer <Your Key>"
    }
    response = requests.put(
    	"<https://api.secoda.co/dictionary/0krl0y8cvt92uvo2>",
    	headers=headers,
    	json={"name": "New Name"}
    )
    print(response.json())
    ```

***

### Delete Dictionary Term

| Endpoint | [https://api.secoda.co/dictionary/](https://api.secoda.co/dictionary/)<:id> |
| -------- | --------------------------------------------------------------------------- |
| Method   | DELETE                                                                      |

*   Sample Response

    ```json
    ''
    ```
*   Python Example

    ```python
    import requests

    headers = {
        "Authorization": "Bearer <Your Key>"
    }
    response = requests.delete(
    	"<https://api.secoda.co/0krl0y8cvt92uvo2>",
    	headers=headers,
    )
    print(response.json())
    ```

***
