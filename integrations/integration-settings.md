---
description: Set up the integration to your teams preferred settings.
---

# Integration Settings

### **Basic**

In the basic settings, you can pick a name to help you identify this integration in Secoda. This can be especially useful when using multiple instances of the same integration (e.g multiple Tableau instances).&#x20;

<figure><img src="../.gitbook/assets/Screenshot 2024-02-09 at 12.02.47 PM.png" alt=""><figcaption></figcaption></figure>

### **Connection**&#x20;

The connection tab is where you will add your credentials (varies depending on the specific integration requirements). This page also includes the documentation to follow along when connecting an integration for the first time.&#x20;

<figure><img src="../.gitbook/assets/Screenshot 2024-02-09 at 12.05.02 PM.png" alt=""><figcaption></figcaption></figure>

### **Sync History**&#x20;

The sync history tab is where you can find a list of all the syncs completed for the integration. This is also where you can trigger and terminate a sync manually.

<figure><img src="../.gitbook/assets/Screenshot 2024-02-09 at 12.07.49 PM (1).png" alt=""><figcaption><p>Running a manual sync</p></figcaption></figure>

<figure><img src="../.gitbook/assets/Screenshot 2024-02-09 at 4.25.48 PM.png" alt=""><figcaption><p>Terminating a running sync</p></figcaption></figure>

Clicking into any specific sync will open up the sync stages window where you can get a more detailed view of what was extracted. \
\
For some integrations, there will be an option for both pulling and [pushing metadata](../features/push-metadata-to-source.md).&#x20;

<figure><img src="../.gitbook/assets/Screenshot 2024-02-09 at 4.29.12 PM.png" alt=""><figcaption></figcaption></figure>

### **Schedule**

The schedule settings allow you to set a schedule that extractions will follow (e.g. daily, every 7 days). Please enter a cron expression to schedule the extractions. For example, 0 0 \* \* \* will schedule the extractions to run every day at midnight UTC.&#x20;

<figure><img src="../.gitbook/assets/Screenshot 2024-02-09 at 12.15.41 PM.png" alt=""><figcaption></figcaption></figure>

### **Schema**&#x20;

The schema settings allow you to select specific schemas/groups that you would like metadata extracted from the source. The resources associated with the selected schemas/groups will be imported into the workspace and be visible in the catalog view.&#x20;

### **Popularity**

The [popularity](../features/popularity.md) of a data resource in Secoda is calculated based on the number of times it has been queried or viewed in the last 24 hours, pulled directly from the Source.

This section allows you to uncheck service accounts to prevent their queries from counting towards resource popularity.&#x20;

<figure><img src="../.gitbook/assets/Screenshot 2024-02-09 at 4.30.41 PM.png" alt=""><figcaption></figcaption></figure>

### **Permissions**

The Permissions section allows you to control who was access to see [Previews](../features/data-previews.md) and which Editors can run [Queries](../features/queries/running-queries-in-secoda/) for the integration.&#x20;

<figure><img src="../.gitbook/assets/Screenshot 2024-02-09 at 4.34.30 PM.png" alt=""><figcaption></figcaption></figure>

### **Preferences**&#x20;

The preferences section allows you to configure whether you want to always use the integration source for resource descriptions or the definition added in Secoda. If you choose to enable the descriptions from source, changes made to the descriptions in Secoda will be overwritten to match the source description. \
\


<figure><img src="../.gitbook/assets/Screenshot 2024-02-09 at 4.36.26 PM.png" alt=""><figcaption></figcaption></figure>

You can also disable automatically removing resources that are not in subsequent extractions for this integration. Normally, when a resource is not in a subsequent extraction, it is removed from the workspace. With this setting enabled, these resources will still be accessible in the workspace.&#x20;

## Removing an Integration&#x20;

To remove an integration, simply select the integration and delete it from the integrations page.&#x20;

{% embed url="https://www.loom.com/share/5046d7ee0e6f4b479d219c9daeefe7f6?sid=8e402714-3d3e-48db-845f-2945423d55cd" %}

{% hint style="warning" %}
Deleting an integration from the workspace will remove all associated resources. Adding the integration back will not preserve the changes (e.g. metadata updates) that were made when originally connected and rather will act as a new integration.&#x20;
{% endhint %}
