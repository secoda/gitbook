---
description: >-
  This page explains all the fields that are used to add metadata to the
  resources in Secoda.
---

# Secoda Fields Explained

The fields below are referenced in the [JSONL file](custom-integration/create-your-jsonl-file.md), the [SDK Documentation](secoda-sdk-custom-integration/sdk-documentation.md), and in the [API docs](broken-reference).

## Base Resource Fields

The following fields apply to all the [Resources](../../resource-and-metadata-management/#what-is-a-resource) in Secoda.&#x20;

<table><thead><tr><th>Field Name</th><th>Data Type</th><th>Description</th><th data-type="checkbox">Required</th><th>Example</th></tr></thead><tbody><tr><td>entity_type</td><td>Enum <br><code>database</code>, <code>schema</code>, <code>table</code>, <code>column</code>, <code>dashboard_group</code>, <code>dashboard</code>, <code>chart</code></td><td>The type of resource.</td><td>true</td><td>"table"</td></tr><tr><td>databuilder_id</td><td>String</td><td>A unique and unchanging ID created for the resource. </td><td>true</td><td>"secoda.snowflake.customers"</td></tr><tr><td>parent_databuilder_id</td><td>String</td><td>A unique and unchanging ID referencing the parent for the resource. </td><td>false</td><td>"secoda.snowflake.orders"</td></tr><tr><td>title</td><td>String</td><td>The title or name for the resource.</td><td>false</td><td>"customer"</td></tr><tr><td>description</td><td>String</td><td>The description for the resource.</td><td>false</td><td>"This table reflects all the customers in the workspace"</td></tr><tr><td>definition</td><td>String</td><td>The mark down documentation for the resource.</td><td>false</td><td>"&#x3C;h2>This is my documentation&#x3C;/h2>"</td></tr><tr><td>external_updated_at</td><td>String (datetime format)</td><td>The last time the resource was updated in the source.</td><td>false</td><td>"2000-10-31T01:30:00.000-05:00"</td></tr><tr><td>native_type</td><td>String</td><td>The type of the resource as it's referred to in the source.</td><td>false</td><td>"view"</td></tr></tbody></table>

For specific resource types, additional fields are available or required, as listed below.

#### Column Specific Fields

<table><thead><tr><th>Field Name</th><th>Data Type</th><th>Description</th><th data-type="checkbox">Required (for Columns)</th><th>Example</th></tr></thead><tbody><tr><td>sort_order</td><td>Integer</td><td>The order in which the columns should show up.</td><td>false</td><td>4</td></tr><tr><td>type</td><td>String</td><td>The datatype of the column.</td><td>false</td><td>"integer"</td></tr><tr><td>is_pk</td><td>Boolean</td><td>Defines whether the column is a primary key.</td><td>false</td><td>"true"</td></tr><tr><td>parent_databuild_id</td><td>String</td><td>A unique and unchanging ID referencing the parent for the resource. For a column, the parent is either another column or a table.</td><td>true</td><td>"snowflake.orders.table"</td></tr></tbody></table>

#### Table Specific Fields

<table><thead><tr><th>Field Name</th><th>Data Type</th><th>Description</th><th data-type="checkbox">Required (for Tables)</th><th>Example</th></tr></thead><tbody><tr><td>schema</td><td>String</td><td>The schema from which the table is extracted.</td><td>true</td><td>"sales"</td></tr><tr><td>database</td><td>String</td><td>The database from which the table is extracted.</td><td>true</td><td>"sales_db"</td></tr></tbody></table>

#### Dashboard Specific Fields

<table><thead><tr><th>Field Name</th><th>Data Type</th><th>Description</th><th data-type="checkbox">Required (for Dashboards)</th><th>Example</th></tr></thead><tbody><tr><td>group</td><td>String</td><td>The group that the dashboard is extracted from.</td><td>true</td><td>"analytics"</td></tr></tbody></table>

#### Chart Specific Fields

<table><thead><tr><th>Field Name</th><th>Data Type</th><th>Description</th><th data-type="checkbox">Required (for Charts)</th><th>Example</th></tr></thead><tbody><tr><td>product</td><td>String</td><td>The name of the source.</td><td>true</td><td>"tableau"</td></tr><tr><td>parent_databuilder_id</td><td>String</td><td>A unique and unchanging ID referencing the parent for the resource. For a chart, the parent is a dashboard.</td><td>true</td><td>"tableau.analytics.dashboard"</td></tr></tbody></table>

## Lineage Fields

The lineage fields can be used to build a connection between any two resources in Secoda.&#x20;

Each Lineage object should have a `to_identifier` to represent a target resource, and a `from_identifier` to represent a source resource. One or both of these resources **must** be an internal resource (a part of the custom integration that is being built).&#x20;

The `to_identifier` and `from_identifier` accept a LineageID object, which is made up of a type, as well as several fields unique to each type. The type and relevant fields are broken down below.&#x20;

<table><thead><tr><th width="169">Field Name</th><th width="137">Data Type</th><th width="156">Description</th><th width="107" data-type="checkbox">Required</th><th>Example</th></tr></thead><tbody><tr><td>from_identifier</td><td>Object</td><td>A LineageID object identifying the type of lineage, and source resource. </td><td>true</td><td>"from_identifier": { "type": "external_column", "cluster": "data_warehouse_cluster", "database": "marketing_db", "schema": "public", "table": "campaign_data", "column": "click_through_rate" }</td></tr><tr><td>to_identifier</td><td>Object</td><td>A LineageID object identifying the type of lineage, and target resource. This field <strong>does not</strong> accept <code>tables_from_query</code> as a type. </td><td>true</td><td>"to_identifier": { "type": "internal_resource", "databuilder_id": "internal.dashboard.654" }</td></tr></tbody></table>

### LineageID Fields

The LineageID object will **always** consist of a `type` field, along with several other fields depending on the type. &#x20;

<table><thead><tr><th>Field Name</th><th width="211">Data Type</th><th>Description</th><th data-type="checkbox">Required</th><th>Example</th></tr></thead><tbody><tr><td>type</td><td>Enum  <br>-<code>internal_resource</code><br>-<code>external_table</code><br>-<code>external_column</code><br>-<code>tables_from_query</code></td><td>The type of resource in the context of lineage. </td><td>true</td><td>"internal_resource"</td></tr></tbody></table>

#### Internal Resource Fields

If the source or target resource is internal to the integration, the type of the LineageID object should be `internal_resource`, and the following field is required in addition to type.&#x20;

<table><thead><tr><th width="163">Field Name</th><th>Data Type</th><th>Description</th><th data-type="checkbox">Required</th><th>Example</th></tr></thead><tbody><tr><td>databuilder_id</td><td>String</td><td>A unique and unchanging ID referencing the internal resource in Secoda. </td><td>true</td><td>"internal.dashboard.123"</td></tr></tbody></table>

#### External Table Fields

If the source or target resource is a table external to the integration, the type of the LineageID object should be `external_table`, and the following fields are required in addition to type.&#x20;

<table><thead><tr><th>Field Name</th><th>Data Type</th><th>Description</th><th data-type="checkbox">Required</th><th>Example</th></tr></thead><tbody><tr><td>cluster</td><td>String</td><td>The name of the cluster that the external table belongs to in Secoda.</td><td>true</td><td>"sales"</td></tr><tr><td>database</td><td>String</td><td>The name of the database that the external table belongs to in Secoda.</td><td>true</td><td>"sales_db"</td></tr><tr><td>schema</td><td>String</td><td>The name of the schema that the external table belongs to in Secoda.</td><td>true</td><td>"staging"</td></tr><tr><td>table</td><td>String</td><td>The name of the external table. </td><td>true</td><td>"customers"</td></tr></tbody></table>

#### External Column Fields

If the source or target resource is a column external to the integration, the type of the LineageID object should be `external_column`. In addition to type, all of the fields from the External Table type are required, along with a field for column.&#x20;

<table><thead><tr><th>Field Name</th><th>Data Type</th><th>Description</th><th data-type="checkbox">Required</th><th>Example</th></tr></thead><tbody><tr><td>column</td><td>String</td><td>The name of the external column.</td><td>true</td><td>"customer_id"</td></tr></tbody></table>

#### Tables from Query Fields&#x20;

For the source resource (the LineageID object in the `from_identifier` field), the type can also be `tables_from_query`. This type requires an SQL query that will be processed to determine what the source resources are.

<table><thead><tr><th>Field Name</th><th>Data Type</th><th>Description</th><th data-type="checkbox">Required</th><th>Example</th></tr></thead><tbody><tr><td>sql</td><td>String</td><td>An SQL query used to determine lineage. The SQL query must return resources that exist in Secoda. </td><td>true</td><td>"SELECT * FROM public.users INNER JOIN public.orders ON users.id = orders.user_id"</td></tr></tbody></table>
