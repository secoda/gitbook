---
description: This page will go over the Secoda AI functionality.
---

# Secoda AI

Explore plans which include Secoda AI [here](https://www.secoda.co/pricing).

## Overview

The Secoda Secoda AI enhances your data stack by providing a powerful chat interface that allows anyone in your organization to retrieve data insights.&#x20;

Secoda's Secoda AI is powered by [OpenAI's APIs](https://openai.com/product), which sit atop the GPT4 Large Language Model. We are updated to the latest version of GPT -- [GPT-4o](https://platform.openai.com/docs/models/gpt-4o).&#x20;

By sharing **only** the metadata in your workspace with OpenAI, Secoda's AI Assistant can help you with documentation, query building, institutional knowledge discovery, all while safeguarding your metadata!

## **Enabling the Secoda AI**

By default, Secoda AI is disabled. To activate it:

1. Navigate to [Settings](../../readme/secoda-as-an-admin/settings.md) > AI.
2. Toggle on the Secoda AI.
3. Once enabled, the Secoda AI will appear in the left-hand menu of your workspace.

<figure><img src="../../.gitbook/assets/image (33).png" alt=""><figcaption><p>Toggle on AI</p></figcaption></figure>

## **AI Settings for Admins**

Admins can customize AI settings to align with workspace preferences and security protocols:

<figure><img src="../../.gitbook/assets/image (34).png" alt=""><figcaption><p>AI Settings</p></figcaption></figure>

### **Governance**

AI Governance in Secoda empowers organizations to control the data accessed by AI, enhancing security and data relevance.&#x20;

#### Key Features:

* **Customizable Filters:** Admins can specify which resources are accessible to the AI by setting inclusive or exclusive filter rules. This ensures that AI interactions are confined to appropriate datasets.
* **Consistent Configuration:** The filter rules for AI are aligned with [those used on the Search and Catalog pages](../filters.md), ensuring a unified approach to data governance across the platform.

#### Benefits:

* **Enhanced Data Security:** Restricts AI access to sensitive or non-production data, minimizing potential exposure.
* **Improved Data Relevance:** Focuses AI interactions on current and verified data, increasing the accuracy and reliability of the insights provided.

By implementing these rules, Admins can tailor AI capabilities to fit organizational needs and compliance requirements, ensuring that only relevant and secure data is queried.

<figure><img src="../../.gitbook/assets/Screenshot 2024-06-20 at 12.23.40 PM.png" alt=""><figcaption><p>AI Governance Filters</p></figcaption></figure>

### Agent Tools

* By default, tools like `search_resources`, `search_knowledge`, `catalog_search`, `retrieve_entity`, and `entity_link` are enabled to ensure comprehensive search capabilities across the workspace.
* The `run_sql` tool, disabled by default, allows the AI to execute SQL queries directly on your connected integrations. This tool can provide answers to data queries but can be disabled if there are security concerns. Users can ask questions like "How many customers do we have?" and getting a numeric answer instead of pointing the user to a guiding resource or query. The AI will also provide the user with the steps that it took to find that answer, including any SQL queries it ran on the backend to provide more context.

{% hint style="info" %}
**To ensure security and relevance:**

**Team-Based Replies:** Our AI strictly adheres to Team-based data access permissions. If a user asks about resources from a Team that they are not a part of, the AI will not return any results.

**Query Execution Requirements**: The AI will only execute a query if both of the following conditions are met:

1. `run_sql` is toggled on in the AI settings.
2. **The user asking the question has Query access** for the specific integration, which can be managed by admins in the Integration Permissions settings.

This ensures that only authorized users can run queries on sensitive or critical data, maintaining control over data access.
{% endhint %}

### **Custom Instructions**&#x20;

#### Chat

Admins can set specific instructions for the AI to follow, enhancing control and relevance.

Some examples that we've seen work well:

> * Do not index on resources tagged with "archived" or "deprecated" or "stale".
> * Only provide results on "Verified" resources.
> * Only provide results on Published resources - do not include resources that are still in Draft.
> * Only reference tables and views from the production analytics schema in Snowflake, never use data from the RAW database.&#x20;

{% hint style="info" %}
By default, both Published and Draft resources are included in Secoda AI responses. This can be controlled using the custom instructions to restrict this to only Published resources, for example.
{% endhint %}

#### Descriptions

Admins are able to define custom instructions to the [ai-description-editor.md](../../resource-and-metadata-management/add-documentation/ai-description-editor.md "mention") so that you can define documentation standards and a format for it to follow.

Some examples that we've seen work well:

> * Add "AI-Generated" to the end of each description added, to indicate to users that a human didn't come up with this definition.
> * Do not reference the database, schema, table information in the description (this information is obvious in Secoda)
> * Do not use full, wordy sentences. Be brief and include only the necessary facts.
> * Descriptions should be concise and not editorialized. Do not describe the data as 'essential' or 'critical'; only describe the contents.
> * All tables and columns are related to insurance. Keep this in mind when generating descriptions.

### Personas

Secoda AI Personas are customizable assistants tailored to specific roles, aligning with team workflows. They access relevant data, support unique instructions, and integrate with tools like Slack. Personas can be personalized with names, icons, and permissions, ensuring the right people use the right tools for enhanced productivity.

#### Configuration

To create an AI Persona, open the [AI settings](https://app.secoda.co/settings/ai) and expand the "Personas" section and click the "Create Persona" button.

<figure><img src="../../.gitbook/assets/image (43).png" alt="" width="563"><figcaption></figcaption></figure>

Each Persona can be configured with the following details:

* **Name**: Give your Persona a unique name.
* **Icon**: Select an icon that represents the Persona.
* **Description**: Add a brief description of the Persona's purpose.
* **Custom Instructions**: Set specific instructions for the Persona’s role and tasks.
* **Resource Filters**: Limit the Persona’s access to certain datasets or resources.
* **Team Access**: Control which teams or users can access this Persona.

<figure><img src="../../.gitbook/assets/image (45).png" alt="" width="563"><figcaption></figcaption></figure>

Once your Persona has been created, you can switch between Personas on the Secoda AI page. After that you can chat with your Secoda AI Persona similar to how you chat with Secoda AI.

<figure><img src="../../.gitbook/assets/image (44).png" alt="" width="563"><figcaption></figcaption></figure>



## **Future Improvements**&#x20;

Looking ahead, we are committed to enhancing the Secoda AI Assistant with:

* Improved response times and reliability.
* Enhanced understanding of complex prompts.
* Tailored responses based on user roles and access levels.

## Additional documentation

{% content-ref url="best-practices.md" %}
[best-practices.md](best-practices.md)
{% endcontent-ref %}

{% content-ref url="secoda-ai-use-cases.md" %}
[secoda-ai-use-cases.md](secoda-ai-use-cases.md)
{% endcontent-ref %}

{% content-ref url="security.md" %}
[security.md](security.md)
{% endcontent-ref %}

{% content-ref url="prompts.md" %}
[prompts.md](prompts.md)
{% endcontent-ref %}

This guide ensures that Admins are equipped to optimize the AI Assistant within their Secoda environment, driving efficient and secure data operations across the organization.

{% hint style="info" %}
Secoda AI Assistant is only available for Version 7.0.0 and up.
{% endhint %}
