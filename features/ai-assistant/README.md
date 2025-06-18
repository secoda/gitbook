---
description: This page will go over the Secoda AI functionality.
---

# Secoda AI

{% hint style="info" %}
"LLM provider" refers to OpenAI or Anthropic.
{% endhint %}

## Overview

The Secoda Secoda AI enhances your data stack by providing a powerful chat interface that allows anyone in your organization to retrieve data insights.

Secoda AI is powered by Anthropic's Claude Sonnet 4 and Opus 4 models. Read more about Secoda AI's security posture in our [security.md](security.md "mention").

Secoda's AI can help you with documentation, query building, institutional knowledge discovery.

## **Enabling Secoda AI**

By default, Secoda AI is disabled. To activate it:

1. Navigate to [Settings](../../readme/secoda-as-an-admin/settings.md) > AI.
2. Toggle on the Secoda AI.
3. Once enabled, the Secoda AI will appear in the left-hand menu of your workspace.

<figure><img src="../../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

## **Charting**

Secoda AI Charting enables users to create data visualizations through natural language prompts, making data insights accessible without requiring SQL or charting expertise.

Secoda AI Charting allows users to describe the charts they want in plain English (e.g., "Show monthly revenue trends"). The system analyzes your data to suggest appropriate visualization types and provides contextual explanations of insights.Users can refine visualizations through conversational follow-ups to adjust chart types, add trendlines, or change grouping parameters.

Simply navigate to the Secoda AI interface, ask a question involving data visualization, and request a chart based on SQL results. The feature integrates seamlessly with the SQL query functionality, allowing you to save both queries and their visualizations.For best results, be specific about metrics, dimensions, and time periods in your requests. The AI will guide you through creating the most effective visualization for your data story.

## **AI Settings**

Admins can customize AI settings to align with workspace preferences and security protocols:

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

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

### Personas

Secoda AI Personas are customizable assistants tailored to specific roles, aligning with team workflows. They access relevant data, support unique instructions, and integrate with tools like Slack. Personas can be personalized with names, icons, and permissions, ensuring the right people use the right tools for enhanced productivity.

#### Configuration

To create an AI Persona, open the [AI settings](https://app.secoda.co/settings/ai) and expand the "Personas" section and click the "Create Persona" button.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/4206c7f9-c60f-437d-9258-ea53657c3556.png" alt="" width="563"><figcaption></figcaption></figure>

Each Persona can be configured with the following details:

* **Name**: Give your Persona a unique name.
* **Icon**: Select an icon that represents the Persona.
* **Description**: Add a brief description of the Persona's purpose.
* **Custom Instructions**: Set specific instructions for the Persona's role and tasks.
* **Resource Filters**: Limit the Persona’s access to certain datasets or resources.
* **Team Access**: Control which teams or users can access this Persona.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/431656c4-124f-4801-9387-5e25ec4d6e1f.png" alt="" width="563"><figcaption></figcaption></figure>

Once your Persona has been created, you can switch between Personas on the Secoda AI page. After that you can chat with your Secoda AI Persona similar to how you chat with Secoda AI.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/d01b9fdc-c295-44fd-b8d6-3aade6cbc0e0.png" alt="" width="563"><figcaption></figcaption></figure>

### Memory

Secoda AI Memory allows Secoda AI to remember important details about your preferences and working style across conversations. This personalization feature helps make interactions more efficient and contextual over time.

**Enabling AI Memory**

AI Memory can be enabled by workspace administrators through the AI settings page:

* Navigate to Settings > AI
* Ensure "Use Secoda AI" is enabled
* Look for the Personalization section
* Click "Manage Memories" to view and manage stored memories

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

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

### Advanced Memory

Advanced Memory enables Secoda AI to learn from past interactions across the entire workspace, improving response quality and efficiency over time. Secoda AI analyzes past successful AI interactions to identify patterns and strategies that work well. This knowledge is then applied to future conversations to provide better assistance.

#### Key Features

**Interaction Analysis:** The system automatically analyzes completed AI interactions to identify:

* **Successful strategies:** Tool sequences and reasoning approaches that led to correct solutions
* **Common pitfalls:** Where the AI initially failed but later succeeded, noting breakthrough moments
* **Efficient workflows:** Optimal tool usage patterns and data retrieval paths
* **Effective approaches:** Information synthesis methods that produced good results

**Knowledge Accumulation:** The system builds a workspace-level knowledge base that includes:

* Which tools work best for different query types
* Effective error recovery strategies
* Successful information synthesis approaches
* Common dead ends to avoid

**Automatic Learning:** After each user-generated AI interaction, the system:

1. Analyzes the conversation for patterns and insights
2. Updates the workspace knowledge base with new learnings
3. Applies these insights to improve future interactions

#### Benefits

**Enhanced Accuracy:** By learning from past successes and failures, the AI becomes more accurate in similar future scenarios.

**Improved Efficiency:** The AI learns optimal tool sequences and approaches, reducing the number of steps needed to reach correct answers.

**Workspace-Specific Intelligence:** The knowledge base is tailored to your organization's specific data patterns, terminology, and common use cases.

**Continuous Improvement:** The system continuously learns and adapts, becoming more effective over time as it processes more interactions.

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

{% content-ref url="broken-reference" %}
[Broken link](broken-reference)
{% endcontent-ref %}

This guide ensures that Admins are equipped to optimize the AI Assistant within their Secoda environment, driving efficient and secure data operations across the organization.

{% hint style="info" %}
Secoda AI Assistant is only available for Version 7.0.0 and up.
{% endhint %}
