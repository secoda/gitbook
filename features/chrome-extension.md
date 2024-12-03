---
description: >-
  Access Secoda metadata and features without leaving your other data tools by
  adding the Chrome extension.
---

# Chrome Extension

## Overview

The goal of the Chrome extension feature is to make the capabilities of Secoda more accessible directly in people's existing workflows.

It's main capabilities include:

* Searching, accessing, and editing Secoda metadata directly in tools like Looker, Tableau, Snowflake, BigQuery, and others. See [#supported-tools](chrome-extension.md#supported-tools "mention")for the full list.
* Accessing and searching resource lineage from within these tools.
* Starting conversations with Secoda AI and asking the data team questions from within these tools.
* Highlighting text and searching Secoda from anywhere on the web.

Once installed and configured, the Chrome extension will appear as a Secoda icon in the bottom right hand of your screen for easy access within a supported tool.

<figure><img src="../.gitbook/assets/Kapture 2024-12-03 at 16.27.51.gif" alt=""><figcaption></figcaption></figure>

## How to Install and Authenticate

1. The first step is to ensure that you have a Secoda account, and that your workspace has connected at least one of the [#supported-tools](chrome-extension.md#supported-tools "mention") below.
2. Download the Secoda Chrome Extension in the web store using[ <mark style="color:blue;">**this link**</mark>](https://chrome.google.com/webstore/detail/secoda/akcolkhleaionhppniljgglpeeohkljk)<mark style="color:blue;">.</mark>
3. Click **Add to Chrome.**
4. Open the Secoda Chrome Extension and click **Authenticate.**
5. Go through the authentication flow in Secoda. Verify that the connection is made in the Chrome Extension settings at [https://app.secoda.co/settings/chrome-extension](https://app.secoda.co/settings/chrome-extension)

## Capabilities

Once you click into the Secoda icon, you will be able to see the Overview metadata of the resource, the downstream and upstream lineage, as well as a space to start a chat with the AI Assistant. This will allow you to reduce the need to jump from tool to tool, reducing the amount of time spent on workflows.

### View and Edit Resource Metadata

Access resource metadata in the supported tools to gain context about ownership, descriptions and any other enrichment that you've built out in Secoda.

You also have the ability to edit resources from the extension and push these changes into Secoda.

<figure><img src="../.gitbook/assets/image (86).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Your permissions in Secoda will control what metadata you can see and edit when using the extension in other supported tools. For example, viewers in Secoda will not be able to push any edits.
{% endhint %}

### Access and Search Lineage

See the upstream and downstream lineage of the resource without having to leave the other tool that you are currently working in. Click into Lineage to see the relationships at different depths, use the provided search bar to search, and access the lineage graph within the Secoda UI.

<figure><img src="../.gitbook/assets/image (87).png" alt=""><figcaption></figcaption></figure>

### Search Resources

If you have a question about any resource in your Secoda workspace you can use the universal search to find, access, and understand from any data tool.

<figure><img src="../.gitbook/assets/image (89).png" alt=""><figcaption></figcaption></figure>

### Ask Questions to Secoda AI and the Data Team

Do you have a question about a resource for the AI Assistant or the Data Team? Click on the links in the main page of the Chrome Extension to be redirected to Secoda for asking these questions.

<figure><img src="../.gitbook/assets/image (88).png" alt=""><figcaption></figcaption></figure>

### Highlight Text to Search

To search for Secoda context for any information from **any** website:

1. Highlight the text that you'd like to search for on the page that you're viewing
2. Right-click, and then select "Search Secoda for '...'"

The Chrome extension will open up a new browser tab with the results for that text.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/bde0dd82-92aa-4896-9776-1017e7f00446.png" alt=""><figcaption></figcaption></figure>

## Supported tools

The Chrome extension supports resources in the following tools:

* [Tableau](../integrations/data-visualization-tools/tableau-integration/): Dashboards, Workbooks, Datasources
* [Looker](../integrations/data-visualization-tools/looker-integration/): Dashboards, Explores
* [Metabase](../integrations/data-visualization-tools/metabase/): Dashboards, Questions
* [Redash](../integrations/data-visualization-tools/redash/): Visualizations, Dashboards
* [PowerBI](../integrations/data-visualization-tools/power-bi/): Dashboards, Reports
* [Snowflake](../integrations/data-warehouses/snowflake-integration/) (via Snowsight): Schemas, Tables, Views
* [BigQuery](../integrations/data-warehouses/bigquery-integration/): Schemas, Tables, Views
* [Sigma](../integrations/data-visualization-tools/sigma-integration/): Workbooks, Elements, Pages
* [Mode](../integrations/data-visualization-tools/mode/): Reports, Charts
* [dbt Cloud](../integrations/data-transformation-tools/dbt/#chrome-extension-with-dbt-cloud): Jobs, Models
* [Lightdash](../integrations/data-visualization-tools/lightdash/): Dashboards
* [Hex](../integrations/data-visualization-tools/hex/): Projects

## Video resource

{% embed url="https://www.loom.com/share/6e22054c0b864badbd97d3581f765dcc?sid=a247fb0b-e4a6-4b86-a0f0-dfeecf6ad711" %}
