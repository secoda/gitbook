---
description: >-
  Learn about Secoda's options for logging into the app through single sign on
  and email
---

# Sign in options

There are a variety of ways to sign into Secoda, depending on your existing systems and levels of security. When first accessing the app at app.secoda.co, you'll be shown this screen below. You have the options to sign in with email, SAML, a Microsoft account or a Google account.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/6c847a24-4a22-4c1e-855f-8aec32354e20.png" alt=""><figcaption></figcaption></figure>

## Microsoft SSO, Google SSO and email

Continuing with email and password, Microsoft and Google are included in every contract. You don't need to configure anything in order to access Secoda in the following ways:

* **Continue with Microsoft:** Choose this option if your organization uses Microsoft for email, as this will allow you to sign in with SSO. The Azure Admin will likely have to authorize Secoda as an allowed application to enable SSO with Microsoft.
* **Continue with Google:** Choose this option if your organization uses Google for email, as this will allow you to sign in with SSO
* **Continue with email:** Choose this option if you don't have a Microsoft of Google email address

## SAML options

If you'd like to fine tune permissions and security, your organization can implement SAML SSO. For SAML, we have created guides for the following identity providers (IdPs):

* [Okta SAML SSO](../../saml/okta-saml.md)
* [Azure Active Directory SAML SSO](../../saml/microsoft-azure-ad-saml.md)
* [Google Workspace SAML SSO](../../saml/google-saml.md)
* [OneLogin SAML SSO](../../saml/onelogin-saml.md)

Enterprise plan subscribers can opt-in on the settings page to use:

* [SCIM](../../saml/scim.md)
* [SAML Attributes](../../saml/attributes.md)

## Enforce SSO type

Workspace admins have the option to enforce SSO with a specific identity provider (IdP). In Settings > Workspace Settings > Enforce SSO, a workspace admin can enforce Google OAuth, Microsoft OAuth, or SAML. Once chosen, users will not be able to login through email or another IdP. If they attempt to, they will be redirected to the type that you've specified.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/97ddc084-6ead-43c7-b4a1-7d07f494cc84.png" alt=""><figcaption></figcaption></figure>
