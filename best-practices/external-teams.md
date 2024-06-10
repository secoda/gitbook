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

1. Create a Private Team for each external customer
   * [_Read up on how to make a Team Private_](../user-management/teams.md#creating-teams)_._
2. User Role Configuration
   * **Assign 'Guest' Role**: In the [Members Settings](https://app.secoda.co/settings/members), set the user's roles to Guest when adding them to Secoda.
     * _Guests in Secoda will only see usernames of the Team that they are apart of._&#x20;
     * _Note: All other roles will get pulled into the default Team (General), even if it is Private. For enhanced security, ensure these users are Guests._
   * **Add Users to Teams**: Add the relevant users to their corresponding Private team(s) in the Teams Settings.
     * Consider setting up [Groups](../user-management/groups.md) for your clients.
3. Resource Management
   * **Add Resources**: Add relevant resources into the respective Private Teams.
   * **Search Visibility**: Resources in Private Teams are hidden from search results for users outside that Team.
   * **Automations**: Use _an_ [_Automation_](../features/automations.md) for bulk resource allocation.
   * _Note: Adding a parent resource (e.g., a database table) automatically adds child resources (e.g., columns in the table) into the Team._&#x20;

By following these guidelines, you can effectively manage data access for external customers using Secoda, ensuring that each customer's information remains secure and isolated.
