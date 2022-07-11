---
description: How to manage collections with the Secoda API
---

# Collections

## List All Collections

| Endpoint | https://api.secoda.co/tag/ |
| -------- | -------------------------- |
| Method   | GET                        |

*   Sample Response

    ```json
    {
       "page":1,
       "results":[
          {
             "id":"u3qnn6xe9jcuo6zk",
             "neo4j_id":"u3qnn6xe9jcuo6zk",
             "created_at":"None",
             "updated_at":"None",
             "name":"test2",
             "icon":"None",
             "description":"test3",
             "count":0,
             "jobs":[
                
             ],
             "tables":[
                
             ],
             "dictionary_terms":[
                
             ],
             "badges":[
                
             ],
             "requests":[
                
             ]
          },
          {
             "id":"2w1dot2hn6ksmskj",
             "neo4j_id":"2w1dot2hn6ksmskj",
             "created_at":"None",
             "updated_at":"None",
             "name":"AWS",
             "icon":"🖥️",
             "description":"Resources associated with Amazon Web Services",
             "count":12,
             "jobs":[
                
             ],
             "tables":[
                
             ],
             "dictionary_terms":[
                
             ],
             "badges":[
                {
                   "category":"status",
                   "badge_name":"None",
                   "name":"draft"
                }
             ],
             "requests":[
                
             ]
          },
          {
             "id":"39x8pqpw0pi92wh6",
             "neo4j_id":"39x8pqpw0pi92wh6",
             "created_at":"None",
             "updated_at":"None",
             "name":"Sales",
             "icon":"💰",
             "description":"None",
             "count":3,
             "jobs":[
                
             ],
             "tables":[
                
             ],
             "dictionary_terms":[
                
             ],
             "badges":[
                {
                   "category":"status",
                   "badge_name":"None",
                   "name":"published"
                }
             ],
             "requests":[
                
             ]
          },
          {
             "id":"ck7mwwfea59bbn7r",
             "neo4j_id":"ck7mwwfea59bbn7r",
             "created_at":"None",
             "updated_at":"None",
             "name":"Marketing",
             "icon":"📣",
             "description":"None",
             "count":7,
             "jobs":[
                
             ],
             "tables":[
                
             ],
             "dictionary_terms":[
                
             ],
             "badges":[
                {
                   "category":"status",
                   "badge_name":"None",
                   "name":"published"
                }
             ],
             "requests":[
                
             ]
          },
          {
             "id":"3xqw7edwbro7m571",
             "neo4j_id":"3xqw7edwbro7m571",
             "created_at":"None",
             "updated_at":"None",
             "name":"Engineering",
             "icon":"💻",
             "description":"This is the engineering collection",
             "count":9,
             "jobs":[
                
             ],
             "tables":[
                
             ],
             "dictionary_terms":[
                
             ],
             "badges":[
                {
                   "category":"status",
                   "badge_name":"None",
                   "name":"draft"
                }
             ],
             "requests":[
                
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
    	"<https://api.secoda.co/tag/>",
    	headers=headers
    )
    print(response.json())
    ```

***

### Get Specific Collection

| Endpoint | [https://api.secoda.co/tag/](https://api.secoda.co/tag/)<:id> |
| -------- | ------------------------------------------------------------- |
| Method   | GET                                                           |

*   Sample Response

    ```json
    {
       "id":"u3qnn6xe9jcuo6zk",
       "neo4j_id":"u3qnn6xe9jcuo6zk",
       "created_at":"None",
       "updated_at":"None",
       "name":"test",
       "icon":"None",
       "description":"None",
       "count":0,
       "jobs":[
          
       ],
       "tables":[
          
       ],
       "dictionary_terms":[
          
       ],
       "badges":[
          
       ],
       "requests":[
          
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
    	"<https://api.secoda.co/tag/0krl0y8cvt92uvo2>",
    	headers=headers
    )
    print(response.json())
    ```

***

### Update Collection

| Endpoint                 | [https://api.secoda.co/tag/](https://api.secoda.co/tag/)<:id> |
| ------------------------ | ------------------------------------------------------------- |
| Method                   | PUT                                                           |
| Accepted Body Parameters | name, description                                             |

*   Sample Response

    ```json
    {
       "msg":"Tag updated"
    }
    ```
*   Python Example

    ```python
    import requests

    headers = {
        "Authorization": "Bearer <Your Key>"
    }
    response = requests.put(
    	"<https://api.secoda.co/tag/0krl0y8cvt92uvo2>",
    	headers=headers,
    	json={"name": "New Name"}
    )
    print(response.json())
    ```

***

### Delete Collection

| Endpoint | [https://api.secoda.co/tag/](https://api.secoda.co/tag/)<:id> |
| -------- | ------------------------------------------------------------- |
| Method   | DELETE                                                        |

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
    	"<https://api.secoda.co/tag/0krl0y8cvt92uvo2>",
    	headers=headers,
    )
    print(response.json())
    ```
