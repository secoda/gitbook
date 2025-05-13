---
description: Manage users and groups from your identify provider.
---

# SCIM

### Overview

Enterprise plan subscribers with SAML SSO enabled can opt to enable SCIM for their workspace. SCIM, or _System for Cross-domain Identity Management_, is an open standard that allows for the automation of user provisioning. If you have SAML SSO enabled with a supported identity provider, you can contact us to get SCIM enabled for your workspace.

### Configure

To configure SCIM, you'll need to add a Token and URL to your SCIM provider.

The SCIM token is the [API access token](../secoda-api/authentication.md#step-1-create-an-api-key). As an Admin, you can generate one by navigating to Settings > API.

{% hint style="info" %}
Your SCIM URL may be under a custom domain at https://\<CUSTOM>/api/v1/auth/scim/
{% endhint %}

Follow the directions below for your identity provider to setup the SCIM integration.

{% tabs %}
{% tab title="Okta" %}
* In the Okta admin pages, open the Secoda application you have for SAML 2.0
* In the _General_ tab, click _Edit_ and choose _SCIM_ in the Provisioning section and _Save_
* In the _Provisioning_ tab, enter the `https://app.secoda.co/api/v1/auth/scim/`
* For the _Unique identifier_ field for users section enter **email**
* For _Supported provisioning actions_ you can enable "Import New Users and Profile Updates", "Push New Users" and "Push Profile Updates", "Push and Import for Groups".
* For _Authentication mode_ field, choose HTTP Header and enter your Bearer token generated from your API settings in Secoda. You can now test the configuration and save
{% endtab %}

{% tab title="OneLogin" %}
* In OneLogin's Admin panel > Applications, click _Add App_
* Search for the "SCIM Provisioner with SAML (SCIM v2 Enterprise, full SAML)" app and add
* Click on the _Configuration_ tab and add your SCIM base URL as `https://app.secoda.co/api/v1/auth/scim/` and the Bearer token generated from your API settings in Secoda.
* Click on the _Provisioning_ tab and Enable Provisioning
* Save your App
{% endtab %}

{% tab title="Azure AD" %}


1. In Azure portal, go to Azure Active Directory -> Enterprise Applications.
2. Select an existing application or create a new one by searching for the specific application in the gallery.
3. In the application management screen, choose Provisioning in the left panel.
4. Under Provisioning Mode, select Automatic.
5. In Admin Credentials, enter the Tenant URL (e.g., `https://app.secoda.co/api/v1/auth/scim/`) and a Secret Token generated from your API settings in Secoda.
6. Expand Mappings and configure user attributes. Set mappings like `userPrincipalName` to `userName`, `mail` to `emails[type eq "work"].value`, etc.
7. Ensure Create, Update, and Delete actions are selected under Target Object actions.
8. Save the configuration
{% endtab %}
{% endtabs %}

### Group syncing

Secoda's SCIM integration also supports group syncing. From your side all you have to do is start pushing groups from your Identity provider to Secoda. These will then map one to one with [groups.md](../user-management/groups.md "mention") in Secoda.&#x20;

When syncing groups, the following attributes are supported:

* `displayName`: The name of the group in Secoda
* `members`: Array of user references that belong to the group

```json
PUT /api/v1/auth/scim/Groups/{group_id}
Content-Type: application/json
Authorization: Bearer {your_access_token}

{
  "schemas": ["urn:ietf:params:scim:schemas:core:2.0:Group"],
  "displayName": "{group_name}",
  "members": [
    {
      "value": "{user_id_1}",
      "display": "{user_1_display_name}"
    }
    // Add other members here if needed, for example:
    // ,
    // {
    //   "value": "{user_id_2}",
    //   "display": "{user_2_display_name}"
    // }
  ]
}

```

### Adding users

To add an active or disabled user using SCIM you can make a PUT request. Here is an example of how to use SCIM to add a user.

```json
PUT /api/v1/auth/scim/Users/{user_id}
Content-Type: application/json
Authorization: Bearer {access_token}

{
  "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
  "userName": "{user_email}",
  "name": {
    "givenName": "{user_first_name}",
    "familyName": "{user_last_name}"
  },
  "emails": [
    {
      "value": "{user_email}",
      "primary": true,
      "type": "work"
    }
  ],
  "active": true,
  "externalId": "{scim_external_id}"
}
```

Setting `"active": false` will disable the user, while setting it to `"active": true` would activate the user.
