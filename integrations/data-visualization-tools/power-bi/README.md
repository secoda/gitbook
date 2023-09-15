---
description: >-
  This page walks through the Secoda and Power BI integration that Secoda
  supports
---

# Power BI

{% content-ref url="metadata-extracted.md" %}
[metadata-extracted.md](metadata-extracted.md)
{% endcontent-ref %}

## **Getting Started with Power BI** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

There are two options for setting up the Power BI integration on Secoda:

1. OAuth with Secoda's managed Power BI Azure Enterprise Application (**OAuth**)
2. Create and manage a Power BI Azure Enterprise Application (**Azure AD App**). This can either use:
   * Admin APIs&#x20;
   * Non-Admin APIs

### OAuth

The PowerBI integration uses OAuth 2.0 to connect Secoda to your Power BI workspace. To connect Power BI to Secoda follow the steps below:

1. Click **Integrations** in the sidebar, then **New integration** and select **Power BI**
2. Select **OAuth** tab
3. Click **Connect with OAuth**. You'll be brought to the login page and asks for permissions on your Power BI workspace
4. Upon successful completion of OAuth authentication with Power BI, click **Run Initial Sync** button.

### Azure AD App

Here are the steps to set up Power BI Integration using Azure AD App:

**Step 1**: Create an Azure AD App

* Open the [Azure portal](https://portal.azure.com/)
* Search for `App registrations`
* Click `+ New registration`
* Fill in the following details
  * **Name** - Secoda
  * **Supported account types** - Accounts in this organizational directory only (Default Directory only - Single tenant)
  * **Redirect URI (optional)** - Leave blank
* Click Register
* After submitting the form, the `Application ID` is available from the Overview tab. Copy and save the `Application ID` (Client ID) for later use
* Copy and save the `Tenant ID` for later use
* Click the **Certificates & secrets** tab
* Click the **New client secret** button
* In the Add a client secret window, enter any description, specify when you want the client secret to expire, and click **Add**.
* Copy and save the Client secret **value** for later use

**Step 2.1**: (Only applicable if you're using non-admin API)

* Go to **API permissions** tab, click Add a permission and add the following permissions:

<div align="left" data-full-width="false">

![](https://raw.githubusercontent.com/secoda/gitbook/master/.gitbook/assets/image%20\(9\).png)

</div>

**Step 2.2**: (Only applicable if you're using admin API)

* Open the [Azure portal](https://portal.azure.com/)
* Search for `Azure Active Directory` and select **Azure Active Directory** link
* Click the **Groups** tab
* Click the **New group** button
* Fill form in the required information:
  * **Group type** - Select "Security"
  * **Group name** - Type "PowerBI API Access"
  * **Group description** - Enter any description or leave empty
* Select "No members selected" to open a drawer. Search for `Secoda` and select **Secoda** entry. Click the **Select** button to confirm.
* Click **Create**

**Step 2.3**: (Only applicable if you're using admin API) Enable the Power BI service admin settings

* Open [Power BI admin portal](https://app.powerbi.com/admin-portal/) and sign in
* Log into the Power BI admin portal. You need to be a Power BI admin to see the tenant settings page
* Ensure that **Tenant settings** tab are open
* Search for the subsection "Allow service principals to use Power BI APIs" in "Developer settings" section and open it. Select "Enabled" and add the security group you created "PowerBI API Access" in Azure AD. Click **Apply**
* Repeat process for all subsection in "Admin API settings" section. Open the section, Select "Enabled" and add the security group you created "PowerBI API Access" in Azure AD. Click **Apply**. You must complete the step for following sections:
  * Allow service principals to use read-only admin APIs
  * Enhance admin APIs responses with detailed metadata
  * Enhance admin APIs responses with DAX and mashup expressions

**Step 3:** Add Azure AD app to your workspace

* Open [Power BI](https://app.powerbi.com/) and sign in
* Search to the workspace you want to enable access for, and from the _More menu_, select _Workspace access_

![](https://raw.githubusercontent.com/secoda/gitbook/master/.gitbook/assets/image%20\(10\).png)

* Fill form in the required information:
  * Search for `Secoda` as member and select **Secoda** entry
  * Permission - select "Viewer" or "Contributor"&#x20;
  * Click **Add** button to add
  * Click **Close** button to confirm

**Step 4:** Connect PowerBI API to Secoda:

* Click **Integrations** in the sidebar, then **New integration** and select **Power BI**
* Fill form in the required information referred in Step 1 above:
  * **Client ID:** Application ID of Azure AD.
  * **Tenant ID:** Identifier of tenant of organization in Azure Active AD.&#x20;
  * **Client Secret:** Client secret of the Azure AD App
* Click **Connect**



**Note:** &#x20;

* Non-admin API does not support extracting tables, columns and measures from PowerBI datasets (except for push datasets)
* You must be a PowerBI Admin in order to successfully go through the OAuth flow.
