---
description: This page reviews the security practices in place for Secoda AI.
---

# Secoda AI Security FAQs

Wondering if the Secoda AI is the right tool for your workspace considering your data governance and privacy policies?

Ensuring our customers feel safe and comfortable using this tool is a **top priority for us**. Read on to learn how we are ensuring your data is safe and secure.

{% hint style="info" %}
The term "LLM provider" could refer to OpenAI, Google, or Anthropic, depending on the region.
{% endhint %}

### What data is sent to the LLM provider?

The only data sent to the LLM provider by default is the metadata in your workspace. Metadata is defined as properties and documentation describing your resources, including Owners, Tags, Descriptions, Definitions, Popularity, Resource Names, and more. If the Secoda AI run SQL tool is turned on then a sample of the data is sent to the LLM provider to ensure correctness and resolve queries with errors.

### Is data shared between workspaces?

No, all metadata is specific to your workspace and is not shared or accessible by anyone who isn't granted access to your workspace. You cannot ask Secoda AI about metadata that is not in your workspace.

### Is the LLM provider saving this data?

OpenAI, Google, and Anthropic state that any data sent through their APIs is not used to train their language models. You can learn more by reviewing their respective data usage policies: [OpenAI](https://openai.com/enterprise-privacy/), [Google](https://ai.google.dev/gemini-api/terms?_gl=1*q0ne42*_up*MQ..*_ga*MTkwODA2NDgzMy4xNzUyNzg0MTM0*_ga_P1DBVKWT6V*czE3NTI3ODQxMzQkbzEkZzAkdDE3NTI3ODQxMzQkajYwJGwwJGgxMzcyNDI0MzY0), and [Anthropic](https://www.anthropic.com/legal/commercial-terms).

### Do my interactions with Secoda AI get saved by Secoda?

To improve your user experience with Secoda AI, your prompts are saved. You can see your previous prompts in the right hand side panel in the Secoda AI page.

### Is this tool GDPR Compliant?

OpenAI and Anthropic are GDPR compliant and take data privacy very seriously. They have implemented measures to ensure compliance with GDPR and other data privacy laws, such as providing users with the ability to delete their data and implementing data protection impact assessments.

### Does the metadata leave my geographical region?

OpenAI and Anthropic have their servers hosted strictly in the US, so all metadata that is sent to the LLM provider is sent to the US.

OpenAI and Anthropic offer a GDPR-compliant Data Processing Addendum (DPA) that outlines the company's obligations and responsibilities as a data processor under GDPR.

### Who can run queries on data?

Queries can be executed if the following conditions are satisfied:

* **Run SQL Toggle:** The `Run SQL` feature is enabled in the AI settings by an admin.
* **User Permissions:** The user making the query request must have the appropriate query access for the specific integration, as configured by admins in the Integration Permissions settings.

### **How does the AI manage data access?**

Our AI strictly adheres to Team-based data access permissions. If a user inquires about resources from a Team they are not a member of, the AI will not provide any results. This policy ensures that access to data is secure and relevant to the user’s team assignments.
