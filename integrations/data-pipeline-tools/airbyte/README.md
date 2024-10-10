# Airbyte

{% content-ref url="airbyte-extracted-metadata.md" %}
[airbyte-extracted-metadata.md](airbyte-extracted-metadata.md)
{% endcontent-ref %}

### Self-Managed Airbyte Instance <a href="#h_21e27f5a15" id="h_21e27f5a15"></a>

If your Airbyte instance is self-managed, you will need to follow the [steps here](https://docs.airbyte.com/enterprise-setup/api-access-config) before continuing. The minimum Airbyte version required by Secoda is v0.63.13.

## Getting Started with Airbyte <a href="#h_21e27f5a15" id="h_21e27f5a15"></a>

&#x20;There are two steps to get started using Airbyte with Secoda:

1. Generate a set of Application credentials in Airbyte
2. Connect Airbyte to Secoda

## Generating Application Credentials in Airbyte

To generate a set of Application credentials follow the [steps here](https://reference.airbyte.com/reference/authentication). When you finish you should have a `Client ID` and a `Client Secret`. You'll need these for the next step.

## **Connect Airbyte to Secoda** <a href="#h_276d2819e7" id="h_276d2819e7"></a>

The next step is to connect Secoda:

1. In the Secoda App, select ‘Add Integration’ on the Integrations tab
2. Search for and select ‘Airbyte’
3. Under Server URL, input [https://api.airbyte.com](https://api.airbyte.com)
   1. If you're self-managed, change this to your _airbyte-server_ instance (i.e. [https://airbyte.secoda.com/api/](https://airbyte.secoda.com/api/))
4. Under Dashboard URL, input [https://cloud.airbyte.com](https://cloud.airbyte.com)
   1. If you're self-managed change this to your _airbyte-webapp_ instance (i.e. [https://airbyte.secoda.com](https://airbyte.secoda.com))
5. Optionally add Teams for the integration to be added to
6. Click "Test connection"
   1. If the connection fails, ensure that you have the correct Server URL and credentials, and try again. If it still fails, contact support.
7. Select the workspaces you want to sync
8. You are connected :tada::tada:
