---
description: Seamlessly integrate Secoda with your Slack workspace
---

# Slack

Connecting your workspace to Slack allows you to receive notifications from Secoda regarding changes in your workspace and ask questions about your data directly from Slack. When using the Secoda integration for Slack you're agreeing to our [privacy-policy.md](../../../policies/privacy-policy.md "mention")and [terms-of-use.md](../../../policies/terms-of-use.md "mention").

You can learn more about all of the capabilities of this integration here: [slack-user-guide.md](slack-user-guide.md "mention")

## Steps for setting up Slack

1. Create a new Slack channel, multiple channels depending on your use cases (ideas [below](./#how-it-works)), or decide which existing channel(s) you'd like to use. If you'd like to use a **Private** Slack channel for these, you must type **`/invite @Secoda`** in the channel and then go to Secoda and follow the below steps
2. After this channel is created or you've decided which existing channel you'd like to use, go to **Integrations** in the Secoda App.
3. Click **New integration** and search for **Slack**.
4. Choose which **Teams** you'd like to include. We recommend choosing all so that everyone across your organization has access to the Secoda integration for Slack.
5. Click **Connect.** Note: This connection will need to be approved by your Slack admin manager.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/3af6bcb5-c935-46d2-ae16-74faba13cd6f.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Notifications Channel** = Where users receive notifications on everything that is checked off in the Notifications tab of the integration settings

**Incidents Channel** = Where users receive notifications on new monitoring incidents, and when they resolve

**Questions Channel** = Where users can ask data questions and receive Secoda AI-generated responses\

{% endhint %}

7. Within the Slack app, go into the Slack channel(s) you chose and connect it to the Secoda App. This can be done in the channel settings (upper right hand corner) by clicking **Integrations >** **Add an App.**
   1. Note: A Slack Admin needs to do this step.&#x20;

![](https://secoda-public-media-assets.s3.amazonaws.com/e2370145-6019-474a-9515-248b45ec9420.png)

## Configuring Channels

The Secoda Slack integration allows you to streamline communication with your data team and manage incidents directly from Slack. To make the most of this integration, you can configure dedicated Slack channels for different types of interactions. Here’s how to set up each type of channel.

### Questions Channel

The “Questions” channel is where data consumers can ask questions and interact directly with the data team. This channel supports bi-directional syncing with Secoda, meaning any questions asked in Slack will be automatically logged in Secoda, and responses from the data team will sync back into the Slack conversation.

• Setup: Create or select a channel for questions, such as #data-questions. Ensure Secoda is added to the channel to enable bi-directional syncing. Configure the behaviour for pushing threads to Secoda questions and how Secoda AI responds to the questions.

• Use case: Great for quick inquiries about data definitions, metrics, or troubleshooting issues.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/8b82abd3-92f1-4bad-a087-b2d00319b5a5.png" alt=""><figcaption></figcaption></figure>

### Notifications Channel

The “Notifications” channel is used to receive automated updates from Secoda, such as new data releases, system updates, or important announcements.

• Setup: Create or select a channel for notifications, such as #secoda-notifications. Configure the notification preferences in Secoda to send updates to this channel.

• Use case: Ideal for keeping your data team and other stakeholders informed about any changes or important updates in your data ecosystem.\


<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/a2f5cb49-f15f-4b7b-bccb-cf2269ad0247.png" alt=""><figcaption></figcaption></figure>

### Incidents Channel

The “Incidents” channel is dedicated to managing monitoring incidents. Like the Questions channel, it supports bi-directional syncing. This allows incident discussions initiated in Slack to be automatically tracked in Secoda, while any updates made in Secoda regarding an incident will sync back to the Slack conversation.

• Setup: Create or select a channel for incident management, such as #data-incidents. Add Secoda to the channel to enable bi-directional syncing for incidents.

• Use case: Critical for managing data or system outages and ensuring that both the incident and its resolution are well-documented and tracked in real-time.\


By setting up these channels, your team can stay in sync with data operations and ensure effective communication between data consumers, the data team, and incident management processes.

## How it works

There are many ways to use the Secoda integration for Slack. The following three scenarios can be managed in one Slack channel, or can be split into multiple different channels:

* [**Receiving workspace-level notifications in a chosen Channel**](./#slack-workspace-notifications): These can be helpful for the workspace Admins to all be notified of workspace-level changes. Admins/Editors can also [send Announcements](slack-user-guide.md#send-announcements-to-slack) to this Slack channel. Configure these in the **Notifications** tab in the integration Settings.
* [**Receiving Monitoring incident alerts**](../../../features/monitoring.md#slack-channel-for-monitoring-notifications): Get alerted about new incidents and when they've resolved to monitor data quality.
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
