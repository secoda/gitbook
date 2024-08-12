---
description: >-
  This guide details the setup and management of Roles, Groups, Teams, and
  Collections in Secoda, ensuring secure and efficient access control across the
  platform.
---

# User Management

## **Introduction**

Role-Based Access Control (RBAC) in Secoda is designed to ensure that only authorized users have access to specific resources, protecting sensitive information and enhancing platform functionality. This guide outlines how Secoda utilizes Roles, Groups, Teams, and Collections to manage access and permissions efficiently.

Permissions in Secoda are inherited hierarchically. When you grant someone access to a Team, they automatically gain access to all resources within that Team. Similarly, giving someone access to a Collection grants them access to all resources within that Collection. If you'd like to limit resources access at an individual level, check out [sharing-resources.md](roles/sharing-resources.md "mention").

## **Teams**&#x20;

Teams are made up of individual members or groups and serve as the primary way to assign access to resources within Secoda. You can customize Teams to fit specific needs:

* **Resource Access:** Define what resources a team can access, ranging from comprehensive (like multiple integrations) to selective (such as a single column).
* **Feature Visibility:** Customize the end-user experience by toggling off specific features like Metrics or Catalog visibility. This helps streamline the interface for team members, making it simpler and more focused on their needs.
* **Types of Teams:** Teams can be Public, open to any user, or Private, requiring an invitation to join.

For more details on teams, see [teams.md](teams.md "mention").

## Roles

Each member in Secoda is assigned a role that defines what they can do:

* **Viewer:** Can view metadata and resources within the Teams they belong to but cannot make changes or add new content.
* **Editor:** Can edit metadata, add new content, and modify existing resources within any public Team where they hold editor permissions.
* **Admin:** Controls the entire platform, managing roles, settings, and all content across all Teams.

{% hint style="info" %}
**Role Customization at the Team Level:** In Secoda, you can further customize access by adjusting a member’s role within specific teams. For example, a member might be an Editor at the organization level but restricted to a Viewer role in a sensitive team. This flexibility allows for precise control over who can view and edit resources within each team, enhancing security and compliance.
{% endhint %}

For more details on roles, see [roles](roles/ "mention").

## **Groups**&#x20;

Groups are sets of members who share common access needs, simplifying the management of permissions. Groups can also be used to set Ownership of resources at the Group level, instead of at an individual level.

For more details on groups, see [groups.md](groups.md "mention").

## **Collections**&#x20;

Collections are folders within a Team that hold resources related to a specific function, theme or department. For example, a "Revenue" collection within the Finance Team might include all necessary reports, tables, definitions, and documents about revenue.

For more details on collections, see [collections-1.md](../features/collections-1.md "mention").

## **Practical Example: Role, Team, Group and Collections Dynamics**&#x20;

Imagine onboarding both the Business Intelligence and Marketing departments into Secoda. You'd like each team to have a dedicated space to develop and manage resources essential to their daily operations. Here's how to set it up efficiently:

* **Team Creation:** Create the Teams and decide whether or not users should freely be able to join any Team, by setting them as Public or Private.
* **Group Creation:** Form Groups like 'Marketing Editorial Group' (Editors) and 'Marketing Business Users' (Viewers) based on the Marketing team's needs and assign members to them appropriately. Add these groups to the Marketing team.
* **Inter-Team Collaboration:** Suppose Marketing Editors frequently collaborate with the BI team, requiring access to certain BI dashboards. You could:
  * Add the Marketing Editors Group to the BI team, but alter their permissions within that Team to be Viewers.
  * For ease of discovery, the BI team could gather a folder of the key BI dashboards into a Collection in their Team for the Marketing Team's consumption.

This setup ensures everyone has the appropriate level of access while maintaining tight control over important data.

## Video Resource

{% embed url="https://www.loom.com/share/87e16857e8394a81ad5935de0a551208" %}
