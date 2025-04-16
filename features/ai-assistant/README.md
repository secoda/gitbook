---
description: This page will go over the Secoda AI functionality.
---

# Secoda AI

{% hint style="info" %}
"LLM provider" refers to OpenAI or Anthropic. Workspace admins can choose which provider they use in their AI settings.
{% endhint %}

## Overview

The Secoda Secoda AI enhances your data stack by providing a powerful chat interface that allows anyone in your organization to retrieve data insights.

Secoda AI is powered by OpenAI and Anthropic's API. Workspace admins currently have the choice of using OpenAI's GPT-4o model or Anthropic's Claude Sonnet 3.5 model. Read more about Secoda AI's security posture in our [security.md](security.md "mention").

Secoda's AI can help you with documentation, query building, institutional knowledge discovery.

## **Enabling the Secoda AI**

By default, Secoda AI is disabled. To activate it:

1. Navigate to [Settings](../../readme/secoda-as-an-admin/settings.md) > AI.
2. Toggle on the Secoda AI.
3. Once enabled, the Secoda AI will appear in the left-hand menu of your workspace.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/8efa4541-d0fa-4a06-bc40-9c7afb51683a.png" alt=""><figcaption><p>Toggle on AI</p></figcaption></figure>

## **AI Settings for Admins**

Admins can customize AI settings to align with workspace preferences and security protocols:

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/ab0017ec-1f2a-4786-b58f-157e5a5b9a59.png" alt=""><figcaption><p>AI Settings</p></figcaption></figure>

### **LLM**

Secoda provides the option to choose between two LLMs in your [Secoda AI settings](https://app.secoda.co/settings/ai):

1. **Anthropic Claude Sonnet 3.5**
2. **OpenAI GPT 4o**

Both models excel at different things so we encourage teams to experiment with the models to see which performs better for your use cases.

<figure><img src="../../.gitbook/assets/image (91).png" alt=""><figcaption></figcaption></figure>

### **Governance**

AI Governance in Secoda empowers organizations to control the data accessed by AI, enhancing security and data relevance.

#### Key Features:

* **Customizable Filters:** Admins can specify which resources are accessible to the AI by setting inclusive or exclusive filter rules. This ensures that AI interactions are confined to appropriate datasets.
* **Consistent Configuration:** The filter rules for AI are aligned with [those used on the Search and Catalog pages](../filters.md), ensuring a unified approach to data governance across the platform.

#### Benefits:

* **Enhanced Data Security:** Restricts AI access to sensitive or non-production data, minimizing potential exposure.
* **Improved Data Relevance:** Focuses AI interactions on current and verified data, increasing the accuracy and reliability of the insights provided.

By implementing these rules, Admins can tailor AI capabilities to fit organizational needs and compliance requirements, ensuring that only relevant and secure data is queried.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/c3e3c238-b7ba-4c66-8a05-c55abdbf2a77.png" alt=""><figcaption><p>AI Governance Filters</p></figcaption></figure>

### Tools

* **Run SQL:** Executes SQL queries within Secoda to support doing analysis.
* **Add memory:** Saves personal preferences for an individual user, for example, language preference.
* **Get Secoda docs:** Searches https://docs.secoda.co for any product related questions.

{% hint style="info" %}
**To ensure security and relevance:**

**Team-Based Replies:** Our AI strictly adheres to Team-based data access permissions. If a user asks about resources from a Team that they are not a part of, the AI will not return any results.

**Query Execution Requirements**: The AI will only execute a query if both of the following conditions are met:

1. `run_sql` is toggled on in the AI settings.
2. **The user asking the question has Query access** for the specific integration, which can be managed by admins in the Integration Permissions settings.

This ensures that only authorized users can run queries on sensitive or critical data, maintaining control over data access.
{% endhint %}

### **Custom Instructions**

#### Chat

Admins can set specific instructions for the AI to follow, enhancing control and relevance.

Some examples that we've seen work well:

> * Do not index on resources tagged with "archived" or "deprecated" or "stale".
> * Only provide results on "Verified" resources.
> * Only provide results on Published resources - do not include resources that are still in Draft.
> * Only reference tables and views from the production analytics schema in Snowflake, never use data from the RAW database.

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

### Agents

Secoda AI Agents are customizable assistants tailored to specific roles, aligning with team workflows. They access relevant data, support unique instructions, and integrate with tools like Slack. Personas can be personalized with names, icons, and permissions, ensuring the right people use the right tools for enhanced productivity.

#### Configuration

To create an AI Agent, open the [AI settings](https://app.secoda.co/settings/ai) and expand the "Agents" section and click the "Create Agent" button.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/4206c7f9-c60f-437d-9258-ea53657c3556.png" alt="" width="563"><figcaption></figcaption></figure>

Each Agent can be configured with the following details:

* **Name**: Give your Agent a unique name.
* **Icon**: Select an icon that represents the Agent.
* **Description**: Add a brief description of the Agent's purpose.
* **Custom Instructions**: Set specific instructions for the Agent’s role and tasks.
* **Resource Filters**: Limit the Agent’s access to certain datasets or resources.
* **Team Access**: Control which teams or users can access this Agent.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/431656c4-124f-4801-9387-5e25ec4d6e1f.png" alt="" width="563"><figcaption></figcaption></figure>

Once your Agent has been created, you can switch between Agents on the Secoda AI page. After that you can chat with your Secoda AI Agent similar to how you chat with Secoda AI.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/d01b9fdc-c295-44fd-b8d6-3aade6cbc0e0.png" alt="" width="563"><figcaption></figcaption></figure>

### Memory

Secoda AI Memory allows Secoda AI to remember important details about your preferences and working style across conversations. This personalization feature helps make interactions more efficient and contextual over time.

**Enabling AI Memory**

AI Memory can be enabled by workspace administrators through the AI settings page:

* Navigate to Settings > AI
* Ensure "Use Secoda AI" is enabled
* Look for the Personalization section
* Click "Manage Memories" to view and manage stored memories

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

**Managing Memories**

You can view and manage all memories that Secoda AI has stored:

* Click "Manage Memories" in the AI settings
* View a list of all stored memories
* Delete any memories you no longer want the AI to remember

**How It Works**

When you interact with Secoda AI, it automatically identifies and stores important details about your preferences and working patterns. These memories are then used to:

* Provide more personalized responses
* Reduce repetitive questions
* Maintain context across different conversations
* Tailor recommendations to your specific needs

For example, if you frequently work with specific databases or dashboards, the AI will remember these preferences and prioritize them in future interactions.

<figure><img src="../../.gitbook/assets/image (93).png" alt=""><figcaption></figcaption></figure>

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
