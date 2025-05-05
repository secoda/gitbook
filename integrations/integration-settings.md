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

#### Preview Permissions

This section allows you to select which Roles or User Groups should have permission to [Preview](../features/data-previews.md) the resource, if the integration supports Preview. By default, all Roles are given permission to preview.

#### Query Permissions

This section lets you choose which Editors in your workspace have permission to query the resource, if the integration supports querying. By default, only Admins can query the resource. However, querying permissions for Viewers are not currently supported.

#### Popularity

This section allows you to deselect any accounts that you do not want to contribute to resource Popularity. The Popularity of a data resource in Secoda is determined by the number of times it has been queried or viewed in the last 24 hours, with data pulled directly from the integration. Learn more about Popularity [here](../features/popularity.md).

#### Property Management

For any integration that syncs Tags, Owners, or Descriptions, this section allows you to choose where these properties are maintained. If they are maintained in Secoda, the fields will never be overwritten by a sync. If they are maintained in the integration, the fields will not be editable in Secoda.

* **Import Descriptions from Integration**
  * Even if the **Import Descriptions from Integration** setting  is toggled off, if there are no descriptions in Secoda, the descriptions will be imported from the source.&#x20;

{% hint style="info" %}
Regardless of the settings chosen, when a resource is synced with Secoda for the first time, all available metadata will be imported.
{% endhint %}

#### Resource Management

This section offers several options. If a toggle is specific to a particular integration, please refer to the integration page in the Secoda documentation for more details about that toggle. The options listed below are shared across all integrations:

* **Disable Automatic Staling:** Prevents the automatic removal of resources that are not present in subsequent syncs for this integration. By default, if a resource is not extracted in a subsequent sync (ex. it is removed from the source), it is removed from the workspace. With this setting enabled, those resources will remain accessible in the workspace.
* **Disable Extraction of Resources from New Schemas:** Prevents the automatic extraction of resources from newly added groups or schemas. By default, if a new schema or group is added in the source, the subsequent sync will extract all resources from that schema or group. Disabling this option means you'll need to manually select the new schema or group in the [Groups or Schema](integration-settings.md#groups-or-schemas) page to extract those resources.

#### Filtering

In this section, you can use the filters to exclude resources (schemas, tables, columns) from extraction based on their title. Excluding resources based on other properties is not currently supported.

{% embed url="https://www.loom.com/share/4d7f24d958464f95ae493d165da7bb0a?sid=5708cbf8-0635-46a7-9fc9-8da59f80e857" %}
