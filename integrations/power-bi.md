---
description: >-
  This page walks through the Secoda and Power BI integration that Secoda
  supports
---

# Power BI Integration

## **Getting Started with Power BI** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

There are two options for setting up the Power BI integration on Secoda:

1. OAuth with Secoda's managed Power BI Azure Enterprise Application (**Secoda Managed**)
2. Create and manage a Power BI Azure Enterprise Application (**Self Managed**)

{% hint style="info" %}
For either option, the user that connects Power BI to Secoda must be both:

* An administrator for Azure Active Directory
* An administrator for Power BI
{% endhint %}

### Secoda Managed

The PowerBI integration uses OAuth 2.0 to connect Secoda to your Power BI workspace. To connect Power BI to Secoda follow the steps below:

1. Go to [https://app.secoda.co/integrations/new](https://app.secoda.co/integrations/new) and select the Power BI option
2. Click "Connect". You'll be brought to the consent page that asks for the following permissions on your Power BI workspace

![](<https://secoda-public-media-assets.s3.amazonaws.com/image%20(2)%20(1)%20(3).png>)

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/image.png" alt=""><figcaption></figcaption></figure>

3. Ensure that the following permissions have been set in your Secoda (Power BI) Enterprise Application in Azure

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/image%20(1).png" alt=""><figcaption></figcaption></figure>

4. After you've connected Power BI to Secoda go to [https://app.secoda.co/integrations](https://app.secoda.co/integrations)
5.  Select your Power BI integration and go to **History > Run extraction > Metadata extraction** which will start an extraction for your Power BI integration.&#x20;

    <figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/image%20(4)%20(1).png" alt=""><figcaption></figcaption></figure>

### Self Managed

Here are the steps to set up a self managed Power BI Azure AD App

1. Create an Azure AD App
   * Open the [Azure portal](https://portal.azure.com/)
   * Search for `App registrations`
   * Click `+ New registration`
   * Fill in the following details
     * **Name** - Secoda
     * **Supported account types** - Accounts in this organizational directory only (Default Directory only - Single tenant)&#x20;
     * **Redirect URI (optional)** - Leave blank
   * Click Register
   * After submitting the form, the `Application ID` is available from the Overview tab. Copy and save the `Application ID` for later use.
   * Click the **Certificates & secrets** tab
   * Click the **New client secret** button
   * In the Add a client secret window, enter any description, specify when you want the client secret to expire, and click **Add**.
   * Copy and save the Client secret value
2. Create an Azure AD security group
   * Open the [Azure portal](https://portal.azure.com/)
   * Search for `Azure Active Directory` and select **Azure Active Directory** link
   * The `Tenant ID` is available from the Overview tab. Copy and save the `Tenant ID` for later use
   * Click the **Groups** tab
   * Click the **New group** button
   * Fill form in the required information:
     * **Group type** - Select "Security"
     * **Group name** - Type "PowerBI API Access"
     * **Group description** - Enter any description or leave empty
   * Select "No members selected" to open a drawer. Search for `Secoda` and select **Secoda** entry. Click the **Select** button to confirm.
   * Click **Create**
3. Enable the Power BI service admin settings
   * Open [Power BI admin portal](https://app.powerbi.com/admin-portal/) and sign in
   * Log into the Power BI admin portal. You need to be a Power BI admin to see the tenant settings page
   * Ensure that **Tenant settings** tab are open
   * Search for the subsection "Allow service principals to use Power BI APIs" in "Developer settings" section and open it. Select "Enabled" and add the security group you created "PowerBI API Access" in Azure AD. Click **Apply**
   * Repeat process for all subsection in "Admin API settings" section. Open the section, Select "Enabled" and add the security group you created "PowerBI API Access" in Azure AD. Click **Apply**. You must complete the step for following sections:
     * Allow service principals to use read-only admin APIs
     * Enhance admin APIs responses with detailed metadata
     * Enhance admin APIs responses with DAX and mashup expressions
4. Add Azure AD app to your workspace
   * Open [Power BI](https://app.powerbi.com/) and sign in
   * Search to the workspace you want to enable access for, and from the _More menu_, select _Workspace access_
   * Fill form in the required information:
     * Search for `Secoda` as member and select **Secoda** entry
     * Permission - select "Contributor"
     * Click **Add** button to add
     * Click **Close** button to confirm
5. Connect PowerBI API to Secoda
   * Go to the Secoda **Settings**. Click **Integrations** in the sidebar, then **New integration** and select **Power BI**
   * Fill form in the required information:
     * **Client ID:** Application ID of Azure AD. You'll see this after completing [step 1.6](power-bi.md#1-create-an-azure-ad-app) of the instructions.
     * **Client Secret:** Client secret of Application in Azure AD. You'll see this after completing [step 1.8](power-bi.md#1-create-an-azure-ad-app) of the instructions.
     * **Tenant ID:** Identifier of tenant of organization in Azure Active AD. You'll see this after completing [step 2.3](power-bi.md#2-create-an-azure-ad-security-group) of the instructions.
   * Click **Connect**

### Power BI Lineage (Optional)

To extract Power BI datasets, the "Enhance admin APIs responses with detailed metadata" option in the admin panel must be toggled on.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/image%20(2)%20(4).png" alt=""><figcaption></figcaption></figure>
