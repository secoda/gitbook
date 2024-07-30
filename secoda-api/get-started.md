---
description: Tips and tricks for using the Secoda APIs.
---

# Get Started

The Secoda API is based around REST principals. You will need a [Bearer](authentication.md) token to use the API - see the [authentication page](authentication.md) for instructions on how to create your token.&#x20;

## Base URL

See below for the Base URL for your workspace.

| Workspace URL    | API Base URL     |
| ---------------- | ---------------- |
| `app.secoda.co`  | `api.secoda.co`  |
| `eu.secoda.co`   | `eapi.secoda.co` |
| `apac.secoda.co` | `aapi.secoda.co` |

If your workspace is associated with a unique URL, then the Base URL for the API is formed by appending `api/v1/` to the end of your workspace's URL.

### Test the Base URL

Make a request to the Secoda Health Check API endpoint `/healthcheck`. A successful response should look like this.&#x20;

```json
{
    "status": "OK"
}
```

## Pagination

The API response includes several key components relevant to pagination:

* `links`: Contains URLs for the next and previous pages.
* `meta`: Provides metadata including the current page, previous page, and next page numbers.
* `count`: The total number of items in the dataset.
* `total_pages`: The total number of pages available.
* `results`: An array of objects, each representing a data item.

**Initial Request**

To start retrieving data, make a request to the API endpoint. If no page is specified, the first page of results is returned by default.

**Navigating Pages**

* **Next Page**: To move to the next page, use the URL provided in the `links.next` field. If this field is `null`, it indicates you are on the last page.
* **Previous Page**: To return to the previous page, use the URL in the `links.previous` field. A value of `None` indicates you are on the first page.
* **Specific Page**: To request a specific page, modify the request URL to include the desired page number as a query parameter (e.g., `?page=3`).

#### Handling Pagination in Client Code

1. **Check Pagination Links**: Always check the `links.next` field to determine if additional pages are available.
2. **Loop Through Pages**: If automating data retrieval, loop through pages by making subsequent requests using the URL in `links.next` until it is `null`.
3. **Access Page Metadata**: Utilize the `meta` field to present navigation controls or information about the current page status in your application UI.

#### Example Code Snippet

Here's a simplified example in Python using the `requests` library to navigate through pages:

```python
pythonCopy codeimport requests

def fetch_all_pages(start_url):
    next_url = start_url
    while next_url:
        response = requests.get(next_url)
        data = response.json()
        process_data(data['results'])  # Implement this function as needed
        next_url = data['links']['next']  # Will be None if on the last page

def process_data(results):
    for item in results:
        print(item)  # Placeholder for data processing logic

# Initial call to fetch data
fetch_all_pages("https://api.secoda.co/resource/all/")
```

## Catalog Filters

To list resources in your workspace with fine-grained control over filtering and sorting, you can use the `resource/catalog` endpoint from Secoda. This endpoint allows you to customize the response by providing a serialized JSON object, URL encoded, as a query parameter in your request.

To generate the JSON object, you can use our API filter generator in your Settings page.&#x20;

{% embed url="https://www.loom.com/share/0d051cbf9b7a45b0b8582c5f779ac448" %}

If you'd like to build your filters from scratch, refer to the [JSON documentation](https://api.secoda.co/api/schema/redoc/#tag/Resource/paths/\~1resource\~1catalog/get) for detailed information on the JSON structure, and the file linked below for how to utilize this request. The linked file is a sample Jupyter Notebook that demonstrates how to retrieve all resources that are Tables, Views, Dashboards, or Workbooks, which contain "customers" in the title. The results are sorted in descending order based on the last update time of the resource.

{% file src="../.gitbook/assets/Catalog Filter Template" %}

Note: This script linked does not account for pagination. Please see the [pagination](get-started.md#pagination) section above for guidance around implementing this as part of your script.&#x20;
