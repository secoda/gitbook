---
description: An overview of Secoda's MicroStrategy One integration
---

# MicroStrategy One

## MicroStrategy Integration

Connect MicroStrategy to Secoda to discover your reports, dossiers, and datasets. This integration organizes your MicroStrategy content by project with dedicated folders for different content types, making it easy to search and understand your business intelligence assets.

### Overview

The MicroStrategy integration extracts and catalogs the following content types from your MicroStrategy instance:

* **Projects**: Main organizational units containing all other content
* **Reports**: Analytical reports and documents
* **Dossiers**: Interactive dashboards and visualizations
* **Datasets**: Data cubes and analytical datasets
* **Documents**: Supporting documentation and files

### Features

* **Project-based Organization**: Content is organized by MicroStrategy projects with dedicated folders for each content type
* **Comprehensive Discovery**: Automatically discovers all reports, dossiers, datasets, and documents
* **Metadata Extraction**: Captures titles, descriptions, modification dates, and ownership information
* **Hierarchical Structure**: Creates a logical folder structure within each project
* **Search Integration**: All content becomes searchable within Secoda

### Prerequisites

* MicroStrategy instance with REST API access
* Valid MicroStrategy user credentials
* Network connectivity between Secoda and your MicroStrategy instance

### Setup Instructions

#### 1. Configure Integration

1. Navigate to **Integrations** in your Secoda workspace
2. Search for "MicroStrategy" and click **Connect**
3. Fill in the required connection details:
   * **Base URL**: Your MicroStrategy instance URL (e.g., `https://your-instance.microstrategy.com`)
   * **Username**: Your MicroStrategy username
   * **Password**: Your MicroStrategy password

#### 2. Test Connection

Click **Test Connection** to verify your credentials and ensure Secoda can access your MicroStrategy instance.

#### 3. Configure Sync Settings

* **Teams**: Select which teams should have access to this integration
* **Sync Frequency**: Choose how often to sync data (recommended: daily)

#### 4. Start Sync

Click **Create Integration** to begin the initial sync process.

### Content Organization

The integration creates a hierarchical structure within Secoda:

\
├── Project 1\
&#x20; ├── Reports/\
&#x20;   ├── Report A\
&#x20;   └── Report B\
&#x20; ├── Datasets/\
&#x20;   ├── Dataset A\
&#x20;   └── Dataset B\
&#x20; ├── Documents/\
&#x20;   ├── Document A\
&#x20;   └── Document B\
&#x20; └── Dossiers/\
&#x20; ├── Dossier A\
&#x20; └── Dossier B

└── Project 2\
&#x20; ├── Reports/\
&#x20; ├── Datasets/\
&#x20; ├── Documents/\
&#x20; └── Dossiers/
