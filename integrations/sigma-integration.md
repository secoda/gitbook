# Sigma Integration

## **Getting Started with Sigma** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

There are three steps to get started using Sigma with Secoda:

1. Create a Sigma Client ID and Client Secret
2. Retrieve your Sigma host URL
3. Connect Sigma to Secoda

#### **Create an Client ID and Client Secret** <a href="#h_0d871f44cf" id="h_0d871f44cf"></a>

To create a Sigma access token for Secoda visit Sigma and log into your account. Use the following steps to generate an access token:

1. Click on your avatar in the top right and select 'Administration' from the dropdown menu.
2. Click the option **APIs and Embed Secrets**
3. Click **Create New** in the top right

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

4. Fill out the form with the Name and Owner. Make sure that the owner is an Administrator.
5. Copy the Client ID and Secret and save it. This will be used to connect to Secoda.

#### **Retrieve your Sigma host** <a href="#h_2e32c48e7f" id="h_2e32c48e7f"></a>

In the **Administrator** settings go to **Account.** In the top under the **Site** you can see which cloud your hosted on, either AWS or GCP.

<figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

The host parameter is https://api.sigmacomputing.com for GCP organizations and https://aws-api.sigmacomputing.com for AWS organizations.

#### **Connect Sigma to Secoda** <a href="#h_b1c101d905" id="h_b1c101d905"></a>

After retrieving your Sigma client ID, secret and host , the next step is to connect to Secoda:

1. In the Secoda App, select **Add Integration** on the Integrations tab
2. Search for and select **Sigma**
3. Enter your Sigma client ID, secret, and host you retrieved above
4. Click **Connect**
