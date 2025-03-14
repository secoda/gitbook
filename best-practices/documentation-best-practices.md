---
description: >-
  Use cases for using Secoda to automate repetitive documentation tasks, saving
  time for your data team.
---

# Documentation best practices

By leveraging Secoda, data teams can automate manual and repetitive tasks which would improve these processes in terms of efficiency. This page provides some common solutions for leveraging Secoda's features to save time.

{% hint style="info" %}
Note: When making edits to descriptions in Secoda, ensure that you have the [integration's permissions set ](../integrations/integration-settings.md#permissions)so that descriptions made in Secoda persist.&#x20;
{% endhint %}

## Automate enrichment within Secoda

[best-practices.md](../features/ai-assistant/best-practices.md "mention")

* Our AI Assistant can be utilized in many ways, and we find it extremely powerful when it comes to documentation.
* The AI Assistant is available in the sidebar on each resource in your workspace. Simply ask it to write up documentation on a resource that you're clicked into to generate rich documentation in just seconds. Check out the video resource here: [#how-to-use-the-ai-assistant](../features/ai-assistant/best-practices.md#how-to-use-the-ai-assistant "mention").
* The [ai-description-editor.md](../resource-and-metadata-management/add-documentation/ai-description-editor.md "mention") can similarly be used to generate descriptions of your resources with just one click. This can be done on the Catalog resources, Dictionary metrics and Collections.

&#x20;[automations.md](../features/automations.md "mention")

* Define rules once for updating documentation, and have these automatically updated on a set cadence
* Automations can make updates to tags, descriptions, owners as well as help organize your workspace by moving resources to specific Teams or Collections, for example

[bulk-editing-resources.md](../resource-and-metadata-management/add-documentation/bulk-editing-resources.md "mention")

* Check out our bulk editing features to make bulk metadata edits to your resources

[#importing-metadata-into-secoda](../resource-and-metadata-management/import-and-export-data.md#importing-metadata-into-secoda "mention")

* Create a CSV to bulk import metadata for resources already existing in Secoda. For example, if you have descriptions for your Oracle assets living in a G-sheet, you can upload these onto your existing resources in Secoda.

[propagating-metadata.md](../resource-and-metadata-management/add-documentation/propagating-metadata.md "mention")

* You might find that a lot of your data resources are related, and it can become redundant having to manually update resources that should have the same tags and owners, for example.
* Our propagate metadata feature allows you to bulk edit these related resources!
* End result:
  * Reduced time spent on documentation
  * Improved documentation and data literacy

[auto-pii-tagging.md](../resource-and-metadata-management/tags/auto-pii-tagging.md "mention")

* The PII Identifier automatically flags potential PII data assets across your workspace by searching for keywords.
* You can even customize the list of keywords depending on how your organization defines personal information.

[Slack AI Assistant](../extensions/slack-connection/slack-user-guide.md#secoda-ai-slackbot)

* With the Slack integration, you have the ability to ask the AI Assistant questions in Slack, get a response, and then automatically push those answers into your workspace.
* This means less redundancy with answering questions and additional documentation in the product.

[secoda-api.md](../secoda-api.md "mention")

* Use Secoda's APIs to bulk edit the name, descriptions, and tags on your resources.
* Automatic PII detection through the API can identify resources that need to be more governed for auditing purposes
  * PII can be tagged, and automatic reporting for audits can be generated

## Identify what needs to be documented

If you'd like to identify which resources have not been documented yet, you can do so by following these steps to [#search-within-the-catalog](../features/search.md#search-within-the-catalog "mention").

If you'd like to be notified of changes that may result in a need for updated documentation, you can subscribe to schema change notifications for those particular resources. Set those up here[#h\_3a4bfd6458](../features/notifications.md#h_3a4bfd6458 "mention").



**Try out our** [**ROI Calculator**](https://www.secoda.co/data-discovery-roi-calculator) **to estimate how much money your team could save by automating tasks with Secoda.**
