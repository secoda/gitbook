---
description: An overview of the GitHub integration with Secoda
---

# GitHub

Getting Started with GitHub

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

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/67b3fad4-de53-4795-8932-c7195f3ff8ea.png" alt=""><figcaption></figcaption></figure>

## Sync metadata back to dbt

Run a metadata sync to update your dbt resources with the info your have changed in Secoda. When a sync is run, Secoda will update dbt metadata files that relate to Secoda resources in your workspace and create a new pull request in your repositories for you to review before merging. The following metadata will be updated from Secoda:

* descriptions
* tags
* owners
* column descriptions

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/d9fed4fc-6d6d-4ce8-ad7b-0a97645b6137.png" alt=""><figcaption></figcaption></figure>

## DBT model update preferences

This setting determines whether Secoda should automatically sync column-level metadata — such as column names, descriptions, and tags — from your tables in Secoda back to your dbt model `.yml` files in GitHub.&#x20;

When the `Sync columns to DBT models` setting is turned on:

* Secoda will **update and add** column definitions in your dbt `.yml` files to reflect what’s defined in Secoda.
* If a column does **not** already exist in the dbt model file, it will be **added** (with name and any available metadata).
* If a column **does** exist, its metadata will be updated to match what’s stored in Secoda.
* This is useful if you want Secoda to be your source of truth for column-level metadata.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/b1ab0601-dfbc-4c36-b855-ad830bb1535a.png" alt=""><figcaption></figcaption></figure>
