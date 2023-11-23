---
description: Manage users and groups from your identify provider.
---

# SCIM

Enterprise plan subscribers with SAML SSO enabled can opt to enable SCIM for their workspace. SCIM, or _System for Cross-domain Identity Management_, is an open standard that allows for the automation of user provisioning.

### Overview

If you have SAML SSO enabled with a supported identity provider, you can contact us to get SCIM enabled for your workspace.

### Configure

#### Upgrade to the Enterprise plan

Contact us to upgrade to the Enterprise plan and enable SAML SSO.

#### Configuration

To configure SCIM, you'll need to add a Token and URL to your SCIM provider.

The SCIM token is the same as the [API access token](../secoda-api/authentication.md#step-1-create-an-api-key) in Secoda. As an Admin, you can self generate it by navigating to Settings page, and clicking on API under the Workspace heading.  The SCIM URL is `https://app.secoda.co/api/v1/auth/scim`.&#x20;

{% hint style="info" %}
If you have a custom Secoda domain, the SCIM URL will be https://your-custom-domain.secoda.co/api/v1/auth/scim
{% endhint %}

Follow the directions below for your identity provider to setup the SCIM integration.

{% tabs %}
{% tab title="Okta" %}
* In the Okta admin pages, open the Secoda application you have for SAML 2.0
* In the _General_ tab, click _Edit_ and choose _SCIM_ in the Provisioning section and _Save_
* In the _Provisioning_ tab, enter the https://app.secoda.co/api/v1/auth/scim
* For the _Unique identifier_ field for users section enter **email**
* For _Supported provisioning actions_ you can enable "Import New Users and Profile Updates", "Push New Users" and "Push Profile Updates", "Push and Import for Groups".
* For _Authentication mode_ field, choose HTTP Header and enter your Bearer token generated from your API settings in Secoda. You can now test the configuration and save
{% endtab %}

{% tab title="OneLogin" %}
* In OneLogin's Admin panel > Applications, click _Add App_
* Search for the "SCIM Provisioner with SAML (SCIM v2 Enterprise, full SAML)" app and add
* Click on the _Configuration_ tab and add your SCIM base URL as https://app.secoda.co/api/v1/auth/scim and the Bearer token generated from your API settings in Secoda.
* Click on the _Provisioning_ tab and Enable Provisioning
* Save your App
{% endtab %}
{% endtabs %}
