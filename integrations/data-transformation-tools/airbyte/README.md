---
description: An overview of the Airbyte integration with Secoda
---

# Airbyte

{% content-ref url="airbyte-metadata-extracted.md" %}
[airbyte-metadata-extracted.md](airbyte-metadata-extracted.md)
{% endcontent-ref %}

## Getting Started with Airbyte <a href="#h_21e27f5a15" id="h_21e27f5a15"></a>

&#x20;There are two steps to get started using Airbyte with Secoda:

1. Generate an API key in Airbyte&#x20;
2. Connect Airbyte to Secoda

## Generate an API Key

For generating an API key, see: [https://reference.airbyte.com/reference/authentication#:\~:text=Airbyte%20Cloud%20Users,you%20store%20it%20somewhere%20safe](https://reference.airbyte.com/reference/authentication)

## **Connect Airbyte to Secoda** <a href="#h_276d2819e7" id="h_276d2819e7"></a>

The next step is to connect Secoda:

1. In the Secoda App, select ‘Add Integration’ on the Integrations tab
2. Search for and select ‘Airbyte’
3. Under Host, input '[https://api.airbyte.com](https://api.airbyte.com)'. If you're self-hosting, change this to your instance i.e. [https://airbyte.secoda.com](https://airbyte.secoda.com).
4. Under User, input your email address
5. Under Token, add the generated API key. This information is kept encrypted.
6. Optionally add Teams for the integration to be added to
7. Click 'Submit'
