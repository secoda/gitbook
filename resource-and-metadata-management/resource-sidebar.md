---
description: Explaining the information in the sidebar.
---

# Resource Sidebar

When looking at a resource, you can see several pieces of information in the side bar, here is a break down of each.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/b20ea07c-5f1a-408d-b7f2-e3f62d4aa1de.png" alt=""><figcaption><p>Image of the resource sidebar</p></figcaption></figure>

### Properties

Generally, properties refer to fields that are **editable** and can be set within Secoda.

**Status**: This refers to whether the resource is Published or a Draft. More information about Publishing can be found [here](../getting-started/secoda-as-an-admin/add-documentation/publishing.md).

**Tags**: A list of custom tags added to the resource. More information about adding custom tags can be found [here](tags/custom-tags.md).

**Collections**: A list of all the collections that resource is part of. Learn more about [Collections](../features/collections-1.md) here.

**Owners**: A list of [Users or User Groups](../user-management/) that are owners of the resource both set in Secoda and synced from the source (if available). If the owner has been extracted from the source, it cannot be edited and will be greyed out.

**Governance**: A tag denoting whether the resource is PII or not. More information about setting Governance Tags can be found [here](../best-practices/data-governance.md).

**Verification**: A tag denoting whether the resource is Verified or not. More information about setting Verification can be found [here](tags/verified-tag.md).

**Teams**: A list of [Teams](../user-management/teams.md) that the resource can be found in.

Any custom properties will also show up in this section. Learn more about Custom Properties [here](adding-custom-properties.md).

### Metadata

Generally, metadata refers to fields that are **uneditable** in Secoda and can be extracted from the integration or be default fields within Secoda.&#x20;

**Created:** The timestamp of when the resource was created from the Integration. For instance, the time at which the table was created in Snowflake.

**Updated:** The timestamp of last update of the resource from the Integration. For instance, when the Tableau dashboard was last edited in Tableau.

**Type:** The type of the resource as it's referred to in the Integration. For instance, an S Object from Salesforce.

**Frequent Users:** A combination of the top users of the resource, both synced from the Integration as well as from Secoda. The users from the integration are from the last 24 hours relative to the time of sync, while the users from Secoda are from the last 90 days.

**Row Count:** If available, this field indicates the number of rows in that table.

**Table Size:** If available, this field indicates the digital size of the table.

**Popularity:** Synced from the integration only, the [Popularity](../features/popularity.md) field refers the number of Queries run on the resource (if it's a table) or the number of Views received by the resource (if it's a dashboard) in the last 24 hours, relative to the time of the last sync. For instance, if a Snowflake sync happened 3 days ago, Popularity will show the number of queries run on that table in the period from 4 days ago to 3 days ago (24 hours before the time of the sync).

**Views**: The number of views that resource has gotten over the last 90 days in Secoda.

### Subscribers

This is a list of all the users that are subscribed to get notifications about this resource. Learn more about [Notifications](../features/notifications.md) and [Subscribers](resource-sidebar.md#subscribers) here.
