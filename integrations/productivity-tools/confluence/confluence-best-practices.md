---
description: Best practices on integrating Confluence in Secoda
---

# Confluence best practices

## Confluence integration with Secoda

Integrating Confluence with Secoda allows content built in Confluence to become discoverable, searchable, and editable within Secoda's [Documents](../../../features/documents/) feature. This guide outlines various usage scenarios and best practices we've observed to be successful among our customers.

## Initial Confluence sync

When initiating the sync process between Confluence and Secoda, it's important to note that resources can only be selected at the _Space_ level within Confluence for importation into Secoda. If you wish to include only specific sections or Pages, you have the option to create a new Space in Confluence containing only the desired pages, and subsequently sync that designated Space with Secoda. This approach allows for more precise control over the content being brought over.

## Defining your source of truth

You'll want to decide which tool you'd like to be considered the source of truth. **Changes made to Confluence documents in Secoda will not be persisted back to Confluence.** For example, if a document is imported from Confluence and then edited in Secoda, it will become out of sync with its Confluence counterpart. Deciding whether Secoda or Confluence will be your source of truth informs users which platform hosts the most current information.

### **Secoda as the source of truth**

Use Secoda as the source of truth if the documents will no longer be edited within Confluence. A main use case for this method is if you plan to move over all of your documentation to Secoda, and move off of Confluence.

1. Connect the Confluence integration and perform a one time import of the desired documents. Do not schedule or run any future extractions.
2. Rearrange the documents, add them to Collections, Teams etc.
3. Make edits to them, add charts and other formatting edits etc.

{% hint style="info" %}
Be aware that subsequent syncs will override any edits made in Secoda with the original Confluence content.
{% endhint %}

### **Confluence as the source of truth**

Use Confluence as the source of truth if the documents will continue to be edited within Confluence, but you'd like to have these documents be searchable and discoverable in Secoda. A main use case for this method is if your users will continue using Confluence as their main documentation editor, but you'd like to still have this context in Secoda.

1. Connect the Confluence integration and set a schedule of how often you'd like it to be run.
2. Consider setting imported Confluence documents to Read-Only in Secoda to maintain consistency and prevent accidental edits:
   1. **Create an** [**Automation**](../../../features/automations.md) **to Add Docs to a Collection**: Automatically add all Confluence documents to a specific Collection within Secoda.
   2. **Set Read-Only Permissions**: Configure the Collection [permissions](../../../features/sharing-resources.md) to be "Can read" for all users. This prevents editing and ensures that documents are only **viewed** within Secoda, since edits cannot be pushed from Secoda > Confluence.
3. Identify Confluence documents in Secoda through the Source property in the [Sidebar](../../../resource-and-metadata-management/resource-sidebar.md). If you'd like to identify these documents more clearly, we'd recommend making a [Custom Tag](../../../resource-and-metadata-management/tags/custom-tags.md) called Confluence, and adding it to the documents.&#x20;

{% hint style="info" %}
Bringing these documents into Secoda allows them to be searchable and discoverable by [Search](../../../features/search.md) and the [AI Assistant](../../../features/ai-assistant/). It also allows you to relate documents to existing resources, such as tables and dashboards. However, there are less capabilities when it comes to organizing, formatting and editing these pages.
{% endhint %}
