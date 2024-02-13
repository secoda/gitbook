# SDK Documentation

The Secoda SDK is a powerful tool for developers to create custom integrations with the Secoda platform. It provides a framework for connecting and extracting data from various sources into Secoda, allowing for a rich and interconnected data ecosystem.

To build an integration using the Secoda SDK, you'll need to extend the [SecodaIntegration](sdk-documentation.md#secodaintegration-class) base class with extraction logic, sync resources from your source using the [Resource Model](sdk-documentation.md#resource-model), and build lineage using the [Lineage Models](sdk-documentation.md#lineage-models).&#x20;

The Secoda SDK expects that the extraction logic will include several HTTPS network requests, identified in the [Network Methods](sdk-documentation.md#network-methods) below.&#x20;

### SecodaIntegration Class

The `SecodaIntegration` class is the base class for all integrations. It manages authentication, network strategy, and the ingestion of resources and lineage.

When you create a custom integration by subclassing `SecodaIntegration`, you are required to provide a concrete implementation of the `extract` method. This method should contain the logic necessary to connect to your data source, retrieve data, and process it as needed.

#### Key Methods

* `declare_resource(resource: Resource)`: A method to declare a resource such as a table, dashboard, or column to be extracted.
* `declare_lineage(lineage: DeclaredLineage)`: A method to declare lineage, representing a relationship between two resources.

#### Key Attributes

* `credentials`: A dictionary to store user input from the integration connection form in the UI.&#x20;

### Resource Model

The `Resource` model is a data model representing an object in your source system that you want to bring into Secoda. Learn more about Resources [here](../../../resource-and-metadata-management/#what-is-a-resource).&#x20;

The Resource Model is made up of many fields, as seen below.&#x20;

```python
class Resource(pydantic.BaseModel):
    entity_type: str

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
    schema: Optional[str] = None  # type: ignore
    database: Optional[str] = None

    # Dashboard specific
    group: Optional[str] = None

    # Chart specific
    product: Optional[str] = None
```

For more details about the fields of this model, navigate to the [Field Explained](../secoda-fields-explained.md) page.&#x20;

### Lineage Models

The Secoda SDK offers several `Lineage` models, to fully capture all the potential dependencies of the resources, within the source, and between sources. The model has many fields, which are outlined in the classes below.&#x20;

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

The `DeclaredLineage` class captures the relationship between two resources. The `from_identifier` and `to_identifier` attributes accept a `LineageID`. The `LineageID` represents a target or source resource in your workspace, along with the type of resource, and any other relevant details about the resource.&#x20;

The resource types for the `LineageID` are:&#x20;

* Internal Resource - A resource from the current custom integration.
* External Column - A column that already exists in the workspace.
* External Table - A table that already exists in the workspace.
* Tables from SQL Query - A set of tables referenced in a SQL query.&#x20;

When building lineage between two resources, the following combinations are currently supported:&#x20;

* InternalResource ↔ InternalResource
* InternalResource ↔ ExternalTable
* InternalResource ↔ ExternalColumn
* ExternalTable ↔ ExternalTable
* TablesFromSQLQuery -> InternalResource

To learn more about the fields in the Lineage Models, navigate to [Fields Explained](../secoda-fields-explained.md).&#x20;

### Network Methods

Perform HTTP requests of various methods. These methods accept parameters for URL, query parameters, headers, and body data, along with flags for redirect following and SSL verification. Note, you **must** use the Network Methods below for the custom integration.&#x20;

* `http_get()`
* `http_post()`
* `http_put()`
* `http_patch()`
* `http_delete()`

Now that you've written your code, you're ready to [Upload it to Secoda](upload-and-connect-your-custom-integration.md), and [Publish it to the Marketplace](publishing-to-marketplace.md).&#x20;

Looking for extra inspiration? Check our our [Example Integrations](example-integrations.md).&#x20;

{% hint style="info" %}
Need extra support building out your custom integration? Reach out to the Secoda Support team at [support@secoda.co](mailto:support@secoda.co)!
{% endhint %}
