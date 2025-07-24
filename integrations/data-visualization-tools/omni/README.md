---
description: An overview of the Omni integration with Secoda
---

# Omni

Connect Omni Analytics to Secoda to catalog your folders, models, queries, dashboards, and documents. The Omni integration will pull all your analytics assets into Secoda, making them searchable and adding context.

<figure><img src="../../../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

### How does the integration work?

The Omni integration connects to the Omni API to extract metadata about your analytics assets. Once connected, Secoda will automatically catalog:

* **Folders**: Organizational structure for your analytics content
* **Dashboards and Documents**: Data visualizations and reports
* **Queries**: SQL queries that power your analytics
* **Models**: Defined data models in your Omni workspace
* **Lineage**: Connections between your data sources and Omni dashboards

Secoda can also extract ownership information for your Omni assets, helping you maintain accountability and governance across your data stack.

### Prerequisites

Before setting up the integration, you'll need:

1. An Omni account with admin privileges
2. An API key from Omni
3. Your Omni host URL, e.g., https://company.omniapp.co

### Setting up the integration

1. Navigate to the **Integrations** tab in Secoda
2. Select **Add Integration**
3. Choose **Omni** from the Data Visualization category
4. Enter the following credentials:
   * **Host**: Your Omni console URL (e.g., https://myorg.omniapp.co)
   * **API Key**: API key created in Omni Settings > API Keys
5. Click **Test Connection** to verify your credentials
6. Click **Create Integration** to finalize

### Troubleshooting

If you encounter issues with the Omni integration:

1. **Connection failures**: Verify your API key and host URL are correct
2. **Missing content**: Ensure your API key has sufficient permissions to access all folders
3. **Lineage issues**: Check if your SQL queries reference tables that exist in your data stack

### Additional Notes

* The integration runs on a schedule to keep metadata in sync
* Dashboard previews use Omni's embed functionality to show live content
* Omni's folder structure is preserved in Secoda to maintain organization

For more help with the Omni integration, contact Secoda support at support@secoda.co
