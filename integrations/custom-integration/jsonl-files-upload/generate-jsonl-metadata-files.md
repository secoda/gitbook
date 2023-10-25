# Generate JSONL Metadata Files

## Schema and Pydantic Types

Secoda metadata is defined using Pydantic models. Here's an overview of the key attributes for the `Entity` and `Lineage` Pydantic models:

```python
class Entity(pydantic.BaseModel):
    entity_type: SecodaEntityTypes
    databuilder_id: str
    parent_databuilder_id: Optional[str] = None
    title: Optional[str] = ""
    description: Optional[str] = None
    definition: Optional[str] = None
    external_updated_at: Optional[datetime] = None
    native_type: Optional[str] = None

    # Column specific
    sort_order: Optional[int] = None
    type: Optional[str] = None
    is_pk: Optional[bool] = False
    hidden: Optional[bool] = False

    # Table specific, required for table
    schema: Optional[str] = None
    database: Optional[str] = None

    # Dashboard specific
    group: Optional[str] = None

    # Chart specific
    product: Optional[str] = None
    
```

#### Entity

* `entity_type` (Enum): The type of the entity, such as table, column, dashboard, or chart.
* `databuilder_id` (String): A unique identifier for the resource, following your naming convention.
* `parent_databuilder_id` (Optional String): For columns, this indicates the parent table's databuilder\_id.
* `title` (Optional String): A title or name for the resource.
* `description` (Optional String): A description of the resource.
* `schema` (Optional String): Required for tables, the schema to which the table belongs.
* `database` (Optional String): Required for tables, the database where the table is located.

For specific entity types, additional attributes are available, such as `sort_order`, `type`, `is_pk`, `hidden`, `group`, and `product`.

```python
class Lineage(pydantic.BaseModel):
    from_databuilder_id: str
    to_databuilder_id: str
```

#### Lineage

* `from_databuilder_id` (String): The unique identifier of the source resource.
* `to_databuilder_id` (String): The unique identifier of the target resource.



## Metadata File Structure

Metadata files for Secoda follow a newline-delimited JSON (JSONL) format. There are two main types of files:

1. `resources.jsonl`: Contains metadata for various entities, such as tables, columns, dashboards, and charts.
2. `lineages.jsonl`: Contains lineage information that describes relationships between entities.

Here's an example of what these files may look like:

#### Example `resources.jsonl`:

```json
{"entity_type": "table", "databuilder_id": "secoda.public.order", "title": "order", "description": "Orders from KFC", "schema": "public", "database": "secoda"}
{"entity_type": "column", "databuilder_id": "secoda.public.order.order_id", "parent_databuilder_id": "secoda.public.order", "title": "order_id", "is_pk": true, "hidden": false}
{"entity_type": "dashboard", "databuilder_id": "dashboard.revenue_2023_forecast", "title": "2023 Revenue Forecast"}
{"entity_type": "chart", "databuilder_id": "dashboard.revenue_2023_forecast.yoy_growth", "parent_databuilder_id": "dashboard.revenue_2023_forecast", "title": "YoY Growth"}
```

#### Example `lineages.jsonl`:

```json
{"from_databuilder_id": "secoda.public.order.order_id", "to_databuilder_id": "dashboard.revenue_2023_forecast.yoy_growth"}
{"from_databuilder_id": "secoda.public.order", "to_databuilder_id": "dashboard.revenue_2023_forecast"}
```

## Generating Metadata Files

To generate metadata files similar to the examples above, you can use Python. In practice, you can connect to external APIs or databases to create the corresponding entities and lineages. Below is an example of how to generate such JSONL files using Python:

```python
entities = [
	Entity(
		entity_type=SecodaEntityTypes.TABLE,
		databuilder_id="secoda.public.order",
		title="order",
		schema="public",
		database="secoda",
		description="Orders from KFC"
	),
	Entity(
		entity_type=SecodaEntityTypes.COLUMN,
		databuilder_id="secoda.public.order.order_id",
		title="order_id",
		parent_databuilder_id="secoda.public.order",
		is_pk=True,
	),
	Entity(
		entity_type=SecodaEntityTypes.DASHBOARD,
		databuilder_id="dashboard.revenue_2023_forecast",
		title="2023 Revenue Forecast",
	),
	Entity(
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

\
