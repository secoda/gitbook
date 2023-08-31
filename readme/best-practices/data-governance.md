---
description: This page will outline some best practices around data governance
---

# Data Governance

Data governance is a hot topic in the data space as it covers the ways to ensure that your company's data is **secure, accurate, reliable, and accessible**. There are many features and capabilities within Secoda that can help you achieve your data governance goals.&#x20;

Here are some best practices to consider to enable data governance across your organization:

#### Define roles and responsibility

When rolling out a tool like Secoda, it is important to define roles within your organization and who will be taking on which responsibilities. This will ensure that every user knows what needs to be done so that the metadata within the product is **accurate** and up to date. It will also ensure that only the relevant people are able to edit and view certain resources that may be private. Consider these questions:

* Who is a part of the initial group to enrich and implement Secoda? How are we delegating these tasks?
* Who will be the data champions who will own the data resources? How do we define ownership?&#x20;
* Which users and stakeholders will we onboard? Which Teams do we need to create, and which resources will they need access to?

Once you have a grasp on the makeup of your Teams and users, [**roles**](../../user-management/roles/) can be assigned using our RBAC approach and [**Teams**](../../user-management/teams.md) can be created. Enforce ownership of critical data so that it is kept up to date.

#### Identify critical data elements

It's important to start this initiative by identifying the data that most impacts your business. Consider these questions:

* What data is most critical to your business?
* Which reports and dashboards are relevant and up to date?
* What are questions that pop up all of the time?

Start here since they are more likely to have a larger impact on more users.&#x20;

Another way to identify critical data elements once you've integrated your data into Secoda is by using our [**Lineage feature**](../../features/data-lineage.md). Members can look at the overall lineage and see which are some key nodes that touch a lot of parts of a pipeline. Read more about this idea here: [https://www.synq.io/blog/business-critical-data](https://www.synq.io/blog/business-critical-data).

#### Enrich, enrich, enrich

Your users should feel confident using and **accessing** the right data, but we often see questions and concerns like:&#x20;

* What does this data mean?
* Where can I find data on _this subject_?&#x20;
* Who’s responsible or the subject matter expert?
* Is this the right data?
* Is it up to date?
* Is this sensitive data?

This is why enrichment is so important to Secoda, and if done well, should answer all of the questions above. Add descriptions, ownership, and tagging to make your important resources easier to locate when searching within Secoda.

{% hint style="info" %}
Consider using our [**Verified identifier**](../../resource-and-metadata-management/tags/verified-tag.md) on resources that have checked the box on each of those questions, indicating that it is ready for use by your Members. Using this system will provide your users confidence and **reliability** in using the data.

To enable **security measures**, use our [**PII Identifier feature**](../../resource-and-metadata-management/tags/auto-pii-tagging.md) to tag sensitive resources to alert Members in your workspace.
{% endhint %}

####
