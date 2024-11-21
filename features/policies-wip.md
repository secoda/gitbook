---
hidden: true
---

# Policies \[WIP]

### Introduction[​](https://datahubproject.io/docs/authorization/policies#introduction) <a href="#introduction" id="introduction"></a>

Secoda provides the ability to declare fine-grained access control Policies. A few examples of policies are

* Dataset Owners should be allowed to edit documentation, but not Tags.
* Jenny, our Data Steward, should be allowed to edit Tags for any Dashboard, but no other metadata.
* James, a Data Analyst, should be allowed to edit the Related Resources for a specific Data Pipeline he is a downstream consumer of.
* The Data Platform team should be allowed to manage users & groups, view platform analytics, & manage policies themselves.

{% hint style="info" %}
Policies are only enabled for Premium and Enterprise tiers.
{% endhint %}

### What is a Policy?[​](https://datahubproject.io/docs/authorization/policies#what-is-a-policy) <a href="#what-is-a-policy" id="what-is-a-policy"></a>

All policies consist of privileges (see all privileges below) and are applied to Roles to be associated with users. There are 2 types of Policies within Secoda:

1. Platform Policies
2. Resource Policies

#### Platform Policies[​](https://datahubproject.io/docs/authorization/policies#platform-policies) <a href="#platform-policies" id="platform-policies"></a>

**Platform** policies determine who has platform-level privileges on Secoda. Examples of these privileges include

* Managing Users & Groups
* Viewing the Secoda Analytics
* Managing Policies&#x20;

Platform policies consist of just privileges, e.g, "Can view Analytics". Platform policies do not include a specific "target resource" against which the Policies apply. Instead, they simply serve to assign specific privileges.

#### Resource Policies[​](https://datahubproject.io/docs/authorization/policies#metadata-policies) <a href="#metadata-policies" id="metadata-policies"></a>

**Resource** policies determine who can do what to which Resources. For example,

* Who can edit Tables Documentation & Related Resources?
* Who can add Owners to a Chart?
* Who can add Tags to a Dashboard?

A Metadata Policy can be broken down into 2 parts:

1. **Resources**: The _which_. Resources that the policy applies to, e.g. "All Tables".
2. **Privileges**: The _what_. What actions are being permitted by a policy, e.g. "Add Tags".

**Resources**[**​**](https://datahubproject.io/docs/authorization/policies#resources)

Subsets of resources can be associated with the policy by leveraging [filters.md](filters.md "mention"). This uses the same capabilities that the filters in search, catalog, and many places in the application uses. Some examples of filters include:

1. Resources from a specific integration, e.g, Snowflake
2. Resources of a specific type, e.g, Tables
3. Resources that contain a specific tag
4. Resources that are marked as PII

**Privileges**[**​**](https://datahubproject.io/docs/authorization/policies#privileges)

Check out the full list of privileges below.&#x20;

### Managing Policies[​](https://datahubproject.io/docs/authorization/policies#managing-policies) <a href="#managing-policies" id="managing-policies"></a>

Policies can be managed on the page **Settings > Members > Policies** tab. The `Policies` tab will only be visible to those users having the `Manage Policies` privilege.

Out of the box, Secoda is deployed with a set of default Policies. The set of default policies are Viewers, Editors, and Admins.

<figure><img src="../.gitbook/assets/Policy.png" alt=""><figcaption></figcaption></figure>



### Privileges[​](https://datahubproject.io/docs/authorization/policies#reference) \[WIP] <a href="#reference" id="reference"></a>

#### Platform-level privileges[​](https://datahubproject.io/docs/authorization/policies#platform-level-privileges) <a href="#platform-level-privileges" id="platform-level-privileges"></a>

These privileges are for Secoda operators to access & manage the administrative functionality of the system.

**Access & Credentials**[**​**](https://datahubproject.io/docs/authorization/policies#access--credentials)

| Privileges            | Description                                                                                                                  |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Generate API Keys     | Allow user to generate personal access tokens for use with Secoda APIs.                                                      |
| Manage Policies       | Allow user to create and remove access control policies. Be careful - Users with this privilege are effectively super users. |
| Manage Users & Groups | Allow user to create, remove, and update users and groups on Secoda.                                                         |
| Manage Integrations   | Allow user to manage integrations to Secoda.                                                                                 |

**Product Features**[**​**](https://datahubproject.io/docs/authorization/policies#product-features)

| Privileges                | Description                                                                    |
| ------------------------- | ------------------------------------------------------------------------------ |
| Manage Announcements      | Allow user to create and delete announcements                                  |
| Manage Properties         | Allow user to create, update, delete Properties                                |
| Manage Features           | Umbrella privilege to manage all features.                                     |
| View Analytics            | Allow user to view the Secoda analytics dashboard.                             |
| Manage Views              | Allow user to create, update, and delete any Views.                            |
| View Monitors             | Allow user to create, update, and delete any Monitors.                         |
| Manage Workspace Settings | Allow user to view and change platform-level settings, like security settings. |

**Resource Management**[**​**](https://datahubproject.io/docs/authorization/policies#entity-management)

| Privileges      | Description                                           |
| --------------- | ----------------------------------------------------- |
| Manage Teams    | Allow user to create and remove Teams.                |
| Manage Glossary | Allow user to create, edit, and remove Glossary Terms |
| Manage Tags     | Allow user to create and remove Tags.                 |

#### Common Metadata Privileges[​](https://datahubproject.io/docs/authorization/policies#common-metadata-privileges) <a href="#common-metadata-privileges" id="common-metadata-privileges"></a>

These privileges are to view & modify any resource within Secoda.

**Entity Privileges**[**​**](https://datahubproject.io/docs/authorization/policies#entity-privileges)

| Privileges                                                                                    | Description                                                                                 |
| --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| View Resource Page                                                                            | Allow user to view the resource page.                                                       |
| Edit Resource                                                                                 | Allow user to edit any information about an resource. Super user privileges for the entity. |
| Delete                                                                                        | Allow user to delete this resource.                                                         |
| Create Resource                                                                               | Allow user to create a resource if it doesn't exist.                                        |
| Activity Log                                                                                  | Allow user to use the GET Timeline API.                                                     |
| Get Entity + Relationships API[1](https://datahubproject.io/docs/authorization/policies#fn-1) | Allow user to use the GET Entity and Relationships API.                                     |
| Get Aspect/Entity Count APIs[1](https://datahubproject.io/docs/authorization/policies#fn-1)   | Allow user to use the GET Aspect/Entity Count APIs.                                         |
| View Entity[2](https://datahubproject.io/docs/authorization/policies#fn-2)                    | Allow user to view the entity in search results.                                            |
| Share Entity[2](https://datahubproject.io/docs/authorization/policies#fn-2)                   | Allow user to share an entity with another Secoda Cloud instance.                           |

**Aspect Privileges**[**​**](https://datahubproject.io/docs/authorization/policies#aspect-privileges)

| Privileges                                                                               | Description                                                       |
| ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| Edit Tags                                                                                | Allow user to add and remove tags to an asset.                    |
| Edit Glossary Terms                                                                      | Allow user to add and remove glossary terms to an asset.          |
| Edit Description                                                                         | Allow user to edit the description (documentation) of an entity.  |
| Edit Links                                                                               | Allow user to edit links associated with an entity.               |
| Edit Status                                                                              | Allow user to edit the status of an entity (soft deleted or not). |
| Edit Domain                                                                              | Allow user to edit the Domain of an entity.                       |
| Edit Data Product                                                                        | Allow user to edit the Data Product of an entity.                 |
| Edit Deprecation                                                                         | Allow user to edit the Deprecation status of an entity.           |
| Edit Incidents                                                                           | Allow user to create and remove incidents for an entity.          |
| Edit Lineage                                                                             | Allow user to add and remove lineage edges for this entity.       |
| Edit Properties                                                                          | Allow user to edit the properties for an entity.                  |
| Edit Owners                                                                              | Allow user to add and remove owners of an entity.                 |
| Get Timeseries Aspect API[1](https://datahubproject.io/docs/authorization/policies#fn-1) | Allow user to use the GET Timeseries Aspect API.                  |

#### Specific Entity-level Privileges[​](https://datahubproject.io/docs/authorization/policies#specific-entity-level-privileges) <a href="#specific-entity-level-privileges" id="specific-entity-level-privileges"></a>

These privileges are not generalizable.

**Users & Groups**[**​**](https://datahubproject.io/docs/authorization/policies#users--groups)

| Entity | Privilege                                                                                         | Description                                                                                     |
| ------ | ------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Group  | Edit Group Members                                                                                | Allow user to add and remove members to a group.                                                |
| Group  | Manage Group Notification Settings[2](https://datahubproject.io/docs/authorization/policies#fn-2) | Allow user to manage notification settings for a group.                                         |
| Group  | Manage Group Subscriptions[2](https://datahubproject.io/docs/authorization/policies#fn-2)         | Allow user to manage subscriptions for a group.                                                 |
| Group  | Edit Contact Information                                                                          | Allow user to change the contact information such as email & chat handles.                      |
| User   | Edit Contact Information                                                                          | Allow user to change the contact information such as email & chat handles.                      |
| User   | Edit User Profile                                                                                 | Allow user to change the user's profile including display name, bio, title, profile image, etc. |

**Dataset**[**​**](https://datahubproject.io/docs/authorization/policies#dataset)

| Entity       | Privilege                                                                                            | Description                                                                                                                                                                       |
| ------------ | ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Table        | View Table Usage                                                                                     | Allow user to access table usage information (includes usage statistics and queries).                                                                                             |
| Table        | View Table Profile                                                                                   | Allow user to access table profile (snapshot statistics)                                                                                                                          |
| Table        | Edit Table Column Descriptions                                                                       | Allow user to edit the column (field) descriptions associated with a table schema.                                                                                                |
| Table        | Edit Tableaset Column Tags                                                                           | Allow user to edit the column (field) tags associated with a table schema.                                                                                                        |
| Table        | Edit Table Related Resources                                                                         | Allow user to edit the column (field) glossary terms associated with a dataset schema.                                                                                            |
| Table        | Propose Dataset Column Glossary Terms[2](https://datahubproject.io/docs/authorization/policies#fn-2) | Allow user to propose column (field) glossary terms associated with a dataset schema.                                                                                             |
| Table        | Propose Dataset Column Tags[2](https://datahubproject.io/docs/authorization/policies#fn-2)           | Allow user to propose new column (field) tags associated with a dataset schema.                                                                                                   |
| Table        | Manage Dataset Column Glossary Terms[2](https://datahubproject.io/docs/authorization/policies#fn-2)  | Allow user to manage column (field) glossary term proposals associated with a dataset schema.                                                                                     |
| Table        | Propose Dataset Column Descriptions[2](https://datahubproject.io/docs/authorization/policies#fn-2)   | Allow user to propose new descriptions associated with a dataset schema.                                                                                                          |
| Table        | Manage Dataset Column Tag Proposals[2](https://datahubproject.io/docs/authorization/policies#fn-2)   | Allow user to manage column (field) tag proposals associated with a dataset schema.                                                                                               |
| Table        | Edit Assertions                                                                                      | Allow user to add and remove assertions from an entity.                                                                                                                           |
| Table        | Edit Dataset Queries                                                                                 | Allow user to edit the Queries for a Dataset.                                                                                                                                     |
| Table        | Create erModelRelationship                                                                           | Allow user to add erModelRelationship on a dataset.                                                                                                                               |
| Table        | Edit Monitors[2](https://datahubproject.io/docs/authorization/policies#fn-2)                         | Allow user to edit monitors for the entity.                                                                                                                                       |
| Table        | Edit SQL Assertion Monitors[2](https://datahubproject.io/docs/authorization/policies#fn-2)           | Allow actor to edit custom SQL assertion monitors for the entity. Note that this gives read query access to users with through the Custom SQL assertion builder. Grant with care. |
| Table        | Edit Data Contract[2](https://datahubproject.io/docs/authorization/policies#fn-2)                    | Allow actor to edit the Data Contract for an entity.                                                                                                                              |
| Table        | Manage Data Contract Proposals[2](https://datahubproject.io/docs/authorization/policies#fn-2)        | Allow actor to manage a proposal for a Data Contract                                                                                                                              |
| Tag          | Edit Tag Color                                                                                       | Allow actor to change the color of a Tag.                                                                                                                                         |
| Domain       | Manage Data Products                                                                                 | Allow actor to create, edit, and delete Data Products within a Domain                                                                                                             |
| GlossaryNode | Manage Direct Glossary Children                                                                      | Allow actor to create and delete the direct children of this entity.                                                                                                              |
| GlossaryNode | Manage All Glossary Children                                                                         | Allow actor to create and delete everything underneath this entity.                                                                                                               |

**Misc**[**​**](https://datahubproject.io/docs/authorization/policies#misc)

| Entity       | Privilege                       | Description                                                          |
| ------------ | ------------------------------- | -------------------------------------------------------------------- |
| Tag          | Edit Tag Color                  | Allow user to change the color of a Tag.                             |
| Domain       | Manage Data Products            | Allow user to create, edit, and delete Data Products within a Domain |
| GlossaryNode | Manage Direct Glossary Children | Allow user to create and delete the direct children of this entity.  |
| GlossaryNode | Manage All Glossary Children    | Allow user to create and delete everything underneath this entity.   |
