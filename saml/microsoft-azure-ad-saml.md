---
description: Set up Microsoft Azure SAML in three easy steps.
---

# Microsoft Azure AD SAML

### Step 1 - Create the application

Go to [portal.azure.com](http://portal.azure.com), create a new **Enterprise application**. Click **"Integrate any other application you don't find in the gallery (Non-gallery)"**

<figure><img src="../.gitbook/assets/Screenshot 2024-08-29 at 1.57.06 PM.png" alt=""><figcaption></figcaption></figure>



Click "Single sign-on" followed by SAML. Edit the **"Basic SAML Configuration".**

<figure><img src="../.gitbook/assets/Screenshot 2024-08-29 at 1.59.11 PM.png" alt=""><figcaption></figcaption></figure>



Fill in the following **3** values and hit save.

<table><thead><tr><th width="141">Property</th><th width="246">Value</th><th>Example</th><th>Notes</th></tr></thead><tbody><tr><td><strong>Identifier (Entity ID)</strong></td><td><code>https://&#x3C;YOUR_COMPANY_DOMAIN>/secoda</code></td><td><code>https://company.com/secoda</code></td><td>No trailing slash.</td></tr><tr><td><strong>Reply URL (ACS URL)</strong></td><td><code>https://&#x3C;APP|EU|APAC>.secoda.co/api/v1/auth/saml/&#x3C;YOUR_EMAIL_DOMAIN_WITH_PLUS>/acs/</code></td><td><code>https://eu.secoda.co/api/v1/auth/saml/company+com/acs/</code></td><td>Include a trailing slash.</td></tr><tr><td><strong>Sign on URL</strong> </td><td><code>https://&#x3C;APP|EU|APAC>.secoda.co/api/v1/auth/saml/&#x3C;YOUR_EMAIL_DOMAIN_WITH_PLUS>/acs/</code></td><td><code>https://eu.secoda.co/api/v1/auth/saml/company+com/acs/</code></td><td>Include a trailing slash.</td></tr></tbody></table>



Then copy the **App Federation Metadata Url**.

<figure><img src="../.gitbook/assets/Screenshot 2024-08-29 at 2.07.49 PM.png" alt=""><figcaption></figcaption></figure>

### Step 2 - Request the application in Secoda

1. Navigate to the Secoda app > Settings > Security > SAML
2. Choose **Microsoft** as the SAML Provider (IDP)
3. Paste the **App Federation Metadata Url** under "Metadata URL".
4. Click Request which will alert the Secoda team of your request.

Once Secoda has completed their steps, you will be able to go to navigate to Secoda, click “Sign in with SAML”, and enter your domain to complete sign-in.
