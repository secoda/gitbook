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

<figure><img src="../../../.gitbook/assets/Kapture 2024-05-08 at 14.36.40.gif" alt=""><figcaption></figcaption></figure>

This integration empowers teams to track and verify data transformations directly within the Secoda environment, ensuring transparency and accuracy in data operations. Whether you use dbt Core or dbt Cloud, Secoda facilitates a comprehensive view of your data landscape.

### Syncing metadata back to dbt

Metadata changes made in Secoda can be written back to dbt by running a metadata sync in a [github.md](../../productivity-tools/github.md "mention") integration that is linked to your code repository. Once your GitHub integration is setup, you can sync changes made in Secoda to the dbt resources directly in GitHub to keep your metadata up to date.
