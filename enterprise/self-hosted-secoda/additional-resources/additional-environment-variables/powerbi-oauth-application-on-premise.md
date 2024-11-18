# PowerBI OAuth Application (on-premise)

To configure OAuth for your Microsoft Power BI application in Azure Active Directory (Azure AD), follow these steps:

1. **Access the Microsoft Azure Portal**
   * Navigate to the [Azure Portal](https://portal.azure.com/).
   * In the left-hand menu, select **App registrations**.
   * Click on **+ New registration**.
2. **Register a New Application**
   * **Name**: Enter a descriptive name for your application.
   * **Supported account types**: Choose **Accounts in this organizational directory only (\<directory name> only - Single tenant)**.
   * **Redirect URI**:
     * Set the type to **Web**.
     * Enter the URI: `https://<instance_name>.co/api/v1/oauth/pbi/`
   * Click **Register**.
3. **Configure Authentication Settings**
   * After registration, navigate to the **Authentication** tab.
   * In the **Implicit grant and hybrid flows** section, enable **Access tokens (used for implicit flows)**.
   * Click **Save**.
4. **Add Required API Permissions**
   * Go to the **API permissions** tab.
   * Click on **+ Add a permission**.
   * **For Power BI Service**:
     * Select **Power BI Service**.
     * Choose **Delegated permissions**.
     * Enable the following permissions:
       * **App.Read.All**
       * **Dashboard.Read.All**
       * **Dataset.Read.All**
       * **Report.Read.All**
       * **Workspace.Read.All**
     * Click **Add permissions**.
5. **Grant Admin Consent**
   * In the **API permissions** tab, click on **Grant admin consent for \<directory name>**.
   * Confirm by clicking **Yes**.
6. **Add a Client Secret (Optional)**
   * Navigate to the **Certificates & secrets** tab.
   * Click on **+ New client secret**.
   * Provide a description and set an expiration period.
   * Click **Add**.
   * Copy and securely store the **Value** of the client secret; you'll need it later.
7. **Retrieve the Application (Client) ID**
   * Go to the **Overview** tab of your registered application.
   * Note down the **Application (client) ID**; this will be required for integration.

By completing these steps, you've successfully registered an application in Azure AD for use with Microsoft Power BI, enabling OAuth authentication.
