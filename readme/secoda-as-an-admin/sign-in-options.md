---
description: >-
  Learn about Secoda's options for logging into the app through single sign on
  and email
---

# Sign in options

There are a variety of ways to sign into Secoda, depending on your existing systems and levels of security. When first accessing the app at app.secoda.co, you'll be shown this screen below. You have the options to sign in with email, SAML, a Microsoft account or a Google account.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/6c847a24-4a22-4c1e-855f-8aec32354e20.png" alt=""></figure>

## Microsoft SSO, Google SSO and email

Continuing with email and password, Microsoft and Google are included in every contract. You don't need to configure anything in order to access Secoda in the following ways:

* **Continue with Microsoft:** Choose this option if your organization uses Microsoft for email, as this will allow you to sign in with SSO. The Azure Admin will likely have to authorize Secoda as an allowed application to enable SSO with Microsoft.&#x20;
* **Continue with Google:** Choose this option if your organization uses Google for email, as this will allow you to sign in with SSO
* **Continue with email:** Choose this option if you don't have a Microsoft of Google email address

## SAML options

If you'd like to fine tune permissions and security, you can implement your own SSO using SAML technology. SAML requires some additional setup, which is outlined in the documents linked below. For SAML, we offer the following providers:

* [Microsoft Azure Active Directory SAML](../../saml/microsoft-azure-ad-saml.md)
* [Okta SAML](../../saml/okta-saml.md)
* [OneLogin SAML](../../saml/onelogin-saml.md)
* [Google SAML](../../saml/google-saml.md)

Enterprise plan subscribers with SAML SSO enabled can opt to enable [SCIM](../../saml/scim.md).

## Enforce SSO type

Admins can require users to sign in with a specific type of SSO. Go to Settings > Workspace Settings > Enforce SSO. You then can choose between Google, Microsoft or SAML. Once you choose, users won't be able to login through email or any other means. If they attempt to, it will redirect them to the type that you've specified.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/97ddc084-6ead-43c7-b4a1-7d07f494cc84.png" alt=""></figure>
