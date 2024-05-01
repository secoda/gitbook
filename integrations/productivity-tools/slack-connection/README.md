---
description: Seamlessly integrate Secoda with your Slack workspace
---

# Slack

Connecting your workspace to Slack allows you to receive notifications from Secoda regarding changes in your workspace and ask questions about your data directly from Slack. When using the Secoda integration for Slack you're agreeing to our [privacy-policy.md](../../../policies/privacy-policy.md "mention")and [terms-of-use.md](../../../policies/terms-of-use.md "mention").

You can learn more about all of the capabilities of this integration here: [slack-user-guide.md](slack-user-guide.md "mention")

## Steps for setting up Slack

1. Create a new Slack channel, multiple channels depending on your use cases (ideas [below](./#how-it-works)), or decide which existing channel(s) you'd like to use
   1. If you'd like to use a **Private** Slack channel for these, you must type **`/invite @Secoda`** in the channel and then go to Secoda and follow the below steps
2. After this channel is created or you've decided which existing channel you'd like to use, go to **Integrations** in the Secoda App.
3. Click **New integration** and search for **Slack**.
4. Choose which **Teams** you'd like to include.
   1. We recommend choosing all so that everyone across your organization has access to the Secoda integration for Slack.
5. Click **Connect.**
   1. Note: This connection will need to be approved by your Slack admin manager.
6. Choose the Slack channel(s) that you'd like to receive different notifications in.

![](https://secoda-public-media-assets.s3.amazonaws.com/cb828ed5-c8d2-4324-9438-264aa614ec30.png)

{% hint style="info" %}
**Notifications Channel** = Where users receive notifications on everything that is checked off in the Notifications tab of the integration settings

**Monitoring Incidents Channel** = Where users receive notifications on new monitoring incidents, and when they resolve

**Data Requests Channel** = Where users can ask data questions and receive Secoda AI-generated responses
{% endhint %}

7. In the AI Assistant tab \[If you have it enabled], configure how your AI Slack bot behaves to messages to
   * Channel Responses: How Secoda AI responds when a user messages in the connected data request channel
   *   Thread Responses: How Secoda AI responds when a user messages in a thread in the connected data request channel\


       <figure><img src="../../../.gitbook/assets/Screenshot 2024-04-30 at 6.16.52 PM.png" alt=""><figcaption><p>AI Assistant settings page<br></p></figcaption></figure>
8. Within the Slack app, go into the Slack channel(s) you chose and connect it to the Secoda App. This can be done in the channel settings (upper right hand corner) by clicking **Integrations >** **Add an App.**
   1. Note: A Slack Admin needs to do this step.&#x20;

![](https://secoda-public-media-assets.s3.amazonaws.com/e2370145-6019-474a-9515-248b45ec9420.png)

9. To set up [#secoda-ai-slackbot](slack-user-guide.md#secoda-ai-slackbot "mention"), make sure you've enabled Secoda AI Assistant [#set-up](../../../features/ai-assistant/#set-up "mention") in your workspace. You're then able to utilize the Secoda AI Assistant for Slack feature.

## How it works

There are many ways to use the Secoda integration for Slack. The following three scenarios can be managed in one Slack channel, or can be split into multiple different channels:

* [**Receiving workspace-level notifications in a chosen Channel**](./#slack-workspace-notifications): These can be helpful for the workspace Admins to all be notified of workspace-level changes. Admins/Editors can also [send Announcements](slack-user-guide.md#send-announcements-to-slack) to this Slack channel. Configure these in the **Notifications** tab in the integration Settings.
* [**Receiving Monitoring incident alerts**](../../../features/monitoring/#slack-channel-for-monitoring-notifications): Get alerted about new incidents and when they've resolved to monitor data quality.
* [**Managing data-related questions**](../../../best-practices/slack-less-than-greater-than-questions-workflow.md): Set up a workflow in Slack for managing user questions about data.

You can also use the Secoda integration for Slack for personal direct message notifications, and searching Secoda privately.

* [**Receive personally relevant notifications via DM**](slack-user-guide.md#receiving-dms-from-slack): After configuring your preferences in Settings and adding the Slack app, you can get personal notifications via DM.
* [**Searching**](slack-user-guide.md#searching-from-slack) **and**[ **asking questions privately**](slack-user-guide.md#asking-questions-to-secoda-ai-for-personal-use): Use the Slack command `/secoda` anywhere in Slack to search Secoda in a private way.

## Benefits to **Connecting Secoda to Slack** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

1. **Stay updated**: By connecting Slack to Secoda, you can receive notifications about changes to your data or data documentation directly in Slack. This allows you to stay up-to-date and informed about what's happening with your data, without having to constantly check Secoda or other data management tools.
2. **Collaboration**: Connecting Slack to Secoda allows users to ask and answer questions about your data directly from Slack. This can facilitate collaboration and help ensure that everyone has access to the information they need to make informed decisions.
3. **Convenience**: By integrating Slack and Secoda, you can access data-related information and communicate with team members directly from the Slack platform. This can save time and reduce the need to switch between different tools and applications.
4. **Improved productivity**: By streamlining communication and access to data-related information, connecting Slack to Secoda can help improve productivity and reduce the risk of errors or misunderstandings.

Overall, connecting Slack to Secoda can help your team stay updated, collaborate more effectively, and work more efficiently.

## Troubleshooting

If you encounter issues with the Slack integration, don't hesitate to reach out to our support team at [support@secoda.co](mailto:support@secoda.co) for assistance.



{% hint style="info" %}
Not using Secoda to manage your data knowledge yet? Sign up for free [here](https://app.secoda.co) 👈
{% endhint %}
