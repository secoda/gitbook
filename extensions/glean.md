---
description: An overview of the Glean extension with Secoda
---

# Glean

{% hint style="info" %}
Glean is a supplementary integration that currently pushes Secoda resources on your workspace (e.g. documents, tables, glossaries...) into Glean's search index.
{% endhint %}

### What you'll need

From Glean, you'll need two pieces of information:

1. Your Glean instance name
2. Your Glean indexing token

### Creating an indexing token

**If you have a token already, this can be skipped.**&#x20;

Glean provides step by step [instructions](https://developers.glean.com/indexing/authentication/managing-tokens) on how to create a token; however, please ensure that `secoda` is input into the `Scopes` field as a datasource. The rest of the config is discretional.

<figure><img src="../.gitbook/assets/image (137).png" alt=""><figcaption></figcaption></figure>

### Connecting Glean to Secoda

1. On the extension connection page, fill out the **Instance** field with your Glean's instance name, and the **API token** field with your Glean API token.&#x20;
2. Click **Submit** afterwards.&#x20;
3. Since this extension only pushes from Secoda, the **Import** and **Sync** pages which come after can be disregarded.

By default, **all** **entities** with these entity types have their metadata pushed to Glean:

* Documents
* Questions
* Glossary terms
* Columns
* Tables
* Schemas
* Databases
* Charts
* Dashboards

However, it's possible to **include** or **exclude** which entities get pushed using filter rules. For example, here's a simple include rule that ensures only documents get pushed to Glean:

<figure><img src="../.gitbook/assets/image (130).png" alt=""><figcaption></figcaption></figure>

Pushes to Glean can also be run on a schedule automatically by providing a [cron expression](https://crontab.guru/) in the **Schedule** tab:

<figure><img src="../.gitbook/assets/image (136).png" alt=""><figcaption></figcaption></figure>

For a manual refresh of Glean's index, click on **Run sync** and then **Push metadata** at the top right:

<figure><img src="../.gitbook/assets/image (134).png" alt=""><figcaption></figcaption></figure>

After Secoda resources are indexed in Glean, the metadata and resource itself will begin appearing in search results. The results are hyperlinked to the resource in Secoda.

<figure><img src="../.gitbook/assets/image (135).png" alt=""><figcaption></figcaption></figure>

### Important Notes

* Although the pushes from Secoda usually take no more than a few minutes, Glean also takes time to index the entities which can take up to a few hours for large workspaces.
* You won't be able to see Secoda entities in Glean's search without having the `secoda` datasource [enabled](https://glean.redoc.ly/docs/indexing_api/indexing_api_getting_started/#enable-search-results-for-the-datasource)
