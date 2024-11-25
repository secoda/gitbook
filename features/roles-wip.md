---
hidden: true
noIndex: true
---

# Roles \[WIP]

### Custom Roles

Custom Roles are associated with [policies-wip.md](policies-wip.md "mention") to control who can do what to which resources in Secoda.&#x20;

{% hint style="info" %}
Custom Roles are only available for Premium and Enterprise tiers.&#x20;
{% endhint %}

### Default Roles

By default the Admin, Editor, and Viewer roles are predefined to control certain privileges.&#x20;

**Access & Credentials**[**​**](https://datahubproject.io/docs/authorization/policies#access--credentials)

<table><thead><tr><th>Privilege</th><th>Description</th><th width="85" data-type="checkbox">Admin</th><th width="82" data-type="checkbox">Editor</th><th width="70" data-type="checkbox">View</th></tr></thead><tbody><tr><td>Generate API Keys</td><td>Allow user to generate personal access tokens for use with Secoda APIs.</td><td>true</td><td>false</td><td>false</td></tr><tr><td>Manage Policies</td><td>Allow user to create and remove access control policies. Be careful - Users with this privilege are effectively super users.</td><td>true</td><td>false</td><td>false</td></tr><tr><td>Manage Users &#x26; Groups</td><td>Allow user to create, remove, and update users and groups on Secoda.</td><td>true</td><td>false</td><td>false</td></tr><tr><td>Manage Integrations</td><td>Allow user to manage integrations to Secoda.</td><td>true</td><td>false</td><td>false</td></tr></tbody></table>

**Product Features**[**​**](https://datahubproject.io/docs/authorization/policies#product-features)

<table><thead><tr><th width="253">Privilege</th><th width="246">Description</th><th width="87" data-type="checkbox">Admin</th><th width="81" data-type="checkbox">Editor</th><th width="92" data-type="checkbox">Viewer</th></tr></thead><tbody><tr><td>Manage Features</td><td>A catch-all for all features</td><td>true</td><td>false</td><td>false</td></tr><tr><td>Manage Properties</td><td>Allow user to create, update, delete Properties</td><td>true</td><td>true</td><td>false</td></tr><tr><td>Manage Monitors</td><td>Allow a user to create, update, delete Monitors</td><td>true</td><td>true</td><td>false</td></tr><tr><td>Manage Automations</td><td>Allow a user to create, update, delete Automations</td><td>true</td><td>true</td><td>false</td></tr><tr><td>Manage Views</td><td>Allow user to create, update, and delete any Views.</td><td>true</td><td>true</td><td>false</td></tr><tr><td>Manage Questions</td><td>Allow a user to mark question as answered.</td><td>true</td><td>false</td><td>false</td></tr><tr><td>Manage Workspace Settings</td><td>Allow user to view and change platform-level settings, like security settings.</td><td>true</td><td>false</td><td>false</td></tr><tr><td>View Analytics</td><td>Allow user to view the Secoda analytics dashboard.</td><td>true</td><td>true</td><td>false</td></tr><tr><td>View Monitors</td><td>Allow user to create, update, and delete any Monitors.</td><td>true</td><td>true</td><td>false</td></tr></tbody></table>

**Resource Management**[**​**](https://datahubproject.io/docs/authorization/policies#entity-management)

<table><thead><tr><th width="249">Privilege</th><th width="251">Description</th><th width="86" data-type="checkbox">Admin</th><th width="89" data-type="checkbox">Editor</th><th data-type="checkbox">Viewer</th></tr></thead><tbody><tr><td>Manage Teams</td><td>Allow user to create and remove Teams.</td><td>true</td><td>false</td><td>false</td></tr><tr><td>Manage Glossary</td><td>Allow user to create, edit, and remove Glossary Terms</td><td>true</td><td>true</td><td>false</td></tr><tr><td>Manage Collections</td><td>Allow user to create, edit, and remove Collections</td><td>true</td><td>true</td><td>false</td></tr><tr><td>Manage Tags</td><td>Allow user to create and remove Tags.</td><td>true</td><td>true</td><td>false</td></tr></tbody></table>

**Entity Privileges**[**​**](https://datahubproject.io/docs/authorization/policies#entity-privileges)

<table><thead><tr><th width="249">Privilege</th><th>Description</th><th width="77" data-type="checkbox">Admin</th><th width="83" data-type="checkbox">Editor</th><th width="83" data-type="checkbox">Viewer</th></tr></thead><tbody><tr><td>View Resource</td><td>Allow user to view the resource page.</td><td>true</td><td>true</td><td>true</td></tr><tr><td>Edit Resource</td><td>Allow user to edit any information about an resource. Super user privileges for the entity.</td><td>true</td><td>true</td><td>false</td></tr><tr><td>Delete Resource</td><td>Allow user to delete this resource.</td><td>true</td><td>true</td><td>false</td></tr><tr><td>Create Resource</td><td>Allow user to create a resource if it doesn't exist.</td><td>true</td><td>true</td><td>false</td></tr></tbody></table>

**Property Privileges**[**​**](https://datahubproject.io/docs/authorization/policies#aspect-privileges)

<table><thead><tr><th width="249">Privilege</th><th width="254">Description</th><th width="81" data-type="checkbox">Admin</th><th width="82" data-type="checkbox">Editor</th><th data-type="checkbox">Viewer</th></tr></thead><tbody><tr><td>Edit Tags</td><td>Allow user to add and remove tags to a resource.</td><td>true</td><td>true</td><td>false</td></tr><tr><td>Edit Collections</td><td>Allow user to add and remove collections to a resource.</td><td>true</td><td>true</td><td>false</td></tr><tr><td>Edit Description</td><td>Allow user to edit the description of a resource.</td><td>true</td><td>true</td><td>false</td></tr><tr><td>Edit Documentation</td><td>Allow user to edit documentation associated with a resource.</td><td>true</td><td>true</td><td>false</td></tr><tr><td>Edit Status</td><td>Allow user to edit the status of a resource.</td><td>true</td><td>true</td><td>false</td></tr><tr><td>Edit Teams</td><td>Allow user to edit the Teams of a resource.</td><td>true</td><td>true</td><td>false</td></tr><tr><td>Edit Custom Properties</td><td>Allow user to edit the Custom Properties of a resource.</td><td>true</td><td>true</td><td>false</td></tr><tr><td>Edit Lineage</td><td>Allow user to add and remove lineage edges for this resource.</td><td>true</td><td>true</td><td>false</td></tr><tr><td>Edit Owners</td><td>Allow user to add and remove owners of a resource.</td><td>true</td><td>true</td><td>false</td></tr><tr><td>Edit PII</td><td>Allow a user to update the PII of a resource.</td><td>true</td><td>true</td><td>false</td></tr></tbody></table>

