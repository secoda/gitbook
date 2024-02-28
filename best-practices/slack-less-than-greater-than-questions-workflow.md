---
description: Best practices for using Slack to answer user questions
---

# Slack <> Questions workflow

The Slack integration with Secoda allows users to stay in Slack to ask questions about data.

We've talked with many Secoda users and put this page together to highlight some best practices on how to implement this workflow at your organization.

### Initial questions to consider

1. Is there a centralized Slack channel that your colleagues go to when asking questions about data?
   1. If yes, consider connecting the Slack integration to this channel.
   2. If no, work with the relevant stakeholders to create this channel (or delete other channels so this knowledge is centralized) and socialize it to your organization.
2. Who normally has the most questions about data?
   1. Make sure that these users are included in the connected Slack channel.
3. Who normally has the answers about data?
   1. Make sure that these users are included in the connected Slack channel.
4. Have questions to the data team been managed elsewhere in the past? Would it make sense to bring  historical questions and requests into Secoda so that they are searchable?
   1. Check to see if we integrate with your tools for managing this under [integrations](../integrations/ "mention"), or reach out to Customer Support to add a native integration

### Set up the centralized channel

* Consider testing the functionality out in a private channel with a smaller subset of users
* Follow the steps to create the connection here [slack-connection](../integrations/productivity-tools/slack-connection/ "mention")
* Enable the AI Assistant within your workspace, which will allow it to generate responses directly in a Slack thread - steps here [Broken link](broken-reference "mention")

### Communicate what can be done

* Enable users to get the most out of the integration by providing them with documentation - Capabilities are outlined in this doc[slack-connection](../integrations/productivity-tools/slack-connection/ "mention")
* Share tips in the channel to remind users about what can be done, what questions can be asked etc. [#slack-integration-tips](../readme/secoda-as-an-admin/user-engagement-and-adoption/tips-and-tricks-to-share-with-new-users.md#slack-integration-tips "mention")

### Set rules and standards

These will be different for all organizations, but some could include:

* If the AI provides an accurate answer, make sure to check off **Answered** so that the question and answer can be pushed into Secoda so that they're searchable in the future
* If an important thread happens in a separate channel, make sure to manually push this into Secoda following[ these steps](../integrations/productivity-tools/slack-connection/#push-slack-thread-into-secoda-questions)
* Tag users/Secoda admins who might have the answer so that they can hop in the thread to Approve or Deny the AI-generated answer, as well as add additional context
* Set SLAs so that all questions are responded to and answered correctly, either by the AI or a colleague, in a certain timeline
* Designate someone on the data team to be "on-call" who monitors the Slack questions coming in, and ensures that SLAs are followed&#x20;
* If a colleague answers the question in the thread, consider adding what you've learned to the documentation in Secoda
* Consider typing out some frequently asked questions and answers into the [Questions](../features/ask-questions-in-secoda.md) section in your workspace, so that these are easily picked up by the AI within Slack
