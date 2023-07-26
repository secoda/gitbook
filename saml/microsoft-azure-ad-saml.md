# Microsoft Azure AD SAML

## Steps:

Go to [portal.azure.com](http://portal.azure.com), create a new app registration (single tenant), and add the relevant redirect URI (include the trailing slash). Make sure you replace **company+com** with your domain. For example, `apple.com` becomes `apple+com`.

`https://<app|eu|apac|>.secoda.co/api/v1/auth/saml/company+com/acs/`

![](https://imagedelivery.net/28-eDrK8lEif6\_ED0iMQeg/01a2728a-9dd9-4a0f-eb72-5999686fcb00/public)

Go to “App Registrations”, click on the app you just created and then click the “Expose an API” tab, and enter a value in the “Application ID URI” field. This should be to a domain you own. This is only for verification purposes, this url is never called or redirected to.

`https://<apple|tesla|starbucks>.com/secoda`

![](https://imagedelivery.net/28-eDrK8lEif6\_ED0iMQeg/d20fd411-d75e-4c17-550e-9976874a0c00/public)

Click “Endpoints” and copy the “Federation metadata document”. **Send that link to the Secoda team.**

![](https://imagedelivery.net/28-eDrK8lEif6\_ED0iMQeg/344f8cf5-26b7-42d2-2665-bd2a61857e00/public)

Once Secoda has completed their steps, you will be able to go to [https://app.secoda.co](https://app.secoda.co), click “Sign in with SAML”, enter your domain to complete sign-in.

