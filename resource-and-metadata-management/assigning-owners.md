---
description: Assigning owners to resources
---

# Assigning Owners

## **Benefits to assigning ownership**

Assigning owners has many benefits. If your data has ownership defined, you can:

* Understand who will be affected by upstream or downstream changes to a dataset
* Understand who to talk to regarding information about the data
* Get notifications when the datasets change
* Identify abandoned data sets no one currently owns, that may need to be maintained or removed

## **How to assign owners to data in Secoda**

After navigating to a Secoda resource, Editors and Admins can assign Owners by clicking the Owners field and selecting the relevant members from the workspace. The owners field is accessible through Catalog views, or in the side panel.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/Screenshot%202023-06-09%20at%2012.08.28%20PM.png" alt=""><figcaption><p>Owners in the side panel</p></figcaption></figure>

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/Screenshot%202023-06-09%20at%2012.09.58%20PM.png" alt=""><figcaption><p>Owners in Catalog view</p></figcaption></figure>

## Automating ownership

We currently support bringing in ownership metadata for the following integrations:

* Snowflake&#x20;
* BigQuery
* Looker Studio
* PowerBI
* Redash
* Metabase
* Sigma
* Mode
* Fivetran

Try out the [propagating-metadata.md](editing-metadata/propagating-metadata.md "mention") & [bulk-editing-resources.md](editing-metadata/bulk-editing-resources.md "mention") features to bulk add owners to your resources.

## Being an owner

Owners are responsible keeping documentation on their datasets up to date. If something looks off with a dataset, or a new user is looking to get acquainted with the data, they can ask questions in the questions tab.

Owners will receive notifications through email and the Secoda app when tables, columns or documentation-related changes. If you have the Secoda Slack integration installed, you will receive notifications through Slack.

Table Owners can add helpful comments or Frequently Asked Questions about a dataset so they’ll show at the top of the documentation tab.

{% hint style="info" %}
Not using Secoda to manage your data documentation yet? Sign up for free [here](http://app.secoda.co/) 👈
{% endhint %}
