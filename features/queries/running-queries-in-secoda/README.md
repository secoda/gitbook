---
description: >-
  Editors can embed live queries into table documentation, dictionary terms,
  docs, questions and collections.
---

# Running Queries

By using the /query command, editors can embed live queries into table documentation, dictionary terms, docs, questions and collections. This allows users to preview the data directly in Secoda.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/3d7f82a1-97ac-4920-9df2-433ac4b87630.png" alt=""><figcaption></figcaption></figure>

## Turn off Query capabilities

If you'd like to turn off the ability to preview this data within Secoda, you can do so in the Integration settings. You can do this at the role level so that only specific workspace members have access to this feature. Go to the Integration > Permissions > Check off which roles/groups > Submit.

{% hint style="info" %}
**NOTE:** By default, editors do not have the permissions enabled for running queries on integrations. You can enable these permissions by going to the permissions tab in the integrations setting page.&#x20;
{% endhint %}

## Steps to running queries

1. Add a query block using the /query command
2. Select a "source" from the top left of the query block
   1. Ensure that the source has been given the correct permissions
3. Write your query and press the :arrow\_forward: button on the right hand side
4. Sort the query by clicking on the column names, and share it with other users

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/cc74459b-9c48-4e98-b34d-20cb563bf346.gif" alt=""><figcaption></figcaption></figure>

## Scheduling queries

&#x20;If you'd like to write queries that run on a specific schedule, you can create [metrics.md](../../metrics.md "mention") and adjust the refresh rate to your preferred configuration. Metrics can be embedded into the documentation section of resources, dictionary terms, and documents. This can ensure that viewers who are looking at your query results are seeing up to date results that they can trust while also allowing you to manage queries from one location.&#x20;

## Sharing queries with viewers

These queries are useful for showing viewers how to use queries or if editors want to share / document queries for viewers. As a viewer, I am only able to execute the query if I have access to view the data from that integration (this will be based on which Teams they are apart of).

As a viewer, If I don't have integration permission, I will only be able to view the result of the query and download a CSV with the results that have been shared with me.

{% hint style="info" %}
Not using Secoda to manage your data documentation yet? Sign up for free [here](http://app.secoda.co/) 👈
{% endhint %}
