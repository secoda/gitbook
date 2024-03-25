---
description: >-
  This document goes through best practices when exposing your Secoda workspace
  to external clients.
---

# Exposing Secoda to External Clients

{% hint style="danger" %}
This feature is coming soon.&#x20;
{% endhint %}

Several of Secoda's users use Secoda as a tool to organize data for their own company's external customers. In these cases, they would not want their customers to have any awareness of one another for security reasons. There are a few best practices you may want to follow to ensure that users are only seeing the content and usernames specific to their organization.&#x20;

If set up in the following way, the affected users will:

* Only be able to search for or view **resources** within the team
* Only be able to search for or view **users** within the team
* Not be able to search for or view any other **teams** within the workspace

1. In the [Members Settings](https://app.secoda.co/settings/members), set the user's roles to Guest
   * _Guests in Secoda will only see usernames of the team that they are apart of._&#x20;
2. Create Private team(s) for your external customers
   * [_Read up on how to make a Team Private_](../user-management/teams.md#creating-teams)_._
3. Add the relevant users to their corresponding Private team(s)
4. Add relevant resources to those team(s)
   * _Resources in Private teams will not show up in search results to anyone who does not have access to that Private team._
