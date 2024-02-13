# Secoda SDK Custom Integration

## Overview

The Secoda SDK is a Python-based toolkit that allows for the creation of custom integrations. These integrations can be used to add resources and lineage to Secoda.

To start building with the Secoda SDK, there are a few steps to follow. First, you need to write your code. You can use the documentation below or scroll down for a [step by step example](./#example-step-by-step-integration-development)!&#x20;

{% content-ref url="sdk-documentation.md" %}
[sdk-documentation.md](sdk-documentation.md)
{% endcontent-ref %}

Once the code is written, you can upload and connect your integration.&#x20;

{% content-ref url="upload-and-connect-your-custom-integration.md" %}
[upload-and-connect-your-custom-integration.md](upload-and-connect-your-custom-integration.md)
{% endcontent-ref %}

And share it in the Secoda Marketplace!

{% content-ref url="publishing-to-marketplace.md" %}
[publishing-to-marketplace.md](publishing-to-marketplace.md)
{% endcontent-ref %}

### Example: Step-by-Step Integration Development

In this guide, we'll build an example integration with a data visualization service called [Cluvio](https://www.cluvio.com/). By the end, you'll be able to write scripts that can be executed locally and ready to be submitted to Secoda.

### Prerequisites

Before you begin, ensure you have:

* Python (3.11 or later recommended) installed on your system.
* Secoda SDK installed via `pip install --upgrade secodadk`.

#### Step 1: Set Up Your Development Environment

Create a new directory for your integration project. Inside this directory, create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

With your virtual environment activated, install the Secoda SDK (and if exists, upgrade to the latest version)

```bash
pip install --upgrade secodadk
```

#### Step 2: Initialize Your Integration Script

Create a new Python file, `fake_cluvio_integration.py`, which will contain your integration code.

#### Step 3: Import SDK Components and define your Integration Class

At the top of your script, import the necessary components from the Secoda SDK:

```python
from secodadk import SecodaIntegration, Resource, DeclaredLineage, InternalResource, ExternalTable
```

Extend the `SecodaIntegration` class to create your own integration:

```python
class FakeCluvioIntegration(SecodaIntegration):
    def extract(self):
        # Your extraction logic goes here.
```

#### Step 4: Implement the  Extraction Logic

The `extract` method is where the integration interacts with Cluvio's API. We'll authenticate using credentials and then extract data:

```python
# Within your extract method
token_response = self.http_post(
    f"https://api.cluvio.com/users/sign_in",
    json={
        "user": {
            "email": self.credentials.get("email"),
            "password": self.credentials.get("password"),
        }
    },
    headers={"Accept": "application/json"},
)
token = token_response.json().get("token")

# Authentication requests
auth = dict(
    headers={"token": token},
    verify=True,
)


# Logic for fetching and declaring resources and lineage
...
```

Note that:

* &#x20;`self.credentials` is a dictionary provided by the `SecodaIntegration` base class, allowing you to access user inputs in the integration connect form.
* We use `self.http_post` for HTTP requests. You **must** use our `self.http_{method}` for HTTP requests. Other library like `requests` or `httpx` will not work. `self.http_{method}` returns a `httpx.Response` instance.&#x20;

With the data obtained from Cluvio, you can now declare resources (e.g., dashboards) via `self.declare_resource`

```python
# Continue your extract method
group_databuilder_id = "dashboard_group.default"
self.declare_resource(
    Resource(
        entity_type="dashboard_group",
        databuilder_id=group_databuilder_id,
        title="default",
    )
)

dashboards = self.http_get(f"https://api.cluvio.com/dashboards/", **auth).json().get("data", [])
for dashboard in dashboards:
    dashboard_databuilder_id = f"dashboard.{dashboard.get('id')}"
    self.declare_resource(
        Resource(
            entity_type="dashboard",
            databuilder_id=dashboard_databuilder_id,
            title=dashboard.get("attributes", {}).get("name"),
            description=dashboard.get("attributes", {}).get("description"),
            parent_databuilder_id=group_databuilder_id,
            external_updated_at=dashboard.get("attributes", {}).get(
                "updated_at"
            ),
            product="cluvio",
            native_type="dashboard",
        )
    )
```

See [Secoda Fields Explained](../secoda-fields-explained.md) for more information on the fields of `Resource` .&#x20;

Lineage between resources is also crucial for understanding the relationship and flow of data. This is declared via the `self.declare_lineage` method. Lineage can be between resources from the same source.

```python
self.declare_lineage(
    DeclaredLineage(
        from_identifier=InternalResource(
            databuilder_id=dashboard_databuilder_id
        ),
        to_identifier=InternalResource(databuilder_id=group_databuilder_id),
    )
)
```

Lineage can also flow from an existing resource in the workspace, to a resource brought in from the custom integration.&#x20;

```
self.declare_lineage(
    DeclaredLineage(
        from_identifier=ExternalTable(
            schema="public",
            table="orders",
        ),
        to_identifier=InternalResource(databuilder_id=dashboard_databuilder_id)
    )
)
```

#### Step 5: Testing Locally

To ensure that your integration works as expected, test it on your local machine. Set the credentials in your environment for security:

```python
if __name__ == "__main__":
    FakeCluvioIntegration(
        credentials={
            "email": os.environ["EMAIL"],
            "password": os.environ["PASSWORD"],
        }
    ).start()
```

Run your script with the environment variables set to your Cluvio credentials:

```bash
EMAIL=your-email@example.com
PASSWORD=yourpassword
python fake_cluvio_integration.py
```

#### Step 6: Finalize Your Integration for Upload

Once you've tested your script and are happy with the results, it's time to [Upload and Connect your Custom Integration](upload-and-connect-your-custom-integration.md).

For the full code of this integration, see [here](example-integrations.md).&#x20;
