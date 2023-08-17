---
description: >-
  Access Secoda metadata and features without leaving your other data tools by
  adding the Chrome extension.
---

# Chrome Extension

## Overview

The goal of the Chrome extension feature is to make the capabilities of Secoda more accessible directly in people's existing workflows.

It's main capabilities include:

* Accessing and editing Secoda metadata directly in tools like Looker, Tableau, Snowflake, BigQuery, etc.
* Accessing and searching resource lineage from within these tools
* Starting conversations with Secoda AI from within these tools
* Highlighting text and searching Secoda from anywhere

Once installed and configured, the Chrome extension will appear as a Secoda icon in the bottom right hand of your screen for easy access within a supported tool.

<figure><img src="../.gitbook/assets/Screenshot 2023-08-07 at 2.05.22 PM.png" alt=""><figcaption><p>Chrome extension in Snowflake UI</p></figcaption></figure>

## How to Install and Authenticate

1. The first step is to ensure that you have a Secoda account, and that your workspace has connected at least one of the [#supported-tools](chrome-extension.md#supported-tools "mention") below.
2. Download the extension in the web store using[ **this li**<mark style="color:blue;">**nk**</mark>](https://chrome.google.com/webstore/detail/secoda/akcolkhleaionhppniljgglpeeohkljk)<mark style="color:blue;">.</mark>
3. Click **Add to Chrome.**
4. Go to any of the supported tools sites, and click the Secoda icon on the bottom right of the screen.
5. Enter your email associated with your Secoda account.
6. If you're already logged into the Secoda app, it will bring you to Secoda and prompt you to **Authenticate Chrome Extension**. Click Authenticate.
7. If you're not logged into the Secoda app, you will have to use your Secoda email to log into the app and then Authenticate the extension.

<figure><img src="../.gitbook/assets/Screenshot 2023-08-16 at 3.50.58 PM.png" alt=""><figcaption></figcaption></figure>

## Capabilities

Once you click into the Secoda icon, you will be able to see the Overview metadata of the resource, the downstream and upstream lineage, as well as a space to start a chat with the AI Assistant. This will allow you to reduce the need to jump from tool to tool, reducing the amount of time spent on workflows.

### View and Edit Resource Metadata

Access resource metadata in the supported tools to gain context about ownership, descriptions and any other enrichment that you've built out in Secoda.

You also have the ability to edit resources from the extension and push these changes into Secoda.

<div align="left">

<figure><img src="../.gitbook/assets/Screenshot 2023-08-16 at 3.53.00 PM.png" alt=""><figcaption></figcaption></figure>

</div>

{% hint style="info" %}
Your permissions in Secoda will control what metadata you can see and edit when using the extension in other supported tools. For example, viewers in Secoda will not be able to push any edits.
{% endhint %}

### Access and Search Lineage

See the upstream and downstream lineage of the resource without having to leave the other tool that you are currently working in. Click into Lineage to see the relationships at different depths, use the provided search bar to search, and access the lineage graph within the Secoda UI.

<div align="left">

<figure><img src="../.gitbook/assets/Screenshot 2023-08-16 at 3.53.24 PM.png" alt=""><figcaption></figcaption></figure>

</div>

### Chat with Secoda AI

Do you have a question about a resource for the AI Assistant? Ask AI directly in the pop-up and this will automatically open a conversation in Secoda with that prompt.

<div align="left">

<figure><img src="../.gitbook/assets/Screenshot 2023-08-16 at 3.56.23 PM.png" alt=""><figcaption></figcaption></figure>

</div>

### Highlight Text to Search

To search for Secoda context for any information from **any** website:

1. Highlight the text that you'd like to search for on the page that you're viewing
2. Right-click, and then select "Search Secoda for '...'"

The Chrome extension will open up a new browser tab with the results for that text.

<figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

## Supported tools

The Chrome extension supports resources in the following tools:

* [Tableau](../integrations/data-visualization-tools/tableau-integration/): Dashboards, Workbooks, Datasources
* [Looker](../integrations/data-visualization-tools/looker-integration/): Dashboards, Explores
* [Metabase](../integrations/data-visualization-tools/metabase/): Dashboards, Questions
* [Redash](../integrations/data-visualization-tools/redash/): Visualizations, Dashboards
* [PowerBI](../integrations/data-visualization-tools/power-bi/): Dashboards, Reports
* [Snowflake](../integrations/data-warehouses/snowflake-integration/) (via Snowsight): Schemas, Tables, Views
* [BigQuery](../integrations/data-warehouses/bigquery-integration/): Schemas, Tables, Views
