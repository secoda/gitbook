---
description: What Secoda AI has access to answer questions about
---

# Secoda AI Capabilities

The following document outlines what Secoda AI has access to and can answer questions about and what it currently cannot answer. The team at Secoda is quickly evolving the Secoda AI capabilities which will be reflected in this document.

## In scope

This section provides an overview of the capabilities of Secoda AI in the areas of data discovery, cataloging, analysis, querying, and metadata governance. It details what Secoda AI can access, including searching for and retrieving data assets and documentation, executing queries, generating visualizations, and handling metadata.

#### **Data Discovery & Catalog**

* **Search resources** - Find and discover data assets (tables, views, dashboards, etc.)
* **Search knowledge** - Access documents, definitions, and documentation
* **Retrieve resource details** - Get metadata, schemas, descriptions, and properties of data assets
* **Resource links** - Generate links to resources within Secoda
* **Lineage information** - Retrieve upstream and downstream data lineage
* **Glossary terms** - Access business glossary definitions and terms

#### **Data Analysis & Querying**

* **Run SQL queries** - Execute SQL queries on connected data sources (can be disabled by admins)
* **File operations** - Read file contents, view first/last lines, search within files
* **Chart generation** - Create visualizations and charts from data

#### **Metadata & Governance**

* **Tags and owners** - Access information about data tags and resource owners
* **Integrations** - Information about connected data sources
* **Teams and users** - Access to workspace member information

#### **Knowledge Management**

* **Documentation** - Access to Secoda documentation and help content
* **Memory functions** - Store and retrieve information for context in conversations
* **Note-taking** - Create and read notes during research sessions

#### **External Information**

* **Web search** - Search the internet for additional context (when enabled)
* **Web page reading** - Read content from web pages

## Out of scope

This section outlines the limitations and capabilities across various features within the platform, providing clarity on what functionalities are accessible under different categories such as Knowledge Management, External Information, Administrative & Security Features, and System Administration.

#### Administrative & Security Features

* **Policies** - Data governance policies, compliance rules, and policy configurations
* **Access Requests** - Access request workflows, approvals, and permission requests
* **Monitors & Incidents** - Data quality monitors, incident reports, and monitoring configurations
* **Audit logs** - Workspace activity history and user action records

#### System Administration

* **User management** - User account creation, modification, and deletion
* **Workspace settings** - Workspace configurations, billing information, and administrative settings
* **Integration configurations** - Data source connection setup and configuration changes
* **Permission management** - Role assignments and user permission modifications

#### Automation & Operations

* Automations - Automated workflows, scheduled jobs, and automation configurations
* Analytics dashboards - Workspace usage metrics and administrative analytics

## **Access Controls & Restrictions**

Access controls in user management, automation, and AI are crucial for securing resources and safeguarding data privacy. Users can configure access levels through persona-based filtering and control features in alignment with:

#### **Persona-Based Filtering**

* AI Personas can have **included/excluded filters** that restrict which resources the AI can access
* Admins can configure governance rules to limit AI access to specific data assets

#### **Tool-Level Controls**

* Individual AI tools can be **enabled or disabled** by workspace administrators
* By default, some tools like SQL execution may be disabled for security

#### **Data Privacy**

* **PII masking** - Can be configured to mask personally identifiable information
* **Entity permissions** - Respects user-level permissions for data access
* **Team-based access** - AI access follows the same team-based permissions as users

#### **Feature Access**

* Access depends on **subscription plan** and **feature flags**
* Some features may be in beta or require specific workspace configurations
