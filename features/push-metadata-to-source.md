---
description: Secoda is able to push metadata back into the source for select integrations.
---

# Push Metadata to Source

For all of our integrations, Secoda pulls metadata from those sources into the UI. We've enabled **push back to source** for some of these integrations, which supports Secoda's goals to be your data stack's source of truth through bi-directional metadata syncing.

Secoda supports this feature for the following integrations:

* [**BigQuery**](https://docs.secoda.co/integrations/data-warehouses/bigquery-integration/bigquery-metadata#metadata-pushed)
* [**Snowflake**](https://docs.secoda.co/integrations/data-warehouses/snowflake-integration/snowflake-metadata#metadata-pushed)
* [**Redshift**](https://docs.secoda.co/integrations/data-warehouses/redshift-integration/redshift-metadata#metadata-pushed)

Click into the pages linked above to see which metadata is synced.

#### How to run a sync

At this time, this is a manual process to push the metadata from Secoda back into the source. Follow these steps to run the sync:

1. Go into **Integrations** and click into the supported tool that you'd like to push data to
2. Go to **Sync History** and click into the **Push** tab
3. Click **Run sync**

#### Overriding content

This feature will override any content that is currently set within the source with the new values that are coming from Secoda. If they are the same values, nothing will change.
