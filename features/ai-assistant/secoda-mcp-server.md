# Secoda MCP Server

Learn how to use the Model Context Protocol (MCP) to enable AI agents to securely access and interact with your Secoda data catalog, run SQL queries, and explore data lineage.

### What is Model Context Protocol?

MCP is a protocol that enables AI tools and applications to connect with Secoda's data catalog and services in a secure, standardized way. It provides a structured method for AI models to:

* Search and retrieve data assets (tables, columns, dashboards, documentation)
* Execute SQL queries against your connected data warehouses
* Access data lineage and relationships between entities
* Retrieve business glossary terms and definitions
* Access Secoda documentation and knowledge articles

### How MCP Works

Secoda hosts the MCP server as part of your workspace that provides access to your data catalog through a secure, authenticated interface.

When an AI tool or application needs to access Secoda data:

1. The tool connects to Secoda's MCP server endpoints
2. Authentication verifies the user's workspace and AI permissions
3. The tool can then access relevant Secoda data and functionality
4. All operations respect your existing data governance and access controls

### Benefits of Using MCP

* **Secure Access**: All data access is authenticated and respects workspace permissions
* **Live Data Queries**: Execute SQL queries directly against your data warehouses
* **Comprehensive Catalog Access**: Search across all your data assets and documentation
* **Data Lineage**: Understand upstream and downstream dependencies
* **Standardized Interface**: Consistent interaction pattern across different AI tools

### Available Tools

The Secoda MCP server provides the following tools:

| Tool                 | Description                                                        |
| -------------------- | ------------------------------------------------------------------ |
| `search_data_assets` | Search for tables, columns, charts, and dashboards                 |
| `search`             | General search across all Secoda resources including documentation |
| `run_sql`            | Execute SQL queries against your connected data warehouses         |
| `retrieve_entity`    | Get detailed information about a specific data entity              |
| `entity_lineage`     | Explore upstream and downstream data dependencies                  |
| `glossary`           | Access business terms and definitions from your glossary           |
| `get_secoda_docs`    | Retrieve Secoda documentation and knowledge articles               |
| `chart`              | Work with charts and visualizations                                |

### Setting things up

> **Connection issues**: MCP is still evolving. If you experience connection issues, try restarting your AI client or contact your Secoda administrator to verify MCP is enabled for your workspace.

Here's how you can configure popular AI tools to work with Secoda's MCP server:

#### Claude.ai

**Team, Enterprise**

1. Go to your settings at https://claude.ai/settings/profile
2. Under the **Integrations** section click on **Add more**
3. Use your Secoda MCP server URL: `https://[your-workspace].secoda.co/ai/mcp`
4. Authenticate with your Secoda credentials when prompted

**Free, Pro**

1. Open the file `~/Library/Application Support/Claude/claude_desktop_config.json`
2. Add the following and restart the Claude desktop app:

```json
{
  "mcpServers": {
    "secoda": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://[your-workspace].secoda.co/ai/mcp"]
    }
  }
}
```

#### Cursor

1. Open Cursor Settings (`CMD/CTRL + Shift + J`)
2. Go to the **MCP** section
3. Click on **Add new global MCP server**
4. Add the following configuration:

```json
{
  "mcpServers": {
    "secoda": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://[your-workspace].secoda.co/ai/mcp"]
    }
  }
}
```

#### Windsurf

1. Open Windsurf settings (`CMD/CTRL + ,`)
2. Go to the **Cascade** section
3. Press the **Add Server** button then **Add custom server**
4. Add the following configuration:

```json
{
  "mcpServers": {
    "secoda": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://[your-workspace].secoda.co/ai/mcp"]
    }
  }
}
```

#### VS Code

1. Hit `CMD/CTRL + Shift + P` and search for **> MCP: Add Server...**
2. Select **Command (stdio)**
3. Enter `npx mcp-remote https://[your-workspace].secoda.co/ai/mcp` as the command
4. Enter `Secoda` as the Server ID
5. Hit `CMD/CTRL + Shift + P` and search for **> MCP: List Servers**
6. Start Secoda's MCP server

#### Others

Many other tools now support MCP servers. You can configure them to use Secoda's MCP server with the following settings:

* **Command**: `npx`
* **Arguments**: `-y mcp-remote https://[your-workspace].secoda.co/ai/mcp`
* **Environment**: None

### Example Usage

Once connected, you can interact with your Secoda data through natural language:

**Data Discovery**

* "Find all tables related to customer data"
* "Show me the schema for the sales\_summary table"
* "What dashboards use revenue metrics?"

**SQL Queries**

* "Show me total sales for the last quarter"
* "What's the average order value by region?"
* "Count active users in the past 30 days"

**Data Lineage**

* "What feeds into the customer\_metrics table?"
* "What would be affected if I change the orders table?"
* "Show me the lineage for the revenue calculation"

**Business Context**

* "What does 'Monthly Recurring Revenue' mean in our glossary?"
* "Find documentation about our data quality processes"
* "What's the definition of an active user?"

### Prerequisites

* A Secoda workspace with AI features enabled
* An MCP-compatible AI assistant, e.g., Claude

### FAQ

**Why am I getting authentication errors?**\
Ensure you have the correct permissions in your Secoda workspace and that MCP is enabled by your administrator.

**I'm seeing connection timeouts**\
MCP connections can be sensitive to network conditions. Try restarting your AI client or check with your network administrator about proxy settings.

