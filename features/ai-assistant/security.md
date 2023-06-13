---
description: This page reviews the security practices in place for the AI Assistant.
---

# Security

Wondering if the Secoda AI Assistant is the right tool for your workspace considering your data governance and privacy policies?&#x20;

Ensuring our customers feel safe and comfortable using this tool is a **top priority for us**. Read on to learn how we are ensuring your data is safe and secure.&#x20;

### What data is sent to OpenAI?

The only data sent to OpenAI is the metadata in your workspace. Metadata is defined as properties and documentation describing your resources, including Owners, Tags, Descriptions, Definitions, Popularity, Resource Names, and more. **The data within the resource does not leave the workspace.**&#x20;

For example, if you are an owner of tables in your workspace, you can ask the AI Assistant how many tables you own, and to list these tables. Ownership is a metadata property in Secoda.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/Screenshot 2023-04-26 at 2.53.16 PM.png" alt=""><figcaption><p>A screenshot of asking the AI Assistant how many tables do I own.</p></figcaption></figure>

Using other metadata properties, such as Descriptions, the AI Assistant can answer what the content of the tables is.&#x20;

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/Screenshot 2023-04-26 at 2.56.13 PM.png" alt=""><figcaption><p>A screenshot of asking the AI Assistant how many tables do I own.</p></figcaption></figure>

However, because the data itself is not being sent to OpenAI, if you ask to directly see the data, the response renders a query for the data instead.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/Screenshot 2023-04-26 at 3.00.42 PM.png" alt=""><figcaption><p>A screenshot of asking the AI Assistant to see the first few lines of a table.</p></figcaption></figure>

### Is data shared between workspaces?&#x20;

Absolutely not. All metadata is specific to your workspace and is not shared or accessible by anyone who isn't granted access to your workspace. **You cannot ask the AI Assistant about metadata that is not in your workspace.**

### Is OpenAI saving this data?

According to OpenAI, any data sent over through the API is not saved or used to train their Large Language Model. You can read more about this [here](https://openai.com/policies/api-data-usage-policies).&#x20;

### Do my interactions with the AI Assistant get saved?

To establish memory within your interactions with the AI Assistant, your prompts are saved. You can see your previous prompts in the right hand side panel in the AI Assistant page.&#x20;

### Is this tool GDPR Compliant?

As mentioned, the AI Assistant is powered by OpenAI. OpenAI is GDPR compliant and takes data privacy very seriously. They have implemented measures to ensure compliance with GDPR and other data privacy laws, such as providing users with the ability to delete their data and implementing data protection impact assessments.

### Does the metadata leave my geographical region?

As mentioned, the metadata is sent to the OpenAI API. The OpenAI API is designed to route requests to the closest available data center in order to minimize network latency and ensure optimal performance.&#x20;

For example, if you make an OpenAI API request from Germany, the API may route your request to a data center located in Europe or a nearby region, such as the Middle East or Africa.

However, the specific location of the data center used may depend on various factors, such as the availability of resources, network conditions, and demand. Additionally, OpenAI may use different cloud providers and data center locations to serve different parts of the world or for different services.

It's worth noting that OpenAI offers a GDPR-compliant Data Processing Addendum (DPA) that outlines the company's obligations and responsibilities as a data processor under GDPR.

You can learn more about OpenAI's Privacy Policies [here](https://openai.com/policies/privacy-policy).
