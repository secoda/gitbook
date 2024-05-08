---
description: This page will go over the AI Assistant functionality.
---

# AI Assistant

{% hint style="info" %}
Explore plans which include our AI Assistant [here](https://www.secoda.co/pricing).
{% endhint %}

## Overview

The Secoda AI Assistant enhances your data stack by providing a powerful chat interface that allows anyone in your organization to retrieve data insights.&#x20;

Secoda's AI Assistant is powered by [OpenAI's APIs](https://openai.com/product), which sit atop the GPT4 Large Language Model. We are updated to the latest version of GPT -- GPT4 Turbo.&#x20;

By sharing **only** the metadata in your workspace with OpenAI, Secoda's AI Assistant can help you with documentation, query building, institutional knowledge discovery, all while safeguarding your metadata!

## **Enabling the AI Assistant**&#x20;

By default, the AI Assistant is disabled. To activate it:

* Navigate to Settings > AI.
* Toggle on the AI Assistant.
* Once enabled, the AI Assistant will appear in the left-hand menu of your workspace.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/Screenshot%202023-04-26%20at%202.23.16%20PM.png" alt=""><figcaption><p>Screenshot showing how to enable AI Search in the Workspace Settings.</p></figcaption></figure>

Admins can customize AI settings to align with workspace preferences and security protocols:

<figure><img src="../../.gitbook/assets/Screenshot 2024-05-08 at 2.40.52 PM.png" alt=""><figcaption><p>AI Settings</p></figcaption></figure>

#### Agent Tools

* By default, tools like `search_resources`, `search_knowledge`, `catalog_search`, `retrieve_entity`, and `entity_link` are enabled to ensure comprehensive search capabilities across the workspace.
* The `run_sql` tool, disabled by default, allows the AI to execute SQL queries directly on your connected integrations. This tool can provide answers to data queries but can be disabled if there are security concerns. Users can ask questions like "How many customers do we have?" and getting a numeric answer instead of pointing the user to a guiding resource or query. The AI will also provide the user with the steps that it took to find that answer, including any SQL queries it ran on the backend to provide more context.

#### **Custom Instructions**&#x20;

Admins can set specific instructions for the AI to follow, enhancing control and relevance.

Some examples that we've seen work well:

> * Do not index on resources tagged with "archived" or "deprecated" or "stale".
> * Only provide results on "Verified" resources.
> * Only provide results on Published resources - do not include resources that are still in Draft.
> * Only reference tables and views from the production analytics schema in Snowflake, never use data from the RAW database.&#x20;

#### Descriptions custom instructions

Admins are able to define custom instructions to the [ai-description-editor.md](../../resource-and-metadata-management/add-documentation/ai-description-editor.md "mention") so that you can define documentation standards and a format for it to follow.

Some examples that we've seen work well:

> * Add "AI-Generated" to the end of each description added, to indicate to users that a human didn't come up with this definition.
> * Do not reference the database, schema, table information in the description (this information is obvious in Secoda)
> * Do not use full, wordy sentences. Be brief and include only the necessary facts.
> * All tables and columns are related to insurance. Keep this in mind when generating descriptions.

## **Future Improvements**&#x20;

Looking ahead, we are committed to enhancing the Secoda AI Assistant with:

* Improved response times and reliability.
* Enhanced understanding of complex prompts.
* Tailored responses based on user roles and access levels.

This guide ensures that Admins are equipped to optimize the AI Assistant within their Secoda environment, driving efficient and secure data operations across the organization.

{% hint style="info" %}
Secoda AI Assistant is only available for Version 7.0.0 and up.
{% endhint %}
