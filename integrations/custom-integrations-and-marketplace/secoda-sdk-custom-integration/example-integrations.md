# Example Integrations

### Example 1: Cluvio

```python
import os

from secodadk import SecodaIntegration, Resource, DeclaredLineage, InternalResource

BASE_URL = "https://api.cluvio.com"


class FakeCluvioIntegration(SecodaIntegration):
    def extract(self):
        token = (
            self.http_post(
                f"{BASE_URL}/users/sign_in",
                json={
                    "user": {
                        "email": self.credentials.get("email"),
                        "password": self.credentials.get("password"),
                    }
                },
                headers={"Accept": "application/json"},
            )
            .json()
            .get("token")
        )

        auth = dict(
            headers={"token": token},
            verify=True,
        )

        group_databuilder_id = "dashboard_group.default"
        self.declare_resource(
            Resource(
                entity_type="dashboard_group",
                databuilder_id=group_databuilder_id,
                title="default",
            )
        )

        for dashboard in (
            self.http_get(
                f"{BASE_URL}/dashboards/",
                **auth,
            )
            .json()
            .get("data", [])
        ):
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


            self.declare_lineage(
                DeclaredLineage(
                    from_identifier=InternalResource(
                        databuilder_id=dashboard_databuilder_id
                    ),
                    to_identifier=InternalResource(databuilder_id=group_databuilder_id),
                )
            )


if __name__ == "__main__":
    FakeCluvioIntegration(
        credentials={
            "email": os.environ.get("EMAIL"),
            "password": os.environ.get("PASSWORD"),
        }
    ).start()
```

### Example 2: Google Cloud Storage

See webinar reviewing this example [here](https://www.youtube.com/watch?v=1oiWOxXs3B4).&#x20;

```python
import os
import csv
import json
from io import StringIO
from secodadk import SecodaIntegration, Resource, DeclaredLineage, InternalResource, ExternalTable
from google.cloud import storage

class GoogleCloudStorageIntegration(SecodaIntegration):
    def extract(self):

        json_key = json.loads(self.credentials.get("json_file"))
        storage_client = storage.Client.from_service_account_info(json_key)

        BUCKET_NAME = self.credentials.get("bucket_name")
        bucket = storage_client.get_bucket(BUCKET_NAME)
        blobs = list(bucket.list_blobs())

        for blob in blobs: 
            # Sample blob names:
            # 2023/
            # 2023/montreal/
            # 2023/montreal/montreal_sales_data.csv

            parts = [part for part in blob.name.split('/') if part]
            if len(parts) == 1:
                ## Database
                self.declare_resource(
                    Resource(
                        title=parts[0],
                        entity_type="database",
                        native_type="folder",
                        databuilder_id=f"{BUCKET_NAME}.{parts[0]}",
                    )
                )
            elif len(parts) == 2:
                ## Schema
                self.declare_resource(
                    Resource(
                        title=parts[1],
                        entity_type="schema",
                        native_type="sub-folder",
                        database=parts[0],
                        databuilder_id=f"{BUCKET_NAME}.{parts[0]}.{parts[1]}"
                    )
                )
            elif len(parts) == 3:
                ## Table
                table_name = (parts[2])[:-4]
                self.declare_resource(
                    Resource(
                        title=table_name, 
                        entity_type="table",
                        native_type="csv",
                        database=parts[0],
                        schema=parts[1],
                        databuilder_id=f"{BUCKET_NAME}.{parts[0]}.{parts[1]}.{table_name}",
                        description=f"CSV data from pop up sales. Can be found here: {blob.public_url}"
                    )
                )

                dataset = BUCKET_NAME.replace("-", "_")
                self.declare_lineage(
                    DeclaredLineage(
                        from_identifier = InternalResource(
                            databuilder_id=f"{BUCKET_NAME}.{parts[0]}.{parts[1]}.{table_name}"
                        ),
                        to_identifier = ExternalTable(
                            database="secoda-web",
                            schema=dataset,
                            table=table_name
                        )
                    )
                )

                csv_string = blob.download_as_text(encoding='utf-8')
                csv_data = csv.reader(StringIO(csv_string), delimiter=',')
                header = next(csv_data)

                for field in header:
                    ## Column
                    self.declare_resource(
                        Resource(
                            title=field,
                            entity_type="column",
                            native_type="field",
                            database=parts[0],
                            schema=parts[1],
                            table=table_name,
                            parent_databuilder_id=f"{BUCKET_NAME}.{parts[0]}.{parts[1]}.{table_name}",
                            databuilder_id=f"{BUCKET_NAME}.{parts[0]}.{parts[1]}.{table_name}.{field}"
                        )
                    )

if __name__ == "__main__":
    GoogleCloudStorageIntegration(
        credentials={
            "json_file": os.environ.get("json_file"),
            "bucket_name": os.environ.get("bucket_name")
        }
    ).start()
```
