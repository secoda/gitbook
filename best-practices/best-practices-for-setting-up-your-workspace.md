---
description: Learn about some best practices for setting up that we've seen work well
---

# Setting up your workspace

After configuring your integrations and importing metadata, it's essential to consider the layout and structure of your workspace. This guide outlines best practices for effectively organizing your workspace and features to ensure new users are well-prepared upon onboarding.

## **Organizing Teams**

Teams are the primary way to manage your organization's resources. Learn more about the capabilities and setup process for Teams [here](../user-management/teams.md).

### **General Team Usage**

By default, all metadata from connected integrations is accessible via the General Team Catalog. The General Team is set to Public, but you can change it to Private or rename it in the Team Settings.

**Use cases for the Public 'General' Team:**

* Serve as a common space for all workspace users to access.
* House a dictionary of commonly used terms, metrics, and acronyms.
* Store internal processes and best practices documentation.
* Include onboarding documents for new users to navigate the workspace.

### **Creating Specific Teams**

1. **Identify Your Users**: Start by identifying both your current and potential future users. Determine their roles and consider grouping them to streamline access management. For a detailed understanding of how Roles, Teams, and Groups interact within our RBAC framework, refer to our [user-management](../user-management/ "mention") documentation.
2. **Establish Teams**: Create Teams reflecting the departments or roles of your users. For example:
   * If your initial power users are part of the Data Platform team, create a "Data Platform" Team and add relevant users or [Groups](../user-management/groups.md).
   * For future rollouts to the Business Intelligence team, prepare a "Business Intelligence" Team for upcoming onboarding.

#### **Customizing Teams**

* **Sidebar Customization**: [Adjust the sidebar](../user-management/teams.md#customizing-your-teams-sidebar) to match the access needs of each Team. For example, less technical users might only need access to specific Collections, so you can choose to hide unnecessary sections like the Catalog, Dictionary, Documents, or Questions.
* **Assign Integrations or Resources to Teams**: To limit which metadata is added to each Team, at the highest level you can [add whole integrations to Teams in the settings](../getting-started/secoda-as-an-admin/connect-your-data/#how-to-add-integrations). Utilize [these tricks](../features/catalog.md#limiting-resource-access-in-a-catalog) to add only necessary schemas, tables, and columns to each Team.&#x20;

## Automating documentation

Secoda offers several features to help automate the enrichment and documentation of your data. For more details, check out [documentation-best-practices.md](documentation-best-practices.md "mention").

#### **Initial Documentation Setup**&#x20;

Creating robust documentation from the start is crucial. Ensure that Documents, Dictionary terms, and Catalog resource descriptions are well-documented to showcase Secoda's value immediately to new users. This initial content not only helps in accurate searches but also enhances the AI Assistant’s functionality.

#### **Prioritizing Certain Documentation**&#x20;

Begin by documenting the most frequently used resources, especially those relevant to the initial users you're bringing into Secoda. Use the [verified-tag.md](../resource-and-metadata-management/tags/verified-tag.md "mention") tag to signify that these resources are business-approved and provide the most reliable data.

## **Building Out FAQs**&#x20;

Leverage Secoda's Questions feature to support new users effectively. Admins should pre-populate the Questions section with FAQs, providing answers and marking correct responses. This helps guide new users and facilitates their engagement with the data team.

## **Integrating with Slack**&#x20;

Integrate Secoda with Slack to enhance internal communications. This integration allows users to query data through Slack and receive workspace notifications without leaving the platform. Learn more about [setting up](slack-less-than-greater-than-questions-workflow.md) and [using the Slack integration](../integrations/productivity-tools/slack-connection/slack-user-guide.md) here.

## **Creating Search Views**&#x20;

Develop [Search views](../features/views.md) to aid Search navigation for new users. These views, once saved, are accessible to all users, helping them locate needed information efficiently.

## **Enhancing the Homepage**&#x20;

The [#team-homepage](../features/homepage.md#team-homepage "mention") is the first interface users interact with in Secoda. Enhance user experience by pinning critical resources and writing notes in the Notepad feature. Explore how-to videos on optimizing Homepage functionality [here](../features/homepage.md).
