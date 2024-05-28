---
description: >-
  After you've connected your data and metadata to Secoda, you can start adding
  documentation and editing properties to your data to enrich it for your users.
---

# Editing Properties

## Benefits to adding enrichment

1. Improved transparency: Helps to make data more transparent and understandable, making it easier for others to use and trust the data.
2. Enhanced data governance: Helps establish clear roles and responsibilities for data management and ensure that data is being used appropriately.
3. Improved collaboration: Facilitates collaboration by making it easier for team members to understand and use data assets.
4. Enhanced data security: Helps organizations identify and protect sensitive data and ensure that it is only accessed by authorized personnel.

## How to add context to your data

Secoda pulls the descriptions of tables, dashboards and columns that are available in the central source that you've connected. For example, if you integrate your YAML documentation from dbt, Secoda will automatically populate your column and table descriptions to match the YAML documentation.

There are many ways to add additional context your data in Secoda. Here are some options to get you started:

### Automating documentation

Learn about the many ways to automate property management [documentation-best-practices.md](../../best-practices/documentation-best-practices.md "mention")

### Manually add enrichment

* Search for the dataset or click into the Catalog to find the data that you'd like to document
  * After you've selected the dataset you'd like to document, you'll be directed to the dataset overview page, which shows you the resources currently associated with that data set.
  * You can add a description directly to the dataset by clicking underneath the name of the dataset and typing.
  * You can click the **Documents** tab and then begin adding additional documentation there. Read more about [Documents](../../features/documents/)[.](../../features/documents/)

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/Kapture%202023-05-15%20at%2014.31.09.gif" alt=""><figcaption></figcaption></figure>

* Add [tags](../tags/) such as PII, verified and custom tags to annotate the category and status of the data asset
* [Link resources](../relating-resources.md) to create relationships between them
* [Add ownership](../assigning-owners.md) details so that users know who to ask follow up questions about a dataset
