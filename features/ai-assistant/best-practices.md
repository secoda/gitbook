---
description: >-
  This page will review the best ways to use Secoda AI to get the most effective
  results.
---

# Secoda AI User Guide

Secoda AI enhances your ability to quickly find information and document resources within your workspace using a simple, chat-like interface. This guide will help you understand how to effectively use the AI Assistant both within the Secoda platform and in your everyday workflows.

## **How to Use Secoda AI**

**1. Engaging with Secoda AI:**

* **Accessing:** Click into the Secoda AI window within the Secoda UI to start an interaction. You can also find the AI Assistant on all resource pages (see video below).
* **Chatting:** Simply type your question in plain language and receive answers directly in the chat. Check out some [secoda-ai-use-cases.md](secoda-ai-use-cases.md "mention") to help you get started in understanding the power of this feature.
* **Automating Documentation:** Use the AI to automatically generate descriptions for your metadata with just one click [ai-description-editor.md](../../resource-and-metadata-management/add-documentation/ai-description-editor.md "mention").

{% embed url="https://www.loom.com/share/473aad77e80c41caa8e252f7ac2d568b?sid=b0657b9d-6f0f-419c-9719-259bda14ebaa" %}

{% hint style="info" %}
**AI Governance:** Every resource's sidebar in Secoda includes AI Governance settings. This section informs you if the AI is permitted to access the data from that source and if it will include it in its responses. This ensures that AI interactions comply with your organization’s data governance policies.
{% endhint %}

**2. Incorporating AI in Your Workflows:**

* **Slack Integration:** Connect the AI Assistant to your Slack workspace to streamline your data-related queries[#secoda-ai-slackbot](../../extensions/slack-connection/slack-user-guide.md#secoda-ai-slackbot "mention").
* **Chrome Browser Extensions:** Use the Chrome extension to [#chat-with-secoda-ai](../../extensions/chrome-extension.md#chat-with-secoda-ai "mention") directly from other data tools like Tableau and Snowflake.

## **Best Practices for Interacting with Secoda AI**

**1. Understand Data Query Capabilities**

Verify with your workspace Admin whether the AI Assistant can **run direct data queries**. If enabled, you can ask data-specific questions like "How many customers do we have?" and get the number in just a few seconds. Clicking "Show steps" will provide you with the steps that it took to find that answer, including any SQL queries it ran on the backend to provide more context.

{% embed url="https://www.loom.com/share/96ca735fa5704810bb6309ddb2e64565?sid=05b11563-33bb-46de-8a21-ac3e6bbfb79d" %}

If queries aren't enabled, avoid questions about the actual content of the data that isn't referenced in the metadata or documentation. In this case, the data itself is not being sent to OpenAI so we are unable to give accurate results. Instead, try asking it to write a query for the data you're hoping to learn about.

**2. Be Specific**

When you know the exact resource you're inquiring about, use the `@` symbol followed by the resource name to direct the AI accurately.

**Examples:**

* "Can you tell me more about how the @Sales Dashboard was created and which resources it uses?"
* "How would I join the @orders and @payments tables in a query?"
* "What downstream resources would be affected if I deprecated the @customers table?"

{% embed url="https://www.loom.com/share/b7e9c8a8acf44a569b6e15e69416f02e" %}

**3. Provide feedback**

Use the <img src="https://a.slack-edge.com/production-standard-emoji-assets/14.0/apple-medium/1f44d@2x.png" alt=":+1:" data-size="line"> and <img src="https://a.slack-edge.com/production-standard-emoji-assets/14.0/apple-medium/1f44e@2x.png" alt=":-1:" data-size="line"> buttons to provide feedback on the AI Assistant's responses. This helps it learn and improve its accuracy. For instance, if it references the incorrect table, you can correct it, guiding its future responses.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/98a13872-27b5-4f05-9762-2d3e3afa752e.png" alt="" width="375"><figcaption><p>Provide feedback to improve the AI</p></figcaption></figure>

**4. Keep It Fresh**

Start new chats every 10 messages to ensure clarity and reset the context for the AI, enhancing response accuracy.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/8f0a011b-7424-45cb-8704-3f7108d66536.gif" alt=""><figcaption><p>Starting a new conversation</p></figcaption></figure>

**5. Keep Questions Concise and Direct**

Clear and succinct questions yield the best responses. Avoid overly complex or vague prompts that might confuse the AI.

## Unsure where to start?

By following these guidelines, you can significantly enhance your productivity and data understanding using the Secoda AI Assistant.

**Don't just take our word for it! Ask the tool itself** :wink:

<figure><img src="../../.gitbook/assets/Screenshot 2025-05-05 at 3.57.35 PM.png" alt=""><figcaption><p>Secoda AI's response to the best way to use it.</p></figcaption></figure>
