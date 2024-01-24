# Extracted Queries

Extracted queries are pulled in directly from the integration. Secoda extracts the Query History as well as the Creation Query for the resource.

## Query History

By clicking on the Queries tab from a resource in Secoda, you can see the query history for that resource. Query history is extracted for:

* [snowflake-integration](../../integrations/data-warehouses/snowflake-integration/ "mention")
* [redshift-integration](../../integrations/data-warehouses/redshift-integration/ "mention")
* [aws-glue-integration](../../integrations/data-pipeline-tools/aws-glue-integration/ "mention")
* [bigquery-integration](../../integrations/data-warehouses/bigquery-integration/ "mention")

At time of extraction, Secoda pulls the last 24 hours of queries run on the resource, directly from the integration. Any queries that haven't been previously seen will be added to the list of queries associated with that resource in Secoda. This list of queries can be found through the Queries tab of the resource page, as seen below.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/1f615616-7da5-4871-afcd-9be6146ebd62.gif" alt=""><figcaption></figcaption></figure>

Queries can easily be copied, and run directly in Secoda through the [Query editor in a document](running-queries-in-secoda/).

## Creation queries

For resources that are created from a query (ex. Views) , You can find the Creation Query in the top right hand corner by clicking the `</>` icon. You can also copy that code for ease of use.

<figure><img src="../../.gitbook/assets/Kapture 2024-01-24 at 16.24.33.gif" alt=""><figcaption></figcaption></figure>
