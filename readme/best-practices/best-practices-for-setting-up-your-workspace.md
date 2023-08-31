---
description: Learn about some best practices that we've seen work well!
---

# Setting up your workspace

After your integrations are setup and you have all of your data in the product, you might consider how you want the layout of your workspace to look. In this doc, we’ll outline some best practices that we’ve seen work well for our customers.

## Organize Teams

Teams is the main way to organize your organizations resources. Read more about all of the capabilities and how to set up Teams [here](../../user-management/teams.md).

### General Team

At this stage, all of your data from the connected integrations should be accessible via the General Team Catalog. General is default set to Public to all users, but if you’d like you can make it Private in the Teams Settings.

Here are some use cases for the General Team in Secoda:

* Use the General Team as a **public** space for all users in your workspace to access
  * Create a dictionary of terms, metrics and acronyms that are often used cross-functionally
  * Create internal processes and best practices documents relevant to all users
  * Create Secoda onboarding documents for first time users including how to navigate your org’s workspace
* Use the General Team as a **private** space for a subset of users to access
  * This might come in handy if you’re using Secoda as a client-facing tool and you don’t want all users to access integrations across multiple clients
  * Make General private in Team Settings and limit it only to your internal team members

### Other Teams

Begin with outlining your user base, and then create the Teams based off of that list.

1. Make a list of your initial users, and the other users you eventually plan to onboard into the product
2. Create Teams based on the teams those users are apart of. For example,
   1. Let’s say the initial power users who roll out the tool are in the same team, the Data Platform team → Create a Team named “Data Platform” and add the relevant users
   2. Let’s say your first rollout will be to editors on the Business Intelligence team → Create a Team named “Business Intelligence” as a placeholder for when they eventually are onboarded
   3. Consider creating Teams for all of your future users
3. In the Integrations settings, add the relevant Teams to the integrations that they should have access to. These will flow into the Catalogs of each Team selected.
4. Consider editing the sidebar depending on what each Team needs access to
   1. Some customers have less technical users who might only need access to a singular collection. In Teams settings, you are able to remove from their view the Catalog, Dictionary, Documents and Questions sections.

## Add content to Homepage

The Homepage is the first thing your users will see when jumping into Secoda. Enable them further by pinning important resources to the Team homepages, and consider writing up relevant notes using the Notepad. Watch some how-to videos on Homepage functionalities [here](../../features/custom-homepage.md).

## Automate documentation

We have many features that assist in the automation of your documentation and enrichment within Secoda. Check those out here: [automate-workflows.md](automate-workflows.md "mention")

## Integrate with Slack

If your organization uses Slack for internal communications, you definitely will want to set up the Slack integration with Secoda. This allows your users to ask the Slackbot questions about your data without having to leave Slack. It’ll also allow you to receive notifications regarding your workspace within Slack, depending on how you’ve configured your notifications settings.

Read more about setup, and the functionalities of the integration [here](../../integrations/productivity-tools/slack-connection/).
