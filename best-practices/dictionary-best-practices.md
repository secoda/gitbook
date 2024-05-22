---
description: >-
  Read up on some best practices and strategies around building out a Dictionary
  within Secoda
---

# Dictionary best practices

We've put together some ideas around best practices when building out a Dictionary within Secoda. There's not one way to go about these as every organization has different requirements, but here are some ideas that have proven to work well :rocket:

## Choosing terms

If you have an **existing list of terms** and definitions hosted elsewhere...

* Use our [Import feature](../resource-and-metadata-management/import-and-export-data.md#importing-metadata-into-secoda) to automatically bulk upload these into Secoda via CSV format

If you don't have a list yet, and need to start fresh...

* It's important to initially focus on high-impact terms that are important to your users within Secoda
* Consider hosting a small group workshop with your workspace Admins, or some core editors
  * Brainstorm a list of highly-used, high-impact terms across your organization or data team
  * Think of terms that are often misused, undefined, or confusing for your stakeholders
  * Vote on the priority of each term and make plans to gather the right people in a room to develop definitions for these

## [Templates](../resource-and-metadata-management/add-documentation/templates.md)

* Utilizing the Templates feature within the UI is a great way to ensure that documentation standards are set and followed
* Admins of each Team should create dictionary templates so that editors know what kind of information is expected to be added to each term

## Organization

* Since each Team has it's own section for a dictionary, you might consider ways to organize the many terms that your organization needs to define
* Consider using the General Team dictionary as an onboarding tool&#x20;
  * Define more general terms that span across the whole organization&#x20;
  * Define company jargon and acronyms that can often get confusing for new hires
* Team-specific dictionaries
  * Define terms by Team, based on which team _owns_ those terms and therefore owns the documentation of them
* Consider [Nesting terms](../features/dictionary.md#nesting-terms) so that they are easier to navigate for your users

## Enrich dictionary terms

* When defining terms, it's often necessary to involve multiple stakeholders to reach agreement. Secoda's [verifying-resources-workflow.md](verifying-resources-workflow.md "mention") can help facilitate this process.
* Add enrichment to dictionary terms by adding them to relevant Collections, adding owners and tags, link them to related terms
  * Don't forget that you can make bulk changes to terms and use some of our other documentation tips listed here [documentation-best-practices.md](documentation-best-practices.md "mention")
* This ensures that they're even more searchable within the UI, and so users can see how terms and resources are related across the workspace

## Verification

* Consider using our [Verification tag](../resource-and-metadata-management/tags/verified-tag.md) in order to indicate that a term is ready to be used, and the definition has been approved by the data team or a list of relevant stakeholders
* The goal of this tag is to provide trust in the data for users, so that users feel confident using the term in their workflows
