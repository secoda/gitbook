# Google OAuth Application (on-premise)

To configure an OAuth consent screen and generate OAuth credentials for Google BigQuery or Looker Data Studio, follow these steps:

1. **Access the Google Cloud Console**
   * Navigate to the Google Cloud Console.
   * Ensure you're logged into your Google account and have selected the appropriate project.
2. **Configure the OAuth Consent Screen**
   * In the left-hand menu, select **APIs & Services** and then click on **OAuth consent screen**.
   * **User Type**:
     * Choose **External**.
     * Click **Create**.
   * **App Information**:
     * **App name**: Enter a name for your application (e.g., `Secoda_GBQ`).
     * **User support email**: Provide an email address for users to contact in case of issues.
   * **Authorized Domains**:
     * Click **+ Add Domain**.
     * Enter the domain of your Secoda instance. For example, if your instance URL is `https://<instance_name>.co/`, the domain is `<instance_name>.co`.
   * **Developer Contact Information**:
     * Enter one or more email addresses for Google to contact you about your project.
   * Click **Save and Continue**.
   * **Scopes**:
     * Click **Add or Remove Scopes**.
     * Add the following scope for bigquery:
       * `https://www.googleapis.com/auth/bigquery.readonly`
     * Add the following scope for looker data studio:
       * `https://www.googleapis.com/auth/datastudio.readonly`
     * Click **Update**.
     * Click **Save and Continue**.
   * **Summary**:
     * Review the information and click **Back to Dashboard**.
3. **Generate OAuth Credentials**
   * In the left-hand menu, select **APIs & Services** and then click on **Credentials**.
   * Click on **+ Create Credentials** and select **OAuth client ID**.
   * **Application Type**:
     * Choose **Web application**.
   * **Name**:
     * Enter a name for the OAuth client (e.g., `ConnectionsOAuth`).
   * **Authorized Redirect URIs**:
     * Click **+ Add URI**.
     * Enter the following URIs:
       * `https://<instance_name>.co/api/v1/oauth/bigquery/`
       * `https://<instance_name>.co/api/v1/oauth/gds/`
       * Replace with your actual Secoda instance URL.
   * Click **Create**.
   * A dialog will appear displaying your **Client ID** and **Client Secret**.
     * **Important**: Copy and securely store these credentials, as you'll need them to configure the OAuth connection in Secoda.

By completing these steps, you've successfully configured the OAuth consent screen and generated the necessary OAuth credentials to establish a connection between Secoda and Google BigQuery and/or Looker Data Studio.

