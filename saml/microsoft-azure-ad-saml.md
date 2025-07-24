---
description: Set up Microsoft Azure SAML in three easy steps.
---

# Microsoft Azure AD SAML

## Steps

1.  Go to the Secoda app > Settings > Security > SAML. Copy the **ACS URL** and **Entity ID** for use in the following steps

    <figure><img src="../.gitbook/assets/Screenshot 2025-04-23 at 10.43.53 AM.png" alt=""><figcaption><p>Secoda app > Settings > Security > SAML</p></figcaption></figure>
2. Go to [portal.azure.com](http://portal.azure.com) and create a new **Enterprise application**. Click **Integrate any other application you don't find in the gallery (Non-gallery)**

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/9dcadac8-e209-4326-a14e-291dff8c646e.png" alt=""><figcaption></figcaption></figure>

3. Click "Single sign-on" followed by SAML. Edit the **Basic SAML Configuration**

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/6d729b1e-ed1b-4f5c-aebd-17e6c1242984.png" alt=""><figcaption></figcaption></figure>

4. Fill in **Reply URL** with the **ACS URL** copied from Step 1
5. Fill in **Identifier (Entity ID)** with the **Entity ID** copied from Step 1
6. Copy the **App Federation Metadata Url**

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/21c77090-b50a-454f-9cf0-12761f3882bd.png" alt=""><figcaption></figcaption></figure>

6. Navigate to the Secoda app > Settings > Security > SAML
7. Choose **Microsoft** as the SAML Provider (IdP)
8. Paste the **App Federation Metadata Url** under **Metadata URL**
9. Save this configuration

You will now be able to go to navigate to Secoda, click “Sign in with SAML”, and enter your domain to complete sign-in.
