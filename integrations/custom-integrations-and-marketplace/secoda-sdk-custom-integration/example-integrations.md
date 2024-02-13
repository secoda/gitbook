# Example Integrations

#### Cluvio Integration

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
