---
description: Manage users and groups from your SAML identity provider.
---

# SAML Attributes

Enterprise plan subscribers with SAML SSO enabled can configure SAML attributes to automatically manage user roles, group memberships, and team memberships in Secoda.

### Overview

When configuring SAML SSO with your identity provider, you can set up specific SAML attributes that will automatically map to user roles, group memberships, and team memberships in Secoda.

### Configure

#### Upgrade to the Enterprise plan

Contact us to upgrade to the Enterprise plan and enable SAML SSO.

#### Configuration

To configure SAML attributes, you'll need to add the following attributes to your SAML configuration in your identity provider:

{% tabs %}
{% tab title="Okta" %}
* In the Okta admin pages, open your Secoda application
* Navigate to the _Sign On_ tab
* Under _SAML 2.0 Configuration_, click _Edit_
* Add the following attributes:
  * `secodaRole` (string)
  * `secodaGroupMembership` (comma-separated list)
  * `secodaTeamMembership` (comma-separated list)
* Save your configuration
{% endtab %}

{% tab title="OneLogin" %}
* In OneLogin's Admin panel > Applications, select your Secoda application
* Go to the _Configuration_ tab
* Under _Parameters_, add the following attributes:
  * `secodaRole` (string)
  * `secodaGroupMembership` (comma-separated list)
  * `secodaTeamMembership` (comma-separated list)
* Save your configuration
{% endtab %}

{% tab title="Azure AD" %}
1. In Azure portal, go to Azure Active Directory -> Enterprise Applications
2. Select your Secoda application
3. Go to _Single sign-on_ in the left panel
4. Under _User Attributes & Claims_, click _Edit_
5. Add the following claims:
   * `secodaRole` (string)
   * `secodaGroupMembership` (comma-separated list)
   * `secodaTeamMembership` (comma-separated list)
6. Save your configuration
{% endtab %}
{% endtabs %}

### Attribute Mapping

The following SAML attributes are supported for automatic user management:

1. `secodaRole` (string)
   * Maps to the `User` model role
   * Stored in the `_role` property on `User`
   * Example: `"admin"`, `"editor"`, `"viewer"`

2. `secodaGroupMembership` (comma-separated list)
   * Maps to `Group` model membership
   * Users will be automatically added to groups with matching names
   * Example: `"Data Engineers,Analysts"`

3. `secodaTeamMembership` (comma-separated list)
   * Maps to `Team` model membership
   * Users will be automatically added to teams with matching names
   * Example: `"Engineering,Product"`

{% hint style="info" %}
Groups and teams must exist in Secoda before they can be mapped via SAML attributes. If a group or team doesn't exist, the membership will be skipped.
{% endhint %}
