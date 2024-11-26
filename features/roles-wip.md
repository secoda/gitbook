---
hidden: true
noIndex: true
---

# Roles \[WIP]

### Introduction[​](https://datahubproject.io/docs/authorization/policies#introduction) <a href="#introduction" id="introduction"></a>

Secoda provides the ability to declare fine-grained access controls through Custom Roles. Some examples of roles that can be created are:

* Table Owners should be allowed to edit documentation, but not Tags.
* Jenny, our Data Steward, should be allowed to edit Tags for any Dashboard, but no other metadata.
* John, a Data Analyst, should be allowed to edit the Related Resources for a specific Data Pipeline he is a downstream consumer of.
* The Data Platform team should be allowed to manage users and groups, view platform analytics, and manage roles.

{% hint style="info" %}
Custom Roles are only enabled for Premium and Enterprise tiers.
{% endhint %}

### What is a Custom Role?[​](https://datahubproject.io/docs/authorization/policies#what-is-a-policy) <a href="#what-is-a-policy" id="what-is-a-policy"></a>

A Custom Role consists of a set of permissions (see all permissions below) that can be applied to users. There are 2 types of Permissions within Secoda:

1. Platform Permissions
2. Resource Permissions

#### Platform Permissions[​](https://datahubproject.io/docs/authorization/policies#platform-policies) <a href="#platform-policies" id="platform-policies"></a>

**Platform** permissions determine who has platform-level access and management on Secoda. Examples of these permissions include

* Managing Users & Groups
* Viewing the Secoda Analytics
* Managing Roles&#x20;

Platform permissions consist of just permissions, e.g, "Can view Analytics". Platform permissions do not include a specific "target resource" against which the Permission applies to. Instead, they simply serve to assign specific permissions.

#### Resource Permissions[​](https://datahubproject.io/docs/authorization/policies#metadata-policies) <a href="#metadata-policies" id="metadata-policies"></a>

**Resource** permissions determine who can do what to which resources. For example,

* Who can edit Tables Documentation & Related Resources?
* Who can add Owners to a Chart?
* Who can add Tags to a Dashboard?

A Resource Permission can be broken down into 2 parts:

1. **Resources**: Which Resources that the permission applies to, e.g. "All Tables".
2. **Permissions**: What actions are being permitted by a permission, e.g. "Manage Tags".

**Resources**[**​**](https://datahubproject.io/docs/authorization/policies#resources)

Subsets of resources can be associated with the permission by leveraging [filters.md](filters.md "mention"). This uses the same capabilities that the filters in search, catalog, and many places in the application uses. Some examples of filters include:

1. Resources from a specific integration, e.g, Snowflake
2. Resources of a specific type, e.g, Tables
3. Resources that contain a specific tag
4. Resources that are marked as PII

### Managing Roles[​](https://datahubproject.io/docs/authorization/policies#managing-policies) <a href="#managing-policies" id="managing-policies"></a>

Policies can be managed on the page **Settings > Members > Roles** tab. The `Roles` tab will only be visible to those users having the `Manage Roles` privilege.

Out of the box, Secoda is deployed with a set of default Roles. The set of default roles are Viewers, Editors, and Admins.

### Permissions[​](https://datahubproject.io/docs/authorization/policies#reference) \[WIP] <a href="#reference" id="reference"></a>

Each permission can enable Create, Update, View, and Delete. Managed allows for all.

<table><thead><tr><th width="222">Privilege</th><th width="109">Admin</th><th width="108">Editor</th><th width="107">Viewer</th></tr></thead><tbody><tr><td>Users</td><td><code>Manage</code></td><td><code>View</code></td><td><code>View</code></td></tr><tr><td>Roles</td><td><code>Manage</code></td><td><code>View</code></td><td><code>View</code></td></tr><tr><td>Groups</td><td><code>Manage</code></td><td><code>View</code></td><td><code>View</code></td></tr><tr><td>API Keys</td><td><code>Manage</code></td><td><code>Manage</code></td><td><code>View</code></td></tr><tr><td>Integrations</td><td><code>Manage</code></td><td><code>View</code></td><td><code>None</code></td></tr><tr><td>Monitors</td><td><code>Manage</code></td><td><code>Manage</code></td><td><code>None</code></td></tr><tr><td>Automations</td><td><code>Manage</code></td><td><code>Manage</code></td><td><code>None</code></td></tr><tr><td>Views</td><td><code>Manage</code></td><td><code>Manage</code></td><td><code>View</code></td></tr><tr><td>Questions</td><td><code>Manage</code></td><td><code>Manage</code></td><td><code>View</code></td></tr><tr><td>Secoda AI</td><td><code>Manage</code></td><td><code>View</code></td><td><code>View</code></td></tr><tr><td>DQS</td><td><code>Manage</code></td><td><code>View</code></td><td><code>View</code></td></tr><tr><td>Tags</td><td><code>Manage</code></td><td><code>Manage</code></td><td><code>View</code></td></tr><tr><td>Properties</td><td><code>Manage</code></td><td><code>Manage</code></td><td><code>View</code></td></tr><tr><td>Teams</td><td><code>Manage</code></td><td><code>View</code></td><td><code>View</code></td></tr><tr><td>Import &#x26; Export</td><td><code>Manage</code></td><td><code>View</code></td><td><code>None</code></td></tr><tr><td>Billing</td><td><code>Manage</code></td><td><code>None</code></td><td><code>None</code></td></tr><tr><td>Workspace Settings</td><td><code>Manage</code></td><td><code>View</code></td><td><code>None</code></td></tr></tbody></table>

#### **Resources**

<table><thead><tr><th width="226">Permission</th><th width="107">Admin</th><th width="108">Editor</th><th width="116">Viewer</th></tr></thead><tbody><tr><td>Resource</td><td><code>Manage</code></td><td><code>Manage</code></td><td><code>View</code></td></tr><tr><td>Lineage</td><td><code>Manage</code></td><td><code>Manage</code></td><td><code>View</code></td></tr><tr><td>Column Profile</td><td><code>Manage</code></td><td><code>Manage</code></td><td><code>View</code></td></tr><tr><td>Preview</td><td><code>View</code></td><td><code>View</code></td><td><code>View</code></td></tr></tbody></table>

