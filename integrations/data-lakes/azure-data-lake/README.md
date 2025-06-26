---
description: An overview of the Azure Data Lake integration with Secoda
---

# Azure Data Lake

{% content-ref url="adl-metadata-extracted.md" %}
[adl-metadata-extracted.md](adl-metadata-extracted.md)
{% endcontent-ref %}

## Getting started with Azure Data Lake

There are two steps to connect Azure Data Lake Storage Gen2 with Secoda:

1. Set up Microsoft Entra ID authentication
2. Connect Azure Data Lake to Secoda

## 1. Set up Authentication

#### **Option 1: OAuth Authentication (Recommended)**

1. Register a new application in Azure
   1. Navigate to the Azure Portal and go to "Azure Active Directory" > "App registrations", then click "New registration"
   2. Enter a name for your application (e.g., "Secoda Data Lake Integration")
   3. Select "Accounts in this organizational directory only" for supported account types
   4. Click "Register"
2. Configure IAM Permissions
   1. In your storage container, click on "Access control (IAM)"
   2. Click on "Add" > "Add role assignment"
   3. Select "Storage Blob Data Reader" from the "Role" dropdown
   4. On the “Assign access to” dropdown, choose the application that was created in step 1 (e.g., "Secoda Data Lake Integration")
   5. Click "Save" to apply changes
3. Create a Client Secret
   1. Go to "Certificates & secrets" in your app registration
   2. Click "New client secret"
   3. Add a description and select an expiration period
   4. Copy the generated secret value (you won't be able to see it again)
4. Note Your Application Details
   1. Copy the "Application (client) ID" from the Overview page
   2. Copy the "Directory (tenant) ID" from the Overview page
   3. Keep the client secret you just created

#### **Option 2: Service Principal Authentication**

This method uses a service principal for programmatic access.

1. Create a Service Principal:

```
az ad sp create-for-rbac --name <<YOUR_NAME_HERE>> --role "Storage Blob Data Reader"
```

2. Configure IAM Permissions
   1. In your storage container, click on "Access control (IAM)"
   2. Click on "Add" > "Add role assignment"
   3. Select "Storage Blob Data Reader" from the "Role" dropdown
   4. On the “Assign access to” dropdown, choose the service principal that was just created
   5. Click "Save" to apply changes
3. Note Your Service Principal Details
   1. Application (client) ID
   2. Client secret
   3. Tenant ID
   4. Subscription ID

## 2. Connect Azure Data Lake to Secoda

After setting up Microsoft Entra ID authentication, the next step is to connect Azure Data Lake to Secoda:

1. In the Secoda App, navigate to the "Integrations" tab
2. Click on "Connect Integration"
3. Search for and select "Azure Data Lake"
4. Choose your authentication method:
   1. OAuth: Click "Connect with OAuth" and follow the Microsoft Entra ID authorization flow
   2. Managed: Enter the following credentials:
      1. Tenant ID
      2. Subscription ID
      3. Storage account name
      4. Client ID (app or service principal created for this integration)
      5. Client Secret
      6. (Optional) Username and Password for user-based authentication
5. Test the Connection - if successful, you'll be prompted to run your initial sync.

\
