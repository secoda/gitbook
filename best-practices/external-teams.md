---
description: Best practices for exposing Secoda to your external customers or clients
---

# Exposing Secoda to External Clients

Several of Secoda's users use Secoda as a tool to organize data for their own company's external customers. In these cases, they would not want their customers to have any awareness of one another for security reasons. There are a few best practices you may want to follow to ensure that users are only seeing the content and usernames specific to their organization.&#x20;

## Setting up Teams for your clients

If set up in the following way, the affected users will:

* Only be able to search for or view **resources** within the team
* Only be able to search for or view **users** within the team
* Not be able to search for or view any other **teams** within the workspace

1. In the [Members Settings](https://app.secoda.co/settings/members), set the user's roles to Guest
   * _Guests in Secoda will only see usernames of the Team that they are apart of._&#x20;
2. Create Private team(s) for your external customers
   * [_Read up on how to make a Team Private_](../user-management/teams.md#creating-teams)_._
3. Add the relevant users to their corresponding Private team(s)
   * Consider setting up [Groups](../user-management/groups.md) for your clients.
4. Add relevant resources to those team(s)
   * _Resources in Private teams will not show up in search results to anyone who does not have access to that Private team._
   * _Tip: Use an_ [_Automation_](../features/automations.md) _to pull resources into Teams in bulk._
