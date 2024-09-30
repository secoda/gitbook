---
description: This page reviews the security practices in place for Secoda AI.
---

# Secoda AI Security FAQs

Wondering if the Secoda AI is the right tool for your workspace considering your data governance and privacy policies?

Ensuring our customers feel safe and comfortable using this tool is a **top priority for us**. Read on to learn how we are ensuring your data is safe and secure.

### What data is sent to OpenAI?

The only data sent to OpenAI is the metadata in your workspace. Metadata is defined as properties and documentation describing your resources, including Owners, Tags, Descriptions, Definitions, Popularity, Resource Names, and more. **The data within the resource does not leave the workspace.**

### Is data shared between workspaces?

No. All metadata is specific to your workspace and is not shared or accessible by anyone who isn't granted access to your workspace. **You cannot ask Secoda AI about metadata that is not in your workspace.**

### Is OpenAI saving this data?

According to OpenAI, any data sent over through the API is **not used to train their Large Language Model**. However, as mentioned in the OpenAI policy, OpenAI may securely retain API inputs and outputs for up to 30 days for quality assurance. After 30 days, API inputs and outputs are removed. You can read more about this [here](https://openai.com/policies/api-data-usage-policies).

### Do my interactions with Secoda AI get saved by Secoda?

To establish memory within your interactions with Secoda AI, your prompts are saved. You can see your previous prompts in the right hand side panel in the Secoda AI page.

### Is this tool GDPR Compliant?

As mentioned, Secoda AI is powered by OpenAI. OpenAI is GDPR compliant and takes data privacy very seriously. They have implemented measures to ensure compliance with GDPR and other data privacy laws, such as providing users with the ability to delete their data and implementing data protection impact assessments.

### Does the metadata leave my geographical region?

As mentioned, the metadata is sent to the OpenAI API. The OpenAI API is designed to route requests to the closest available data center in order to minimize network latency and ensure optimal performance.

For example, if you make an OpenAI API request from Germany, the API may route your request to a data center located in Europe or a nearby region, such as the Middle East or Africa.

However, the specific location of the data center used may depend on various factors, such as the availability of resources, network conditions, and demand. Additionally, OpenAI may use different cloud providers and data center locations to serve different parts of the world or for different services.

It's worth noting that OpenAI offers a GDPR-compliant Data Processing Addendum (DPA) that outlines the company's obligations and responsibilities as a data processor under GDPR.

You can learn more about OpenAI's Privacy Policies [here](https://openai.com/policies/privacy-policy).

### Who can run queries on data?

Queries can be executed if the following conditions are satisfied:

* **Run SQL Toggle:** The `Run SQL` feature is enabled in the AI settings by an admin.
* **User Permissions:** The user making the query request must have the appropriate query access for the specific integration, as configured by admins in the Integration Permissions settings.

### **How does the AI manage data access?**

Our AI strictly adheres to Team-based data access permissions. If a user inquires about resources from a Team they are not a member of, the AI will not provide any results. This policy ensures that access to data is secure and relevant to the user’s team assignments.
