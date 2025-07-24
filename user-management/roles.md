# Roles

### Introduction[​](https://datahubproject.io/docs/authorization/policies#introduction) <a href="#introduction" id="introduction"></a>

Secoda provides the ability to declare fine-grained access controls through Custom Roles. Some examples of roles that can be created are:

* Table Owners should be allowed to edit documentation, but not Tags.
* Jenny, our Data Steward, should be allowed to edit Tags for any Dashboard, but no other metadata.
* John, a Data Analyst, should be allowed to edit the Related Resources for a specific Data Pipeline he is a downstream consumer of.
* The Data Platform team should be allowed to manage users and groups, view platform analytics, and manage roles.

{% hint style="info" %}
Custom Roles are currently in Early Access. To get early access please fill out the form [here](https://tally.so/r/3N8ENQ).
{% endhint %}

### What is a Custom Role?[​](https://datahubproject.io/docs/authorization/policies#what-is-a-policy) <a href="#what-is-a-policy" id="what-is-a-policy"></a>

Custom roles allow workspace administrators to create tailored permission sets that go beyond Secoda's default roles (Admin, Editor, Viewer, and Guest). With custom roles, you can define precise access levels for different teams and use cases within your organization.

### Understanding Custom Roles

Custom roles provide granular control over:

* Resource access (tables, dashboards, documents, etc.)
* Feature permissions (API access, monitoring, automation, etc.)
* Administrative capabilities

Unlike default roles which have predefined permission sets, custom roles let you:

* Choose specific permissions for each feature
* Set different access levels for different resource types
* Create role-based access control (RBAC) that matches your organization's needs

### Creating a Custom Role

To create a custom role:

1. Navigate to Settings > Members and permissions
2. Click on the "Roles" tab
3. Select "Create Role"
4. Provide:
   * Role name
   * Description
   * Select permissions for each feature category

#### Permission Categories

Custom roles can be configured with permissions across several categories:

* **User Management**
  * Users: Create, update, read, or delete users
  * Groups: Manage group memberships and settings
  * Roles: Create and modify roles
* **Resource Management**
  * Read: View resources and their metadata
  * Write: Edit resources and their properties
  * Manage: Full control including deletion. This includes management of properties including description, owner, tags, verified, etc.
* **Settings**
  * Workspace: Configure general workspace settings
  * Security: Manage SAML and security settings
  * API Keys: Generate and manage API access
  * Properties: Configure custom properties
  * Billing: Access billing and subscription settings
  * Import/Export: Manage data imports and exports
  * Appearance: Customize workspace appearance
* **Features**
  * AI Assistant: Configure and use Secoda AI
  * Quality Score: Manage data quality metrics
  * Questions: Create and manage Q\&A
  * Automations: Set up automated workflows
  * Monitors: Configure data monitoring
  * Views: Create and manage custom views
  * Analytics: Access usage analytics
  * Queries: View and manage queries
  * Lineage: View and edit data lineage
  * Tags: Create and manage resource tags
  * Collections: Organize resources in collections

### Best Practices

1. **Principle of Least Privilege**: Grant only the permissions necessary for each role
2. **Document Role Purposes**: Add clear descriptions to explain each role's intended use
3. **Regular Review**: Periodically audit custom roles to ensure they align with current needs

### Permissions <a href="#reference" id="reference"></a>

Out of the box, Secoda is deployed with a set of default Roles. The set of default roles are Viewers, Editors, and Admins.

{% hint style="info" %}
Manage is all permissions (Create, Update, Delete, and View)
{% endhint %}

**User Management**&#x20;

| Name   | Admin  | Editor | Viewer |
| ------ | ------ | ------ | ------ |
| Groups | Manage | View   | View   |
| Roles  | Manage | View   | View   |
| Teams  | Manage | View   | View   |
| Users  | Manage | View   | View   |

**Resource Management**

| Name      | Admin  | Editor         | Viewer |
| --------- | ------ | -------------- | ------ |
| Resources | Manage | Create, Update | View   |

**Settings**

| Name              | Admin  | Editor         | Viewer |
| ----------------- | ------ | -------------- | ------ |
| API keys          | Manage | Create, Update | None   |
| Billing           | Manage | None           | None   |
| Import and export | Manage | None           | None   |
| Workspace         | Manage | View           | None   |

**Features**

| Name               | Admin  | Editor         | Viewer       |
| ------------------ | ------ | -------------- | ------------ |
| Analytics          | Manage | View           | None         |
| Announcements      | Manage | Manage         | View         |
| Automations        | Manage | View           | None         |
| Column profile     | Manage | Manage         | View         |
| Data quality score | Manage | Create, Update | View         |
| Integrations       | Manage | View           | None         |
| Lineage            | Manage | Create, Update | View         |
| Monitors           | Manage | Create, Update | None         |
| Policies           | Manage | Manage         | View         |
| Preview            | View   | View           | View         |
| Properties         | Manage | Manage         | View         |
| Secoda AI          | Manage | View           | View         |
| Questions          | Manage | Create, Update | Create, View |
| Queries            | Manage | Create, Update | View         |
| Tags               | Manage | Create, Update | View         |
| Views              | Manage | Create, Update | View         |

