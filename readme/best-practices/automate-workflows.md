---
description: >-
  Use cases for using Secoda to automate repetitive tasks, saving time for your
  data team.
---

# Documentation best practices

By leveraging Secoda, data teams can automate manual and repetitive tasks which would improve these processes in terms of efficiency. This page provides some common solutions for leveraging Secoda's features to save time.

## Automate enrichment within Secoda

[ai-description-editor.md](../../resource-and-metadata-management/add-documentation/ai-description-editor.md "mention")

* Our AI Assistant can be utilized in many ways, and we find it extremely powerful when it comes to documentation.
* The Assistant reads the metadata in your workspace and can generate descriptions of your resources with just one click. This can be done on the Catalog resources, Dictionary metrics and Collections.

[propagating-metadata.md](../../resource-and-metadata-management/add-documentation/propagating-metadata.md "mention")

* You might find that a lot of your data resources are related, and it can become redundant having to manually update resources that should have the same tags and owners, for example.
* Our propagate metadata feature allows you to bulk edit these related resources!
* End result:
  * Reduced time spent on documentation
  * Improved documentation and data literacy

[bulk-editing-resources.md](../../resource-and-metadata-management/add-documentation/bulk-editing-resources.md "mention")

* Use our bulk editing feature to make bulk metadata edits to your resources with a drag down shortcut similar to Excel's

[auto-pii-tagging.md](../../resource-and-metadata-management/tags/auto-pii-tagging.md "mention")

* The PII Identifier automatically flags potential PII data assets across your workspace by searching for keywords.
* You can even customize the list of keywords depending on how your organization defines personal information.

[slack-ai-assistant.md](../../integrations/productivity-tools/slack-connection/slack-ai-assistant.md "mention")

* With the Slack integration, you have the ability to ask the AI Assistant questions in Slack, get a response, and then automatically push those answers into your workspace.
* This means less redundancy with answering questions and additional documentation in the product.

[secoda-api.md](../../secoda-api.md "mention")

* Use Secoda’s APIs to bulk edit the name, descriptions, and tags on your resources.
* Automatic PII detection through the API can identify resources that need to be more governed for auditing purposes
  * PII can be tagged, and automatic reporting for audits can be generated

## Automate deprecating unused, stale data

ROT data (Redundant, Obsolete, Trivial) is data that is no longer relevant or of use to an organization. We encourage you to minimize the amount of ROT data by automating some of this clean up.

[secoda-api.md](../../secoda-api.md "mention")&#x20;

* Can identify large amounts of unused and duplicate tables, then deprecate these
* End result:
  * Reduced time identifying this data manually
  * Improved data quality and security
  * Improved productivity for analysts trying to find the right data
  * Reduced costs on data storage

[removing-stale-data.md](../../features/removing-stale-data.md "mention")

* Identifies and hides any stale data across your workspace

## Identify what needs to be documented

If you'd like to identify which resources have not been documented yet, you can do so by following these steps to [#search-within-the-catalog](../../features/search-and-home-page.md#search-within-the-catalog "mention").

If you'd like to be notified of changes that may result in a need for updated documentation, you can subscribe to schema change notifications for those particular resources. Set those up here[#h\_3a4bfd6458](../../features/notifications.md#h\_3a4bfd6458 "mention").



**Try out our** [**ROI Calculator**](https://www.secoda.co/data-discovery-roi-calculator) **to estimate how much money your team could save by automating tasks with Secoda.**
