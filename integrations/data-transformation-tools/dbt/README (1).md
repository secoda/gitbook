---
description: An overview of the dbt integrations with Secoda
---

# dbt

Secoda integrates seamlessly with both [.](./ "mention") and [dbt-core](../dbt-core/ "mention"), enhancing your ability to manage and visualize data transformations and dependencies within your workspace. This guide details the integration process, the display of dbt metadata in Secoda, and how to utilize dbt features effectively.

You can learn more about the integration setup by clicking into the linked documents.

{% hint style="info" %}
dbt is a secondary integration that adds additional metadata on to your data warehouse or relational database tables. Before connecting dbt make sure to connect a data warehouse or relational database first. These include Snowflake, BigQuery, Postgres, Redshift, etc.
{% endhint %}

## **How dbt metadata appears in Secoda**&#x20;

Once the integration is established:

* If connected, Jobs will appear in the Catalog which you can click into to see Test results and additional metadata for those Tests.
* Data warehouse or relational database tables associated with dbt will display a dbt icon next to their titles.
* A 'Tests' tab will appear for resources where dbt Tests have been run.
* You can view dbt metadata overlaid on the lineage graphs to understand dependencies and transformations better.
* Within the lineage tab, lineage nodes will feature a checkmark icon. Clicking on these icons reveals which dbt Tests have been run and their statuses.
* See the video below of what a correctly functioning integration should look like:

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/39ce3633-8550-47f7-a1e0-8861c29c21ce.gif" alt=""><figcaption></figcaption></figure>

This integration empowers teams to track and verify data transformations directly within the Secoda environment, ensuring transparency and accuracy in data operations. Whether you use dbt Core or dbt Cloud, Secoda facilitates a comprehensive view of your data landscape.

## Syncing metadata back to dbt

You can seamlessly sync metadata updates from Secoda directly back to your dbt models. This streamlines workflows and enhances data governance by ensuring that your dbt models stay synced with the latest metadata in Secoda.&#x20;

Here's how you can set it up:&#x20;

1. **Set up a GitHub Integration:** Connect your [github.md](../../productivity-tools/github.md "mention") account to enable syncing between Secoda and your code repository.&#x20;
2. **Initiate a Metadata Push:** Trigger a metadata push via the GitHub sync history tab within Secoda. This process is straightforward and integrates directly with your workflow.&#x20;
3. **Automatic Pull Request Generation:** Once a metadata push is initiated, a Pull Request is automatically created in GitHub. This PR includes updates for column and table descriptions, owner details, and tags, ensuring that your dbt models are always up-to-date.&#x20;

**Benefits:**&#x20;

* Keeps your dbt models consistently updated with the latest metadata from Secoda.&#x20;
* Enhances collaboration by ensuring all team members work with the most current data definitions.&#x20;
* Reduces manual errors by automating the sync process.
