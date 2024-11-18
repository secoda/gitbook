# Github Application (on-premise)

To configure a Github App for use within Secoda,

* **Access Account Settings**:
  * Click your profile photo in the upper-right corner of any GitHub page.
  * For a personal account:
    * Click **Settings**.
  * For an organization account:
    * Click **Your organizations**.
    * Next to the organization, click **Settings**.
* **Navigate to Developer Settings**:
  * In the left sidebar, click **Developer settings**.
  * Then, click **GitHub Apps**.
* **Create a New GitHub App**:
  * Click **New GitHub App**.
* **Configure the App**:
  * **Name**: Enter a clear and concise name for your app (up to 34 characters). This name must be unique across GitHub.
* **Set Permissions and Subscribe to Events**:
  * Under **Permissions**, select the following permissions:
    * Pull requests: Read and write
    * Profile: Read and write
    * Contents: Read and write
    * Metadata: Read only
  * Under **Subscribe to events**, select the webhook events your app should receive:
    * ﻿﻿Pull request
* **Define Installation Scope**:
  * Under **Where can this GitHub App be installed?**, choose **Only on this account** or **Any account**.
* **Create the App**:
  * Click **Create GitHub App** to finalize the registration.
    * Generate a client secret and private key.
