---
description: Clean up your data resources with Secoda's help.
---

# Clean up your data

{% hint style="info" %}
Make sure you check the [lineage graph](../features/data-lineage.md) in Secoda before deprecating a resource in the source!
{% endhint %}

Secoda has built in tools that allows you to clean up your data resources.

End result:

* Reduced time identifying this data manually
* Improved data quality and security
* Improved productivity for analysts trying to find the right data
* Reduced costs on data storage

## Features for cleaning up your data

### [popularity.md](../features/popularity.md "mention")

* Popularity metadata is another important metric for understanding what could be deprecated.&#x20;
* Sort the Catalog by Popularity to find unused resources with minimal views or queries.

## [automations.md](../features/automations.md "mention")

* Create an Automation to automatically tag resources as Stale if they haven't been queried or edited recently.&#x20;
* Then just filter the Catalog for Stale sources to bulk deprecate them!
*

    <figure><img src="../.gitbook/assets/Screenshot 2024-04-03 at 4.51.20 PM.png" alt="" width="375"><figcaption></figcaption></figure>

{% hint style="info" %}
All of the above practices can also be done through [the Secoda API](../secoda-api.md). Reach out to support in the  [Secoda Community Slack](https://via.intercom.io/c?url=https%3A%2F%2Fjoin.slack.com%2Ft%2Fsecodacommunity%2Fshared\_invite%2Fzt-mhnu278g-FktKZmZ51SDQtlu3NRAxqg\&h=13f5aaa171821956434fc25f4c759a803f98a84f-dssmg53d\_11:24933\&l=d215b12164c764d92e3bca464c2434cae72f7a22-8270396) if you have questions about how to utilize the API for your data deprecation goals.
{% endhint %}

## Cost containment resources

* Articles:&#x20;
  * [Data Stack Cost Management Best Practices | Secoda](https://www.secoda.co/blog/managing-costs-of-the-modern-data-stack-at-scale)
  * [How To Increase the ROI of Your Data Team | Secoda](https://www.secoda.co/blog/from-cost-center-to-revenue-generator-unleashing-the-potential-of-data-teams)
* Webinar: [Mastering cost containment for modern data teams](https://www.youtube.com/watch?v=1R8y8LZRJCU)
* [snowflake-costs.md](../integrations/data-warehouses/snowflake-integration/snowflake-costs.md "mention")

