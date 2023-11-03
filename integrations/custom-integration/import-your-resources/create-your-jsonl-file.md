---
description: This page will describe how to create a JSONL file for upload into Secoda.
---

# Create your JSONL File

Create a newline-delimited JSON (JSONL) file that contains a JSON object for each resource or lineage entry that is meant to be imported into Secoda.&#x20;

Secoda expects metadata files to follow a newline-delimited JSON (JSONL) format. Two types of files can be uploaded into Secoda into this way:&#x20;

1. `resources.jsonl`: Contains metadata for various entities, such as tables, columns, dashboards, and charts.
2. `lineages.jsonl`: Contains lineage information that describes relationships between entities.

Example for `resources.jsonl`:

```
{"entity_type": "table", "databuilder_id": "secoda.public.order", "title": "order", "description": "Orders from KFC", "schema": "public", "database": "secoda"}
{"entity_type": "column", "databuilder_id": "secoda.public.order.order_id", "parent_databuilder_id": "secoda.public.order", "title": "order_id", "is_pk": true, "hidden": false}
{"entity_type": "dashboard", "databuilder_id": "dashboard.revenue_2023_forecast", "title": "2023 Revenue Forecast"}
{"entity_type": "chart", "databuilder_id": "dashboard.revenue_2023_forecast.yoy_growth", "parent_databuilder_id": "dashboard.revenue_2023_forecast", "title": "YoY Growth"}
```

Example for `lineage.jsonl`:

```
{"from_databuilder_id": "secoda.public.order.order_id", "to_databuilder_id": "dashboard.revenue_2023_forecast.yoy_growth"}
{"from_databuilder_id": "secoda.public.order", "to_databuilder_id": "dashboard.revenue_2023_forecast"}
```

These JSON objects have several required and optional fields, defined below.

## Resource Fields

<table><thead><tr><th width="135">Field Name</th><th width="171">Data Type</th><th width="155">Description</th><th width="88" data-type="checkbox">Required</th><th>Example</th></tr></thead><tbody><tr><td>entity_type</td><td>Enum (options are <code>table</code>, <code>column</code>, <code>dashboard</code>, <code>chart</code>)</td><td>The type of resource</td><td>true</td><td>"table"</td></tr><tr><td>databuilder_id</td><td>String</td><td>A unique and unchanging ID created for the resource. </td><td>true</td><td>"secoda.snowflake.customers"</td></tr><tr><td>parent_databuilder_id</td><td>String</td><td>A unique and unchanging ID referencing the parent for the resource. </td><td>false</td><td>"secoda.snowflake.orders"</td></tr><tr><td>title</td><td>String</td><td>The title or name for the resource.</td><td>false</td><td>"customer"</td></tr><tr><td>description</td><td>String</td><td>The description for the resource.</td><td>false</td><td>"This table reflects all the customers in the workspace"</td></tr><tr><td>definition</td><td>String</td><td>The mark down documentation for the resource.</td><td>false</td><td>"&#x3C;h2>This is my documentation&#x3C;/h2>"</td></tr><tr><td>external_updated_at</td><td>String (datetime format)</td><td>The last time the resource was updated in the source.</td><td>false</td><td>"2000-10-31T01:30:00.000-05:00"</td></tr><tr><td>native_type</td><td>String</td><td>The type of the resource as it's referred to in the source.</td><td>false</td><td>"view"</td></tr></tbody></table>

For specific resource types, additional fields are available or required, as listed below.

#### Column Specific&#x20;

<table><thead><tr><th>Field Name</th><th width="114">Data Type</th><th width="219">Description</th><th width="95" data-type="checkbox">Required (for Columns)</th><th>Example</th></tr></thead><tbody><tr><td>sort_order</td><td>Integer</td><td>The order in which the columns should show up.</td><td>false</td><td>4</td></tr><tr><td>type</td><td>String</td><td>The datatype of the column.</td><td>false</td><td>"integer"</td></tr><tr><td>is_pk</td><td>Boolean</td><td>Defines whether the column is a primary key.</td><td>false</td><td>"true"</td></tr><tr><td>parent_databuild_id</td><td>String</td><td>A unique and unchanging ID referencing the parent for the resource. For a column, the parent is either another column or a table.</td><td>true</td><td>"snowflake.orders.table"</td></tr></tbody></table>

#### Table Specific

<table><thead><tr><th>Field Name</th><th width="112">Data Type</th><th width="173">Description</th><th width="89" data-type="checkbox">Required (for Tables)</th><th>Example</th></tr></thead><tbody><tr><td>schema</td><td>String</td><td>The schema from which the table is extracted.</td><td>true</td><td>"sales"</td></tr><tr><td>database</td><td>String</td><td>The database from which the table is extracted.</td><td>true</td><td>"sales_db"</td></tr></tbody></table>

#### Dashboard Specific

<table><thead><tr><th>Field Name</th><th>Data Type</th><th width="127">Description</th><th width="69" data-type="checkbox">Required (for Dashboards)</th><th>Example</th></tr></thead><tbody><tr><td>group</td><td>String</td><td>The group that the dashboard is extracted from.</td><td>true</td><td>"analytics"</td></tr></tbody></table>

#### Chart Specific

<table><thead><tr><th width="134">Field Name</th><th width="93">Data Type</th><th width="186">Description</th><th width="73" data-type="checkbox">Required (for Charts)</th><th>Example</th></tr></thead><tbody><tr><td>product</td><td>String</td><td>The name of the source.</td><td>true</td><td>"tableau"</td></tr><tr><td>parent_databuilder_id</td><td>String</td><td>A unique and unchanging ID referencing the parent for the resource. For a chart, the parent is a dashboard.</td><td>true</td><td>"tableau.analytics.dashboard"</td></tr></tbody></table>

## Lineage Fields

The following fields are for creating lineage to upload using a JSONL file.

<table><thead><tr><th width="213">Field Name</th><th width="84">Data Type</th><th width="127">Description</th><th width="97" data-type="checkbox">Required</th></tr></thead><tbody><tr><td>from_databuilder_id</td><td>String</td><td>The databuilder ID of the source resource.</td><td>true</td></tr><tr><td>to_databuilder_id</td><td>String</td><td>The databuilder ID of the target resource.</td><td>true</td></tr></tbody></table>

## Generating Metadata Files (Example)

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
class Lineage(pydantic.BaseModel):
    from_databuilder_id: str
    to_databuilder_id: str
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
		from_databuilder_id="secoda.public.order.order_id",
		to_databuilder_id="dashboard.revenue_2023_forecast.yoy_growth",
	),
	Lineage(
		from_databuilder_id="secoda.public.order",
		to_databuilder_id="dashboard.revenue_2023_forecast",
	),
]

resources_jsonl_content = "\n".join([json.dumps(entity.model_dump(exclude_none=True, by_alias=True)) for entity in entities])
lineages_jsonl_content = "\n".join([json.dumps(lineage.model_dump(exclude_none=True, by_alias=True)) for lineage in lineages])
```

{% hint style="info" %}
Have any questions about how to generate a JSONL file? Get in touch at [support@secoda.co](mailto:support@secoda.co).
{% endhint %}
