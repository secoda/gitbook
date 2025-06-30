---
description: Customize and manage your integration after setup.
---

# Integration Settings

On the **Integrations** page, you can easily view and search through all your integrations. You can see details about your integrations including the last and upcoming runs, as well as the status of the most recent run. Additionally, you can use the command palette to run or delete multiple integrations at once.

{% hint style="warning" %}
Deleting an integration from the workspace will remove all associated resources. Adding the integration back will not preserve the changes (e.g. metadata updates) that were made when originally connected and rather will act as a new integration.
{% endhint %}

If you click into an integration, the following options become available.

### Enable Integration

After selecting an integration, you'll find the **Enabled** toggle in the top right corner. By default, all integrations are enabled. If toggled off, the integration is paused, meaning it will not run automatically based on the schedule set.

### Run Sync

In the top right corner, you'll also see the **Run Sync** button. This action triggers a manual sync. Clicking this button allows you to choose whether the sync should **Pull** or **Push** metadata.

{% hint style="info" %}
Not all integrations will support both Pull and Push. Learn more about what integrations are supported for Push Metadata [here](push-metadata-to-source.md).
{% endhint %}

### Syncs

This is the first page you’ll see when you navigate to an integration. It provides a detailed history of past syncs, allowing you to review each sync's stages, the number of resources pulled, and any errors that may have occurred.

### Schedule

To automate your syncs, use this page to set the run frequency with a Cron Expression. You can learn more about Cron Expressions [here](https://crontab.guru/). If you don’t specify a schedule, the default is `0 0 * * *`, which runs the sync daily at midnight UTC.

### Schemas & Groups

If applicable to the integration, use this page to select which Groups or Schemas you want to sync. Click the **Refresh** button to check for any new Groups or Schemas available for import. By default, all Groups and Schemas will be selected and included in the sync.

If you'd like to change this default behaviour, navigate to the [Resource Management](integration-settings.md#resource-management) section in the [Preferences.](integration-settings.md#preferences)

In addition the Teams that a Database, Schema, or Group are associated with can be configured on this tab under the "Team visibility" column. By default, the Teams will be inherited from the Integration settings but you can override the Teams on any Database, Schema, or Group.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/fccf81f7-f9b1-443f-9e3a-41301152545b.png" alt=""><figcaption></figcaption></figure>

### Preferences

#### Query Permissions

This section lets you choose which users in your workspace have permission to query the resource through the preview, query block, monitoring, and Secoda AI feature, if the integration supports querying. By default, only Admins and Editors can query the resource.

<figure><img src="../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Popularity

This preference allows you to deselect any accounts that you do not want to contribute to resource Popularity. The Popularity of a data resource in Secoda is determined by the number of times it has been queried or viewed in the last 24 hours, with data pulled directly from the integration. Learn more about Popularity [here](../features/popularity.md).

#### Property Import

This preference allows your to determine the import behaviour of properties, such as descriptions and tags, from your data source as properties in Secoda. The following options are available for importing properties:

* **Never**: No properties are imported from your data source
* **Smart**: Properties are imported from your data source until modified in Secoda. Once you edit a property in Secoda, it won't be overwritten by future imports
* **Always**: Properties are always imported from your data source. Overwrites any existing values in Secoda with each sync

#### Resource Management

This section offers several options. If a toggle is specific to a particular integration, please refer to the integration page in the Secoda documentation for more details about that toggle. The options listed below are shared across all integrations:

* **Disable Automatic Staling:** Prevents the automatic removal of resources that are not present in subsequent syncs for this integration. By default, if a resource is not extracted in a subsequent sync (ex. it is removed from the source), it is removed from the workspace. With this setting enabled, those resources will remain accessible in the workspace.
* **Disable Extraction of Resources from New Schemas:** Prevents the automatic extraction of resources from newly added groups or schemas. By default, if a new schema or group is added in the source, the subsequent sync will extract all resources from that schema or group. Disabling this option means you'll need to manually select the new schema or group in the [Groups or Schema](integration-settings.md#groups-or-schemas) page to extract those resources.

#### Filtering

In this section, you can use the filters to exclude resources (schemas, tables, columns) from extraction based on their title. Excluding resources based on other properties is not currently supported.

### FAQs

<details>

<summary>How does property management for descriptions, tags, and owners work?</summary>

Secoda uses change tracking to determine the source of truth for properties like descriptions, owners, and tags.

The source property is used when:

* Property is empty in Secoda
* Property hasn't been modified by users in Secoda
* Source provides new data

User modifications are preserved in Secoda when:

* Users have manually edited the property in Secoda

Additional cases:

* First sync: Source data populates all empty properties
* Empty source values: Don't overwrite existing Secoda data
* Compliance integrations (e.g., Cyera, and Dataplex): Tags are appended rather than replaced

The system prioritizes preserving user curation while allowing source systems to populate and update unmodified properties.

</details>
