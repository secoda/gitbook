---
description: This page will describe how to create a JSONL file for upload into Secoda.
---

# JSONL File Format

Create a newline-delimited JSON (JSONL) file that contains a JSON object for each resource or lineage entry that is meant to be imported into Secoda.&#x20;

### Resources and Lineage

Secoda expects metadata files to follow a newline-delimited JSON (JSONL) format. Two types of files can be uploaded into Secoda into this way:&#x20;

1. `resources.jsonl`: Contains [metadata](../../../resource-and-metadata-management/#what-is-metadata) for various [resources](../../../resource-and-metadata-management/#what-is-a-resource), such as tables, columns, dashboards, and charts.
2. `lineage.jsonl`: Contains [lineage](../../../features/data-lineage.md) information that describes relationships within Resources in the `resouces.jsonl` file (this is referred to as Internal Lineage) and relationships between Resources in the `resources.jsonl` file with Resources that already exist in Secoda (this is referred to as External Lineage).

{% hint style="info" %}
Learn more about the available fields for the JSON objects [here](../secoda-fields-explained.md).&#x20;
{% endhint %}

#### Example for `resources.jsonl`:

```
{"entity_type": "table", "databuilder_id": "secoda.public.order", "title": "order", "description": "Orders from KFC", "schema": "public", "database": "secoda"}
{"entity_type": "column", "databuilder_id": "secoda.public.order.order_id", "parent_databuilder_id": "secoda.public.order", "title": "order_id", "is_pk": true, "hidden": false}
{"entity_type": "dashboard", "databuilder_id": "dashboard.revenue_2023_forecast", "title": "2023 Revenue Forecast"}
{"entity_type": "chart", "databuilder_id": "dashboard.revenue_2023_forecast.yoy_growth", "parent_databuilder_id": "dashboard.revenue_2023_forecast", "title": "YoY Growth"}
```

#### Example for `lineage.jsonl`:

Example 1: Internal lineage between two internal resources.&#x20;

```
{"from_identifier": { "type": "internal_resource", "databuilder_id": "internal.dashboard.123" }, "to_identifier": { "type": "internal_resource", "databuilder_id": "internal.report.456" } } 
```

Example 2: External lineage from an internal resource to an external table.&#x20;

<pre><code><strong>{ "from_identifier": { "type": "internal_resource", "databuilder_id": "internal.dashboard.789" }, "to_identifier": { "type": "external_table", "cluster": "default_cluster", "database": "sales_db", "schema": "public", "table": "orders" } } 
</strong></code></pre>

Example 3: External lineage from an external column to an internal resource.

```
{ "from_identifier": { "type": "external_column", "cluster": "data_warehouse_cluster", "database": "marketing_db", "schema": "public", "table": "campaign_data", "column": "click_through_rate" }, "to_identifier": { "type": "internal_resource", "databuilder_id": "internal.metric.321" } } 
```

Example 4: Lineage involving a SQL query that references multiple tables. Can be internal or external.&#x20;

```
{ "from_identifier": { "type": "tables_from_query", "sql": "SELECT * FROM public.users INNER JOIN public.orders ON users.id = orders.user_id" }, "to_identifier": { "type": "internal_resource", "databuilder_id": "internal.dashboard.654" } }
```

These JSON objects have several required and optional fields. See an outline of the Secoda fields [here](../secoda-fields-explained.md).&#x20;

### Example - Generating Metadata Files

There are several ways to generate a JSONL file. If you plan on using Python, we recommending defining the Secoda resources as Pydantic models. The code below shows how Secoda has defined the Resource and Lineage models using Pydantic. All the fields as part of the models are explained in the documentation above.

```python
class Resource(pydantic.BaseModel):
    entity_type: SecodaEntityTypes
    databuilder_id: str
    title: Optional[str] = ""
    description: Optional[str] = None
    definition: Optional[str] = None
    external_updated_at: Optional[datetime] = None
    native_type: Optional[str] = None

    # parent_databuilder_id is an optional string depending on the resource that is being created. 
    # Please see notes above to determine when it must be included for your resource.
    parent_databuilder_id: Optional[str] = None

    # Column specific
    sort_order: Optional[int] = None
    type: Optional[str] = None
    is_pk: Optional[bool] = False

    # Table specific, required for table
    schema: Optional[str] = None
    database: Optional[str] = None

    # Dashboard specific
    group: Optional[str] = None

    # Chart specific
    product: Optional[str] = None
    
```

```python
class DeclaredLineage(pydantic.BaseModel):
    from_identifier: LineageID
    to_identifier: LineageID


LineageID = Annotated[
    Union[InternalResource, ExternalTable, ExternalColumn, TablesFromSQLQuery],
    Field(discriminator="type"),
]

class TablesFromSQLQuery(pydantic.BaseModel):
    type: Literal["tables_from_query"] = "tables_from_query"
    sql: str

class ExternalColumn(pydantic.BaseModel):
    type: Literal["external_column"] = "external_column"
    cluster: Optional[str] = None
    database: Optional[str] = None
    schema: Optional[str] = None
    table: str
    column: str

class ExternalTable(pydantic.BaseModel):
    type: Literal["external_table"] = "external_table"
    cluster: Optional[str] = None
    database: Optional[str] = None
    schema: Optional[str] = None
    table: str

class InternalResource(pydantic.BaseModel):
    type: Literal["internal_resource"] = "internal_resource"
    databuilder_id: str
```

Using the models above, below is sample code of how to generate such JSONL files using Python:

```python
resources = [
	Resource(
		entity_type=SecodaEntityTypes.TABLE,
		databuilder_id="secoda.public.order",
		title="order",
		schema="public",
		database="secoda",
		description="Orders from KFC"
	),
	Resource(
		entity_type=SecodaEntityTypes.COLUMN,
		databuilder_id="secoda.public.order.order_id",
		title="order_id",
		parent_databuilder_id="secoda.public.order",
		is_pk=True,
	),
	Resource(
		entity_type=SecodaEntityTypes.DASHBOARD,
		databuilder_id="dashboard.revenue_2023_forecast",
		title="2023 Revenue Forecast",
	),
	Resource(
		entity_type=SecodaEntityTypes.CHART,
		databuilder_id="dashboard.revenue_2023_forecast.yoy_growth",
		title="YoY Growth",
		parent_databuilder_id="dashboard.revenue_2023_forecast",
	),

]
lineages = [
	Lineage(
    		from_identifier=InternalResource(type="internal_resource", databuilder_id="dashboard.revenue_2023_forecast"),
    		to_identifier=InternalResource(type="internal_resource", databuilder_id="dashboard.revenue_2023_forecast.yoy_growth")
	),
	Lineage(
    		from_identifier=ExternalColumn(
        		type="external_column",
        		cluster="data_warehouse_cluster",
        		database="marketing_db",
        		schema="public",
        		table="campaign_data",
        		column="click_through_rate"
    			),
    		to_identifier=InternalResource(type="internal_resource", databuilder_id="secoda.public.order.order_id")
	),
	Lineage(
    		from_identifier=TablesFromQuery(
        		type="tables_from_query",
        		sql="SELECT * FROM public.users INNER JOIN public.orders ON users.id = orders.user_id"
    		),
    		to_identifier=InternalResource(type="internal_resource", databuilder_id="dashboard.revenue_2023_forecast")
	)
]

resources_jsonl_content = "\n".join([json.dumps(entity.model_dump(exclude_none=True, by_alias=True)) for resource in resources])
lineages_jsonl_content = "\n".join([json.dumps(lineage.model_dump(exclude_none=True, by_alias=True)) for lineage in lineages])
```

{% hint style="info" %}
Have any questions about how to generate a JSONL file? Get in touch at [support@secoda.co](mailto:support@secoda.co).
{% endhint %}
