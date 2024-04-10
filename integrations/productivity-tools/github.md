---
description: An overview of the GitHub integration with Secoda
---

# GitHub

## Getting Started with GitHub

{% hint style="info" %}
GitHub is a supplementary integration that track impact of potential changes and notifies the relevant people. Before connecting GitHub, a dbt integration must be connected first.
{% endhint %}

There are 2 steps to connect GitHub with Secoda:

1. Retrieve your dbt integration id associated with the GitHub repository
2. Connect Github to Secoda

#### Retrieve your dbt integration id

The GitHub integration uses the metadata extracted from your dbt integration. To retrieve your dbt integration id, follow these steps:

1. Navigate to your Secoda workspace
2. In the bottom left, click on the integrations tab
3. Find your dbt integration that matches to the GitHub repository you are trying to integrate
4. In the url, take the id after 'integrations' part of the url

For example, if the url is 'app.secoda.co/integrations/aa29401b-32c5-4f1f-9003-8473e90589e5/basic', your integration id would be 'aa29401b-32c5-4f1f-9003-8473e90589e5'.

#### Connect Github to Secoda

After retrieving the dbt integration id, the next step is to connect to Secoda:

1. In the Secoda App, select ‘Add Integration’ on the Integrations tab
2. Search for and select GitHub
3. Enter your dbt integration id you have retrieved
4. Click 'Connect with OAuth'
5. Follow the steps to login, if needed
6. Select the location you want to install, either personal or organization
7. Select 'Only select repositories', and use the dropdown to select the specific repository associated with the dbt integration
8. Click install

{% hint style="warning" %}
Github integration is only supported for users on app.secoda.co currently.
{% endhint %}

### After Connecting to Secoda

Once the connection is setup, Secoda will check any new pull requests opened in that repository for entities that exist within your workspace. If any deletions are pressent on the entities, a comment will be written on the pull request of the affected entities, and all immediate downstream entities. An email with the same information will be sent out to all owners of affected entities as well.
