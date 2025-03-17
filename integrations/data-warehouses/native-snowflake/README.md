---
description: A step-by-step guide to set up and configure the Secoda Snowflake Native App
---

# Setting Up Secoda Snowflake Native App

This guide walks you through the process of setting up and configuring the Secoda Snowflake Native App. Follow these steps to establish a secure connection between Secoda and your Snowflake environment.

## Prerequisites

Before you begin, ensure you have:
- A Secoda account with administrative access
- A Snowflake account with permissions to install applications
- Access to Snowflake Marketplace

## Setup Steps

### 1. Create Integration in Secoda

1. Log in to your Secoda account
2. Navigate to the Integrations page
3. Click "Add Integration"
4. Search for and select "Snowflake Native App"
5. Click "Create Integration" (No additional configuration is required at this stage)

### 2. Install Secoda App from Snowflake Marketplace

1. Navigate to Snowflake Marketplace
2. Search for "Secoda"
3. Select the Secoda Native App
4. Click "Get" to begin the installation process
5. Open the "INSTALL_SECODA" application in Snowflake

### 3. Generate API Key

1. In your Secoda account, go to Settings
2. Navigate to the API Keys section
3. Click "Generate New API Key"
4. Save the generated API key securely - you'll need it for the next step
5. Copy your Integration ID from the integration you created in step 1

### 4. Configure the Snowflake Native App

1. In the INSTALL_SECODA application interface, provide:
   - Integration ID (from step 1)
   - API Key (generated in step 3)
2. Click "Connect" to establish the connection

### 5. Grant Required Privileges

The app requires specific privileges to function properly. You'll need to grant the following account-level privileges:

- EXECUTE TASK
- EXECUTE MANAGED TASK

For object access, you'll need to grant:
- Secoda Call Function (USAGE)

To grant these privileges:

1. Navigate to the app's privileges page
2. Click "Review" for Account level privileges
3. Click "Add" for Object access privileges
4. Confirm the privilege grants

## Security Note

The Secoda Snowflake Native App runs entirely within your Snowflake environment, ensuring your data never leaves your infrastructure. All communication between Secoda and Snowflake is encrypted and secured through Snowflake's native security protocols.
