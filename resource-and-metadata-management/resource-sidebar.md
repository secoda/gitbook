---
description: Explaining the information in the sidesheet.
---

# Resource Sidesheet

When looking at a resource, you can click on the Information symbol in the top right to see a sidesheet of relevant information for your resource.&#x20;

### Properties

Properties refer to fields that can be edited.&#x20;

{% hint style="info" %}
For some integrations, properties such as tags and owners can be imported from the source. To learn more about how to maintain properties in the source or in Secoda, navigate to the [Property Management](../integrations/integration-settings.md#metadata-management-this-functionality-is-coming-soon) in the Integration Settings.&#x20;
{% endhint %}

**Status**: This refers to whether the resource is Published or a Draft. More information about Publishing can be found [here](../getting-started/secoda-as-an-admin/add-documentation/publishing.md).

**Tags**: A list of custom tags added to the resource. More information about adding custom tags can be found [here](tags/custom-tags.md).

**Collections**: A list of all the collections that resource is part of. Learn more about [Collections](../features/collections-1.md) here.

**Owners**: A list of [Users or User Groups](../user-management/) that are owners of the resource.&#x20;

**Governance**: A tag denoting whether the resource is PII or not. More information about setting Governance Tags can be found [here](../best-practices/data-governance.md).

**Verification**: A tag denoting whether the resource is Verified or not. More information about setting Verification can be found [here](tags/verified-tag.md).

**Teams**: A list of [Teams](../user-management/teams.md) that the resource can be found in.

Any custom properties will also show up in this section. Learn more about Custom Properties [here](adding-custom-properties.md).

### Metadata

Metadata refers to fields that are uneditable in Secoda. Use the toggle to see the Metadata generated in Secoda, or in the integration.

See below for explanations of metadata:

**Row Count:** If available, this field indicates the number of rows in that table.

**Table Size:** If available, this field indicates the digital size of the table.

**Popularity:** The [Popularity](../features/popularity.md) field refers the number of Queries run on the resource (if it's a table) or the number of Views received by the resource (if it's a dashboard) in the last 24 hours, relative to the time of the last sync. For instance, if a Snowflake sync happened 3 days ago, Popularity will show the number of queries run on that table in the period from 4 days ago to 3 days ago (24 hours before the time of the sync).

**Views**: The number of views of the resource in Secoda.&#x20;

### Subscribers

This is a list of all the users that are subscribed to get notifications about this resource. Learn more about [Notifications](../features/notifications.md) and [Subscribers](resource-sidebar.md#subscribers) here.
