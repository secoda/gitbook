---
description: How to manage tables with the Secoda API
---

# Tables

## List All Tables

| Endpoint | `https://api.secoda.co/table/` |
| -------- | ------------------------------ |
| Method   | GET                            |

*   Sample Response

    ```json
    {
       "page":1,
       "results":[
          {
             "id":"7o7y2s75ktirezg6__bigquery__secoda-web__dbt_amcewen__customers",
             "neo4j_id":"7o7y2s75ktirezg6~bigquery://secoda-web.dbt_amcewen/customers",
             "created_at":"None",
             "updated_at":"None",
             "tags":[
                
             ],
             "name":"customers",
             "schema":"dbt_amcewen",
             "cluster":"secoda-web",
             "database":"bigquery",
             "owners":"None",
    				 "description": "Description of table",
             "columns":[
                
             ],
             "queries":"None"
          },
          {
             "id":"7o7y2s75ktirezg6__bigquery__secoda-web__dbt_amcewen__my_first_dbt_model",
             "neo4j_id":"7o7y2s75ktirezg6~bigquery://secoda-web.dbt_amcewen/my_first_dbt_model",
             "created_at":"None",
             "updated_at":"None",
             "tags":[
                
             ],
             "name":"my_first_dbt_model",
             "schema":"dbt_amcewen",
             "cluster":"secoda-web",
             "database":"bigquery",
             "owners":"None",
    				 "description": "Description of table",
             "columns":[
                
             ],
             "queries":"None"
          },
          {
             "id":"7o7y2s75ktirezg6__bigquery__secoda-web__dbt_amcewen__my_second_dbt_model",
             "neo4j_id":"7o7y2s75ktirezg6~bigquery://secoda-web.dbt_amcewen/my_second_dbt_model",
             "created_at":"None",
             "updated_at":"None",
             "tags":[
                
             ],
             "name":"my_second_dbt_model",
             "schema":"dbt_amcewen",
             "cluster":"secoda-web",
             "database":"bigquery",
             "owners":"None",
    				 "description": "Description of table",
             "columns":[
                
             ],
             "queries":"None"
          },
          {
             "id":"7o7y2s75ktirezg6__bigquery__secoda-web__dbt_amcewen__stg_customers",
             "neo4j_id":"7o7y2s75ktirezg6~bigquery://secoda-web.dbt_amcewen/stg_customers",
             "created_at":"None",
             "updated_at":"None",
             "tags":[
                
             ],
             "name":"stg_customers",
             "schema":"dbt_amcewen",
             "cluster":"secoda-web",
             "database":"bigquery",
             "owners":"None",
    				 "description": "Description of table",
             "columns":[
                
             ],
             "queries":"None"
          },
          {
             "id":"7o7y2s75ktirezg6__bigquery__secoda-web__dbt_amcewen__stg_orders",
             "neo4j_id":"7o7y2s75ktirezg6~bigquery://secoda-web.dbt_amcewen/stg_orders",
             "created_at":"None",
             "updated_at":"None",
             "tags":[
                
             ],
             "name":"stg_orders",
             "schema":"dbt_amcewen",
             "cluster":"secoda-web",
             "database":"bigquery",
             "owners":"None",
    				 "description": "Description of table",
             "columns":[
                
             ],
             "queries":"None"
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
    	"<https://api.secoda.co/table/>",
    	headers=headers
    )
    print(response.json())
    ```

### Get Specific Table

| Endpoint | [https://api.secoda.co/table/](https://api.secoda.co/table/)<:id> |
| -------- | ----------------------------------------------------------------- |
| Method   | GET                                                               |

*   Sample Response

    ```json
    {
       "id":"7o7y2s75ktirezg6__bigquery__secoda-web__dbt_amcewen__customers",
       "neo4j_id":"7o7y2s75ktirezg6~bigquery://secoda-web.dbt_amcewen/customers",
       "created_at":"None",
       "updated_at":"None",
       "tags":[
          "7o7y2s75ktirezg6~dbt_tag"
       ],
       "name":"customers",
       "schema":"dbt_amcewen",
       "cluster":"secoda-web",
       "database":"bigquery",
       "owners":"None",
    	 "description": "Description of table",
       "columns":[
          "customer_id",
          "first_name",
          "last_name",
          "first_order_date",
          "most_recent_order_date",
          "number_of_orders"
       ],
       "queries":[
          {
             "description":"None",
             "query_text":"create or replace table `secoda-web`.`dbt_amcewen`.`customers`\\n\\n\\n  OPTIONS()\\n  as (\\n    with customers as (\\n\\n    select * from `secoda-web`.`dbt_amcewen`.`stg_customers`\\n\\n),\\n\\norders as (\\n\\n    select * from `secoda-web`.`dbt_amcewen`.`stg_orders`\\n\\n),\\n\\ncustomer_orders as (\\n\\n    select\\n        customer_id,\\n\\n        min(order_date) as first_order_date,\\n        max(order_date) as most_recent_order_date,\\n        count(order_id) as number_of_orders\\n\\n    from orders\\n\\n    group by 1\\n\\n),\\n\\n\\nfinal as (\\n\\n    select\\n        customers.customer_id,\\n        customers.first_name,\\n        customers.last_name,\\n        customer_orders.first_order_date,\\n        customer_orders.most_recent_order_date,\\n        coalesce(customer_orders.number_of_orders, 0) as number_of_orders\\n\\n    from customers\\n\\n    left join customer_orders using (customer_id)\\n\\n)\\n\\nselect * from final\\n  );",
             "frequency":0,
             "last_updated_timestamp":"None",
             "key":""
          },
          {
             "description":"None",
             "query_text":"SELECT * FROM dbt_amcewen.customers",
             "frequency":0,
             "last_updated_timestamp":"None",
             "key":""
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
    	"<https://api.secoda.co/table/7o7y2s75ktirezg6__bigquery__secoda-web__dbt_amcewen__customers>",
    	headers=headers
    )
    print(response.json())
    ```

***

### Update Table

| Endpoint                 | [https://api.secoda.co/table/](https://api.secoda.co/table/)<:id> |
| ------------------------ | ----------------------------------------------------------------- |
| Method                   | PUT                                                               |
| Accepted Body Parameters | owners, tags                                                      |

*   Sample Response

    ```json
    {
       "msg":"Successfully updated table"
    }
    ```
*   Python Example

    ```python
    import requests

    headers = {
        "Authorization": "Bearer <Your Key>"
    }
    response = requests.put(
    	"<https://api.secoda.co/table/7o7y2s75ktirezg6__bigquery__secoda-web__dbt_amcewen__customers>",
    	headers=headers,
    	json={"owners": ["kash@secoda.co"]}
    )
    print(response.json())
    ```

***

### Get All Table Columns

| Endpoint | [https://api.secoda.co/table/](https://api.secoda.co/table/)<:id>/columns |
| -------- | ------------------------------------------------------------------------- |
| Method   | GET                                                                       |

*   Sample Response

    ```json
    {
       "page":1,
       "size":6,
       "results":[
          {
             "id":"7o7y2s75ktirezg6~bigquery://secoda-web.dbt_amcewen/customers~customer_id",
             "neo4j_id":"7o7y2s75ktirezg6~bigquery://secoda-web.dbt_amcewen/customers~customer_id",
             "created_at":"None",
             "updated_at":"None",
             "tags":[
                "3xqw7edwbro7m571"
             ],
             "name":"customer_id",
             "col_type":"INTEGER",
             "owners":[
                "andrew@secoda.co"
             ],
             "badges":"None"
          },
          {
             "id":"7o7y2s75ktirezg6~bigquery://secoda-web.dbt_amcewen/customers~first_name",
             "neo4j_id":"7o7y2s75ktirezg6~bigquery://secoda-web.dbt_amcewen/customers~first_name",
             "created_at":"None",
             "updated_at":"None",
             "tags":[
                "2w1dot2hn6ksmskj"
             ],
             "name":"first_name",
             "col_type":"STRING",
             "owners":[
                "mark@secoda.co",
                "kash@secoda.co",
                "andrew@secoda.co",
                "andrewmcewen96@gmail.com"
             ],
             "badges":"None"
          },
          {
             "id":"7o7y2s75ktirezg6~bigquery://secoda-web.dbt_amcewen/customers~last_name",
             "neo4j_id":"7o7y2s75ktirezg6~bigquery://secoda-web.dbt_amcewen/customers~last_name",
             "created_at":"None",
             "updated_at":"None",
             "tags":[
                "ck7mwwfea59bbn7r"
             ],
             "name":"last_name",
             "col_type":"STRING",
             "owners":[
                "andrewmcewen96@gmail.com",
                "kash@secoda.co"
             ],
             "badges":"None"
          },
          {
             "id":"7o7y2s75ktirezg6~bigquery://secoda-web.dbt_amcewen/customers~first_order_date",
             "neo4j_id":"7o7y2s75ktirezg6~bigquery://secoda-web.dbt_amcewen/customers~first_order_date",
             "created_at":"None",
             "updated_at":"None",
             "tags":[
                "ck7mwwfea59bbn7r"
             ],
             "name":"first_order_date",
             "col_type":"DATE",
             "owners":[
                "mark@secoda.co"
             ],
             "badges":"None"
          },
          {
             "id":"7o7y2s75ktirezg6~bigquery://secoda-web.dbt_amcewen/customers~most_recent_order_date",
             "neo4j_id":"7o7y2s75ktirezg6~bigquery://secoda-web.dbt_amcewen/customers~most_recent_order_date",
             "created_at":"None",
             "updated_at":"None",
             "tags":[
                "2w1dot2hn6ksmskj"
             ],
             "name":"most_recent_order_date",
             "col_type":"DATE",
             "owners":[
                "kash@secoda.co"
             ],
             "badges":"None"
          },
          {
             "id":"7o7y2s75ktirezg6~bigquery://secoda-web.dbt_amcewen/customers~number_of_orders",
             "neo4j_id":"7o7y2s75ktirezg6~bigquery://secoda-web.dbt_amcewen/customers~number_of_orders",
             "created_at":"None",
             "updated_at":"None",
             "tags":[
                
             ],
             "name":"number_of_orders",
             "col_type":"INTEGER",
             "owners":[
                "andrew@secoda.co"
             ],
             "badges":"None"
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
    	"<https://api.secoda.co/table/7o7y2s75ktirezg6__bigquery__secoda-web__dbt_amcewen__customers/columns>",
    	headers=headers
    )
    print(response.json())
    ```

***

### Update Table Column

| Endpoint                 | [https://api.secoda.co/table/](https://api.secoda.co/table/)<:id>/columns |
| ------------------------ | ------------------------------------------------------------------------- |
| Method                   | PUT                                                                       |
| Accepted Body Parameters | name, owners, tags, description                                           |

*   Sample Response

    ```json
    {
       "msg":"Successfully updated column"
    }
    ```
*   Python Example

    ```python
    import requests

    headers = {
        "Authorization": "Bearer <Your Key>"
    }
    response = requests.put(
    	"<https://api.secoda.co/table/7o7y2s75ktirezg6__bigquery__secoda-web__dbt_amcewen__customers/columns/>",
    	headers=headers,
    	json={"name": "number_of_orders", "owners": ["kash@secoda.co"]}
    )
    print(response.json())
    ```

***

### Delete Table Column

| Endpoint                 | [https://api.secoda.co/table/](https://api.secoda.co/table/)<:id>/columns?name=\<col\_name> |
| ------------------------ | ------------------------------------------------------------------------------------------- |
| Method                   | DELETE                                                                                      |
| Accepted Body Parameters | name                                                                                        |

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
    	"<https://api.secoda.co/table/7o7y2s75ktirezg6__bigquery__secoda-web__dbt_amcewen__customers/columns?name=number_of_orders>",
    	headers=headers
    )
    print(response.json())
    ```



    {% hint style="info" %}
    Not using Secoda to manage your data knowledge yet? Sign up for free [here](https://app.secoda.co) 👈
    {% endhint %}
