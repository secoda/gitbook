# Confluence best practices

## Confluence integration with Secoda

With the Confluence integration, you can sync the content that you've built out in Confluence into Secoda's [Documents](../../../features/documents/) feature. This allows it to be discoverable, searchable and editable for your Secoda users. There are a few ways to use this integration and we've put together some best practices that we've seen work successfully for our customers.

You'll want to decide which tool you'd like to be considered the source of truth. **Changes made to Confluence documents in Secoda will not be persisted back to Confluence.** For example, if you have brought in a Document and then decide to make edits on it within Secoda. That document will then become out of sync with the one in Confluence. We recommend choosing between Secoda or Confluence being your source of truth so that your users know which one to trust as the most up to date resource.

## **Secoda as the source of truth**

Use Secoda as the source of truth if the documents will no longer be edited within Confluence. A main use case for this method is if you plan to move over all of your documentation to Secoda, and move off of Confluence.

1. Connect the Confluence integration and do a one time load of the document(s) you'd like brought in (do not run any future extractions).
2. Move them around, add them to Collections, Teams etc.
3. Make edits to them, add charts and other formatting edits etc.

{% hint style="info" %}
If another sync is preformed, the edits you make in Secoda will not persist. The documents will revert to whatever is in Confluence, and any edits or changes in Secoda will be removed.
{% endhint %}

## **Confluence as the source of truth**

Use Confluence as the source of truth if the documents will continue to be edited within Confluence, but you'd like to have these documents be searchable and discoverable. A main use case for this method is if your users will continue using Confluence as their main documentation editor, but you'd like to still have this context in Secoda.

1. Connect the Confluence integration and set a schedule of how often you'd like it to be run.
2. Identify Confluence documents in Secoda through the Source property in the [Sidebar](../../../resource-and-metadata-management/resource-sidebar.md). If you'd like to identify these documents more clearly, we'd recommend making a [Custom Tag](../../../resource-and-metadata-management/tags/custom-tags.md) called Confluence, and adding it to the documents.&#x20;

{% hint style="info" %}
Bringing these documents into Secoda allows them to be searchable and discoverable by [Search](../../../features/search.md) and the [AI Assistant](../../../features/ai-assistant/). It also allows you to relate documents to existing resources, such as tables and dashboards. However, there are less capabilities when it comes to organizing, formatting and editing these pages.
{% endhint %}
