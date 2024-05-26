---
description: This page will outline some best practices around data governance
---

# Data Governance

Data governance is a hot topic in the data space as it covers the ways to ensure that your company's data is **secure, accurate, reliable, and accessible**. There are many features and capabilities within Secoda that can help you achieve your data governance goals.&#x20;

Here are some best practices to consider to enable data governance across your organization:

## Define roles and responsibility

When rolling out a tool like Secoda, it is important to define roles within your organization and who will be taking on which responsibilities. This will ensure that every user knows what needs to be done so that the metadata within the product is **accurate** and up to date. It will also ensure that only the relevant people are able to edit and view certain resources that may be private. Consider these questions:

* Who is a part of the initial group to enrich and implement Secoda? How are we delegating these tasks?
* Who will be the data champions who will own the data resources? How do we define ownership?&#x20;
* Which users and stakeholders will we onboard? Which Teams do we need to create, and which resources will they need access to?

Once you have a grasp on the makeup of your Teams and users, [**roles**](../user-management/roles/) can be assigned using our RBAC approach, owners can be set, and [**Teams**](../user-management/teams.md) can be created. [Set permissions at the Team level](../user-management/teams.md#editing-member-settings) so that only the right users have access to editing the metadata in that Team. Enforce [ownership](../resource-and-metadata-management/assigning-owners.md) of critical data so that it is kept up to date.

{% hint style="info" %}
Consider creating an [Automation](../features/automations/) that assigns ownership to owner-less resources, to ensure that resources don't get lost. Use the template we provided in the UI called "Assign ownership for schema tables".
{% endhint %}

## Identify critical data elements

It's important to start this initiative by identifying the data that most impacts your business. Consider these questions:

* What data is most critical to your business?
* Which reports and dashboards are relevant and up to date?
* What are questions that pop up all of the time?

Start here since they are more likely to have a larger impact on more users.&#x20;

Another way to identify critical data elements once you've integrated your data into Secoda is by using our [**Lineage feature**](../features/data-lineage.md). Users can look at the overall lineage and see which are some key nodes that touch a lot of parts of a pipeline. They can also make note of important data resources and make a note of anything upstream of that asset, as it shouldn't also be marked as critical since it's dependent on it.&#x20;

[**Popularity**](../features/popularity.md) metadata could be another important field to look at since usage data can help us understand what's most important to the business. Read more about these ideas here: [https://www.synq.io/blog/business-critical-data](https://www.synq.io/blog/business-critical-data).

## Enrich, enrich, enrich

Your users should feel confident using and **accessing** the right data, but we often see questions and concerns like:&#x20;

* What does this data mean?
* Where can I find data on _this subject_?&#x20;
* Who’s responsible or the subject matter expert?
* Is this the right data?
* Is it up to date?
* Is this sensitive data?

This is why enrichment is so important to Secoda, and if done well, should answer all of the questions above. Add descriptions, ownership, and tagging to make your important resources easier to locate when searching within Secoda. Define **standards** for your editors to follow so they know which types of metadata needs to be included in their documentation. Some of this can be addressed by creating [templates.md](../resource-and-metadata-management/add-documentation/templates.md "mention") for documentation!

{% hint style="info" %}
Consider using our [**Verified identifier**](verifying-resources-workflow.md) on resources that have checked the box on each of those questions, indicating that it is ready for use by your Members. Using this system will provide your users confidence and **reliability** in using the data. Check out some tips on implementing a [verifying-resources-workflow.md](verifying-resources-workflow.md "mention") at your organization!



To enable **security measures**, use our [**PII Identifier feature**](../resource-and-metadata-management/tags/auto-pii-tagging.md) to tag sensitive resources to alert Members in your workspace. An  [automations](../features/automations/ "mention") can be created that automatically tags new resources with certain qualities, as PII.
{% endhint %}

## Read about how one team automated data governance with Secoda's help

{% embed url="https://www.secoda.co/customers/kaufland-e-commerce-case-study" %}

In summary, the team uses the following strategies to work towards their data governance goals:

* They organized the workspace so that each team has their own [**Collection**](../features/collections-1.md) which acts as a single source of truth for all of their documentation
* They map every table to a Collection , and ensured that every table has a defined [**owner**](../resource-and-metadata-management/assigning-owners.md)
  * Tip: Try out [**Automations**](../features/automations/) to push new tables into the right Collection, and set the owners automatically
* They rely heavily on [**Lineage**](../features/data-lineage.md) for understanding downstream impacts of their schema changes
* They use [**Announcements**](../features/announcements.md) as well as [**Slack**](../integrations/productivity-tools/slack-connection/slack-user-guide.md) to notify relevant stakeholders about changes
* They have a very defined workflow using our [**APIs**](../secoda-api.md) where documentation criteria is required by the developer in order to create new tables and push them to Secoda
