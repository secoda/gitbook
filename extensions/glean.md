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

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/1a67e582-f13d-49cf-a23c-26a9165138fa.png" alt=""><figcaption></figcaption></figure>

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

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/5b122d88-d5b2-4e77-a01a-1cfa60ce7b06.png" alt=""><figcaption></figcaption></figure>

Pushes to Glean can also be run on a schedule automatically by providing a [cron expression](https://crontab.guru/) in the **Schedule** tab:

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/ec263987-092c-44a4-8c2b-f73f4a7e4b66.png" alt=""><figcaption></figcaption></figure>

For a manual refresh of Glean's index, click on **Run sync** and then **Push metadata** at the top right:

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/10a7216d-8c00-4966-99b2-199e61dade50.png" alt=""><figcaption></figcaption></figure>

After Secoda resources are indexed in Glean, the metadata and resource itself will begin appearing in search results. The results are hyperlinked to the resource in Secoda.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/e3868158-0189-47be-9968-9ec01cd2a498.png" alt=""><figcaption></figcaption></figure>

### Important Notes

* Although the pushes from Secoda usually take no more than a few minutes, Glean also takes time to index the entities which can take up to a few hours for large workspaces.
* You won't be able to see Secoda entities in Glean's search without having the `secoda` datasource [enabled](https://glean.redoc.ly/docs/indexing_api/indexing_api_getting_started/#enable-search-results-for-the-datasource)
* Make sure that the users are indexed into the database to enable searching within Glean. More details to do so can be found [here](https://developers.glean.com/api-info/indexing/documents/permissions#scenario-2).&#x20;
