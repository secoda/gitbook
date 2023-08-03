# Syncing metadata to Snowflake

The ability to sync metadata from Secoda back to the source has been extended to Snowflake for table and column descriptions. Secoda can now be the single source of truth for Snowflake table and column descriptions with bi-directional metadata syncing.

Please ensure ensure the `SECODA` role has `INSERT` table privileges, as well as `MODIFY` schema and database. You can check what privileges the role has by running `SHOW GRANTS TO ROLE SECODA`.

#### How to run a sync

At this time, this is a manual process to push the metadata from Secoda back to Snowflake. Follow these steps to run the sync:

1. Go into **Integrations** and find Snowflake
2. Go to Sync History and click into the **Push** tab
3. Push the metadata into Snowflake

<figure><img src="../../../../.gitbook/assets/Screenshot 2023-07-24 at 2.43.51 PM.png" alt=""><figcaption></figcaption></figure>

#### What will sync?

As of now, this will sync the descriptions on tables and columns within Snowflake. It only looks at the tables that have been published and all of their columns. If a table isn't published in Secoda and you run a sync, it will not push back to the source.

#### Overriding content

This will override any description that is currently set within Snowflake with the new values that are coming from Secoda. If they are the same values, nothing will change.
