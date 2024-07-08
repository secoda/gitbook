---
description: An overview of the GitHub integration with Secoda
---

# GitHub

## Getting Started with GitHub

{% hint style="info" %}
GitHub is a supplementary integration that track impact of potential changes and notifies the relevant people. Before connecting GitHub, **ensure you have a dbt integration** already set up in Secoda.
{% endhint %}

There are 2 steps to connect GitHub with Secoda:

1. Retrieve your dbt integration id associated with the GitHub repository
2. Connect Github to Secoda

### Retrieve your dbt Integration ID

The GitHub integration uses the metadata extracted from your dbt integration. To retrieve your dbt integration id, follow these steps:

1. Navigate to your Secoda workspace.
2. Click on the 'Integrations' tab in the bottom left corner.
3. Find your dbt integration that matches to the GitHub repository you are trying to integrate.
4. Extract the ID from the URL. For example, in 'app.secoda.co/integrations/aa29401b-32c5-4f1f-9003-8473e90589e5/basic', the integration ID would be 'aa29401b-32c5-4f1f-9003-8473e90589e5'.

### Connect Github to Secoda

After retrieving the dbt integration id, the next step is to connect to Secoda:

1. In the Secoda App, select ‘Add Integration’ on the Integrations tab.
2. Search for and select GitHub.
3. Enter the retrieved dbt integration ID.
4. Click 'Connect with OAuth' and follow the login steps, if needed.
5. Select the location you want to install, either personal or organization.
6. Select 'Only select repositories', and use the dropdown to select the specific repository associated with the dbt integration.
7. Click install.

{% hint style="warning" %}
Github integration is currently only supported for users on app.secoda.co.
{% endhint %}

## After Connecting to Secoda

Once the connection is setup, Secoda will check any new pull requests opened in that repository for entities that exist within your workspace. If any deletions are present on the entities, a comment will be written on the pull request of the affected entities, and all immediate downstream entities. An email with the same information will be sent out to all owners of affected entities as well.

## Sync metadata back to dbt

Run a metadata sync to update your dbt resources with the info your have changed in Secoda. When a sync is run, Secoda will update dbt metadata files that relate to Secoda resources in your workspace and create a new pull request in your repositories for you to review before merging. The following metadata will be updated from Secoda:

* descriptions
* tags
* owners
* column descriptions

