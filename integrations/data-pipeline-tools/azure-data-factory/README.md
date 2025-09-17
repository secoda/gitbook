---
description: An overview of the Azure Data Factory Integration with Secoda
---

# Azure Data Factory

## **Getting Started with Azure Data Factory** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

There are two options for setting up the Azure Data Factory integration on Secoda, OAuth (into Secoda's managed Azure AD App) or by creating and managing your own Azure AD App.

## Option 1: OAuth

**You must have access to Azure Data Factory to connect through OAuth.**

The Azure Data Factory integration uses OAuth 2.0 to connect Secoda to your Azure workspace. To connect Data Factory to Secoda follow the steps below:

1. In the Integrations section, click on New Integration, and select Azure Data Factory.
2. Navigate to the OAuth tab, and click Connect with OAuth. You will be prompted to log in to your Azure Workspace.
3. Upon successful completion of OAuth authentication with Azure Data Factory, click the Run Initial Sync button to begin a sync.

## Option 2: Azure AD App

### Step 1 -> Create an Azure AD App

1. Open the [Azure portal](https://portal.azure.com/)
2. Search for App registrations and start a new Registration
3. In the New Registration form, fill in the following details:
   * Name: Secoda
   * Supported account types: Accounts in this organizational directory only (Default Directory only - Single tenant)
   * Redirect URI: Leave blank
4. Click Register to submit the form. You'll now be able to access an Application ID and Tenant ID from the Overview tab. Save these values.

### Step 2 -> Create a Client Secret

1. In the certificates and Secrets tab, click the New Client Secret button.
2. The description and expiry of the client secret is up to you. Click Add, and save the Client Secret value.

### Step 3 -> Enable API Access

In the Manage -> API Permissions section of your App Registration, add the permissions `Azure Service Management.user_impersonation` and `Microsoft Graph.user_read`&#x20;

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/d38657d4-47d5-468d-88a8-de1e5188bcac.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/8415dc40-e70f-46d5-8273-e968f74ff8d0.png" alt=""><figcaption></figcaption></figure>

### Step 5 ->Add the Azure Data Factory Integration To Secoda

1. In the Integrations section, click on New Integration, and select Azure Data Factory.
2. Navigate to the Managed tab, and fill in the form with the required information from the previous steps.
   * **Client ID:** Application ID of Azure AD.
   * **Tenant ID:** Identifier of tenant of organization in Azure Active AD.
   * **Client Secret:** Client secret of the Azure AD App.
   * **Username:** Username of a user with access to the desired resources in Data Factory.
   * **Password:** Password corresponding to the provided username.

{% hint style="info" %}
Using service account credentials for the username and password is strongly recommended, because the username will be visible to all viewers of the integration.
{% endhint %}
