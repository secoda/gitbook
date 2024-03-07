# Get Started

The Secoda API is based around REST principals. You will need a [Bearer](authentication.md) token to use the API.&#x20;

See below for the Base URL for your workspace.

| Workspace URL    | API Base URL     |
| ---------------- | ---------------- |
| `app.secoda.co`  | `api.secoda.co`  |
| `eu.secoda.co`   | `eapi.secoda.co` |
| `apac.secoda.co` | `aapi.secoda.co` |

> If your workspace has it's own unique instance, with a URL that follows the pattern of `COMPANY-NAME.secoda.co`, the API Base URL to use will following the pattern of `COMPANY-NAME.secoda.co/api/v1`**.**

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
