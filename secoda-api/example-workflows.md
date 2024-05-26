---
description: See below for a few use cases for Secoda APIs.
---

# Example Workflows

Secoda's API's can be used for many workflows. Below are some customer favourites!

{% hint style="info" %}
Thinking about a workflow that you don't see here? Let's chat about it at [support@secoda.co](mailto:support@secoda.co)!&#x20;

Don't forget! You can also use [Automations](../features/automations/), [CSV Imports](../resource-and-metadata-management/import-and-export-data.md), and our [Custom Integration SDK](../integrations/custom-integrations-and-marketplace/secoda-sdk-custom-integration/) to programmatically add documentation and resources without the Secoda APIs.
{% endhint %}

## Identify Stale Dashboards

Worried about data sprawl? Use Secoda to prune your data resources!&#x20;

1. Pull all the dashboards in your workspace using a `GET` request, on the `dashboard/dashboards/` endpoint.&#x20;
2. Use the following fields to determine how often a dashboard is used.&#x20;
   * `external_usage` - The number of dashboard views in the source in the last 24 hours from time of sync.
   * `external_users` - The users who frequently access the dashboard, as reported by the source.
   * `internal_usage` - The number of views of the resource in Secoda over the last 90 days.
   * `internal_users` -  The users who frequently access the dashboard, from within Secoda.
   * `external_updated_at` - The last time the dashboard was updated in the source.
3. If the fields above are `null` or `0`, consider those resources for deprecation.

## Track Adoption

While Secoda has a robust [Analytics](../features/analytics-dashboard.md) page with many widgets, there might be unique user actions that you'd like to capture to track user adoption. Some of our customers have tracked which users answer questions most frequently, to reinforce Secoda as a hub for all data questions and documentation.&#x20;

1. Pull all the question answers in your workspace using a `GET` request on the `question/replies/` endpoint.
2. Use the `owners` field to track which users are answering questions.
3. Use the `accepted_answer` field to track which answers are chosen as the correct answer.

## Create Manual Lineage

Creating lineage for resources that aren't automatically connected can help add overall context to your workspace. See the below snippet for an example of how to create manual lineage in your workspace.&#x20;

1. Identify the IDs of the resources that the lineage should be created for using a `GET` request on the respective endpoint. For example, find a table ID using a GET request on the `table/tables/` endpoint, with a filter for the `schema` and `database` name.
2. Send a `POST` request to `lineage/manual/` using the IDs for the resources.

```json
{
    "to_entity": "42241243-4e27-4def-984a-31af25e4dbee",
    "from_entity": "907104ca-4609-4240-8e50-883c2773bec7",
    "direction": "UPSTREAM",
    "is_manual": "true"
}
```

&#x20;You only need to define one direction for lineage, as the opposite will automatically be created.

## Implement Data Contracts

There are many ways to build data contracts using the documentation created in Secoda. One example of this is using the Secoda lineage endpoints to determine if there are any downstream impacts of a table before merging any changes.&#x20;

In this workflow, use a `GET` request on `lineage/manual/` with a `from_entity` query param, set to the ID of the table you are making a change to. If there are any downstream resources, use extra caution when making a change.&#x20;

## Migrate Documentation

Moving to a new database? You don't want to lose all the documentation added to the original resources. The following workflow outlines how you can ensure you don't lose any of the documentation, even when moving to an entirely new tool.&#x20;

1. Integrate the new database with Secoda and run a sync. Do not delete the old database, just yet.&#x20;
2. Save the `integration_id` of both the old and new integration. You can find the ID in the url when navigating to the [Integration](https://app.secoda.co/integrations) page.&#x20;
3. Pull all the tables of the old database using a `GET` request to the `table/tables/` endpoint, with `integration_id` as a query param.&#x20;
4. For each table of the old database, find the ID of the matching table in the new database using the `GET` request to the `table/tables/` endpoint, with the new `integration_id`.&#x20;
5. Make a `PATCH` request with the documentation from the old table (ex. `description`, `tags`, `definition`, `pii`), and push it to the new table using the `table/tables/{table_id}/` endpoint.&#x20;
6. Repeat the process for all the columns associated with the old integration.&#x20;
7. Once all the documentation has been copied (you can validate this in the UI), you can safely delete the old integration.&#x20;

## Add New Users

While you can use [invite links](../getting-started/secoda-as-an-admin/invite-teammates/) to bring in users, you can also set up users programatically using Secoda APIs.

1. If you'd like to assign the user to user groups, locate the ID of the [Group](../user-management/groups.md) by listing all the groups in the workspace using a `GET` request to the `auth/group/` endpoint.&#x20;
2. If you'd like to assign the user to teams, locate the ID of the [Team](../user-management/teams.md) by listing all the teams in the workspace using a `GET` request to the `auth/teams/` endpoint. You can also locate the ID of the team through the URL when navigating to the Team homepage in the UI.&#x20;
3. Create a POST request to `user/` endpoint, with the following payload to create a user.
4. Repeat the process for any user you'd like to create in Secoda. Make sure the email you enter is the email they will use to sign into Secoda.

```json
{
    "emails": [
        "test@test.com"
    ],
    "role": "editor",
    "groups": [
        "26273b8b-4bbf-4fb4-a70a-935fb5baa5fd"
    ],
    "teams": [
        "6f40cfc2-4447-4df9-9d80-faaf27b6e905"
    ]
}
```
