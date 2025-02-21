---
description: An overview of the GitHub integration with Secoda
---

# GitHub

## Getting Started with GitHub

{% hint style="info" %}
GitHub is a supplementary integration that track impact of potential changes and notifies the relevant people. Before connecting GitHub, **ensure you have a dbt integration** already set up in Secoda.
{% endhint %}

### Connect Github to Secoda

1. In the Secoda App, select ‘Add Integration’ on the Integrations tab.
2. Search for and select GitHub.
3. Click 'Connect with OAuth' and follow the login steps, if needed.
4. Select the location you want to install, either personal or organization.
5. Select 'Only select repositories', and use the dropdown to select the specific repository associated with the dbt integration.
6. Click install.

## After Connecting to Secoda

Once the connection is setup, Secoda will check any new pull requests opened in that repository for entities that exist within your workspace. If any deletions are present on the entities, a comment will be written on the pull request of the affected entities, and all immediate downstream entities. An email with the same information will be sent out to all owners of affected entities as well.

## Sync metadata back to dbt

Run a metadata sync to update your dbt resources with the info your have changed in Secoda. When a sync is run, Secoda will update dbt metadata files that relate to Secoda resources in your workspace and create a new pull request in your repositories for you to review before merging. The following metadata will be updated from Secoda:

* descriptions
* tags
* owners
* column descriptions

