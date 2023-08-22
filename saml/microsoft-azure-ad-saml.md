---
description: Set up Microsoft Azure SAML in three easy steps.
---

# Microsoft Azure AD SAML

### Step 1 - Redirect URI

Go to [portal.azure.com](http://portal.azure.com), create a new app registration (single tenant), and add the relevant redirect URI (include the trailing slash). Make sure you replace **company+com** with your email domain.

`https://<app|eu|apac>.secoda.co/api/v1/auth/saml/company+com/acs/`

For example, if your Secoda url is `eu.secoda.co` email is `brittany@abc.company.co` then the redirect URI should be:

`https://eu.secoda.co/api/v1/auth/saml/abc+company+co/acs/`

![](https://imagedelivery.net/28-eDrK8lEif6\_ED0iMQeg/01a2728a-9dd9-4a0f-eb72-5999686fcb00/public)

### Step 2 - Application ID URI

Go to “App Registrations”, click on the app you just created and then click the “Expose an API” tab, and enter a value in the “Application ID URI” field. This should be to the email domain you own. This is only for verification purposes, this url is never called or redirected to.

`https://<domain>/secoda`

Continuing with the example above, the Application ID URI field should be.&#x20;

`https://abc.company.co/secoda`

![](https://imagedelivery.net/28-eDrK8lEif6\_ED0iMQeg/d20fd411-d75e-4c17-550e-9976874a0c00/public)

### Step 3 - XML Link

Click “Endpoints” and copy the “Federation metadata document”. **This is an XML link that needs to be sent to the to the Secoda team.**

![](https://imagedelivery.net/28-eDrK8lEif6\_ED0iMQeg/344f8cf5-26b7-42d2-2665-bd2a61857e00/public)

Once Secoda has completed their steps, you will be able to go to navigate to Secoda, click “Sign in with SAML”, and enter your domain to complete sign-in.

