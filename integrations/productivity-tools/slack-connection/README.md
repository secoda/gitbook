---
description: Seamlessly integrate Secoda with your Slack workspace
---

# Slack

Connecting your workspace to Slack allows you to receive notifications from Secoda regarding changes in your workspace and ask questions about your data directly from Slack. When using the Slack Integration you're agreeing to our [privacy-policy.md](../../../policies/privacy-policy.md "mention")and [terms-of-use.md](../../../policies/terms-of-use.md "mention").

## Benefits to **Connecting Secoda to Slack** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

1. **Stay updated**: By connecting Slack to Secoda, you can receive notifications about changes to your data or data documentation directly in Slack. This allows you to stay up-to-date and informed about what's happening with your data, without having to constantly check Secoda or other data management tools.
2. **Collaboration**: Connecting Slack to Secoda allows users to ask and answer questions about your data directly from Slack. This can facilitate collaboration and help ensure that everyone has access to the information they need to make informed decisions.
3. **Convenience**: By integrating Slack and Secoda, you can access data-related information and communicate with team members directly from the Slack platform. This can save time and reduce the need to switch between different tools and applications.
4. **Improved productivity**: By streamlining communication and access to data-related information, connecting Slack to Secoda can help improve productivity and reduce the risk of errors or misunderstandings.

Overall, connecting Slack to Secoda can help your team stay updated, collaborate more effectively, and work more efficiently.

## How it works

There are many ways to use the Slack integration. The following three scenarios can be managed in one Slack channel, or can be split into multiple different channels:

* [**Receiving workspace-level notifications in a chosen Channel**](./#slack-workspace-notifications): These can be helpful for the workspace Admins to all be notified of workspace-level changes. Admins/Editors can also [send Announcements](./#send-announcements-to-slack) to this Slack channel.
* [**Receiving Monitoring incident alerts**](../../../features/monitoring.md#slack-channel-for-monitoring-notifications): Get alerted about new incidents and when they've resolved to monitor data quality.
* [**Managing data-related questions**](./#secoda-ai-slack): Check out our doc on the [slack-less-than-greater-than-questions-workflow.md](../../../best-practices/slack-less-than-greater-than-questions-workflow.md "mention") for best practices when implementing a workflow for managing user questions.

You can also use the Slack integration for personal direct message notifications, and searching Secoda privately.

* [**Receive personally relevant notifications via DM**](./#receiving-dms-from-slack): After configuring your preferences in Settings and adding the Slack app, you can get personal notifications via DM.
* [**Searching**](./#searching-from-slack) **and** [**asking questions privately**](./#ask-questions-from-slack): Use the Slack command `/secoda` anywhere in Slack to search Secoda in a private way.

## Steps for setting up Slack

1. Create a new Slack channel, multiple channels depending on your use cases (ideas [above](./#how-it-works)), or decide which existing channel(s) you'd like to use&#x20;
   1. If you'd like to use a **Private** Slack channel for these, you must type **`/invite @Secoda`** in the channel and then go to Secoda and follow the below steps
2. After this channel is created or you've decided which existing channel you'd like to use, go to **Integrations** in the Secoda App.
3. Click **New integration** and search for **Slack**.
4. Choose which **Teams** you'd like to include.
   1. We recommend choosing all so that everyone across your organization has access to the Slack integration.
5. Click **Connect.**
   1. Note: This connection will need to be approved by your Slack admin manager.
6. Choose the Slack channel(s) that you'd like to receive different notifications in.&#x20;

<figure><img src="../../../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Notifications Channel** = Where users receive notifications on everything that is checked off in the Notifications tab of the Slack integration settings

**Monitoring Incidents Channel** = Where users receive notifications on new monitoring incidents, and when they resolve

**Data Requests Channel** = Where users can ask data questions and receive Secoda AI-generated responses
{% endhint %}

7. Within the Slack app, go into the Slack channel(s) you chose and connect it to the Secoda App. This can be done in the channel settings (upper right hand corner) by clicking **Integrations >** **Add an App.**
   1. Note: A Slack Admin needs to do this step.

![](https://secoda-public-media-assets.s3.amazonaws.com/e2370145-6019-474a-9515-248b45ec9420.png)

## Workspace Notifications

Admins can set the workspace-level updates from Secoda to go to a Slack channel of their choice.&#x20;

Admins can edit the Slack Notification preferences in the **Notifications** tab in the Slack Integration Settings.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/Screenshot%202023-06-12%20at%204.55.37%20PM.png" alt=""><figcaption></figcaption></figure>

## Secoda AI : Slack

The AI Assistant can generate answers to your questions directly in Slack, then push these questions/answers into the Questions section of your workspace! Read more about it here [slack-ai-assistant.md](slack-ai-assistant.md "mention").

## Push Slack thread into Secoda Questions

If a Slack conversation happens in another channel that is not listed in the Settings, you can still push this information into Secoda. Simply click the three dots, Push to Secoda, set a title of the question/conversation, and Submit.

This will be helpful for when questions are asked in Slack and a user chimes in with an answer. You won't have to copy this context into Secoda, but instead Push it into Questions with a few clicks.

<figure><img src="../../../.gitbook/assets/Kapture 2023-12-18 at 10.28.21.gif" alt=""><figcaption></figcaption></figure>

## Receiving DMs from Slack

If you'd like to receive notifications as direct messages as well as in a channel, you can add the Secoda App to your Slack workspace.

If you're an owner or subscriber of a resource, you'll receive notifications about documentation or schema changes to that resource. Anyone who is an owner or assignee on a question, document, or dictionary term will receive a notification when there has been an update or change related to that resource or any related resources.

1.  Hover over "... More" in Slack and click Automations&#x20;

    <figure><img src="../../../.gitbook/assets/Screenshot 2023-11-16 at 11.09.21 AM.png" alt="" width="375"><figcaption></figcaption></figure>
2. Click into Apps and Search for Secoda
3. Add Secoda, and see your personal Notifications appear via DM

![](https://secoda-public-media-assets.s3.amazonaws.com/Screenshot%202023-05-18%20at%2012.24.58%20PM.png)

## Searching from Slack

To search Secoda from Slack, type `/secoda` into any channel or DM, followed by your search term. Once the results come up, you can open them to the page that you're looking for.

{% hint style="info" %}
Note: Everyone in your Slack workspace can search Secoda, regardless of whether they have a Secoda account or not.
{% endhint %}

![](https://secoda-public-media-assets.s3.amazonaws.com/askslack%20\(1\)%20\(1\)%20\(1\).gif)

## Ask Questions from Slack

You can ask Questions using the Slack command: `/ask` followed by a question.

![](https://secoda-public-media-assets.s3.amazonaws.com/Screen%20Shot%202022-04-09%20at%202.08.29%20PM%20\(1\)%20\(1\)%20\(1\)%20\(1\)%20\(1\)%20\(1\)%20\(1\).png)

From here, you'll be prompted to ask your question and submit information to follow up. Admins are able to customize default [question template](../../../features/ask-questions-in-secoda/templates.md)s.

![](https://secoda-public-media-assets.s3.amazonaws.com/Screen%20Shot%202022-04-09%20at%202.09.20%20PM.png)

You can view your asked questions by going into the Secoda app and going to the Questions tab or going to the Slack channel that has been set up to receive notifications from Secoda.

![](https://secoda-public-media-assets.s3.amazonaws.com/Screen%20Shot%202022-04-09%20at%202.09.34%20PM.png)

When this question is answered, you'll receive a notification.

![](https://secoda-public-media-assets.s3.amazonaws.com/Screen%20Shot%202022-04-09%20at%202.10.05%20PM%20\(1\).png)

To respond to incoming and new questions, head to the Secoda app, click on Questions, and you’ll see all of the questions that have been asked and answered.

## Send Announcements to Slack

You can also use Announcements with Slack if you'd like to send adhoc announcements to your users about a resource.

1. Click into a resource
2. Click on the Announcement button in the top right corner
3. Type up your announcement
4.  In the Recipients field, search for a Slack channel that you'd like to share it to and select!

    <figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/Kapture%202023-05-16%20at%2016.28.49.gif" alt=""><figcaption></figcaption></figure>

## Video resource

{% embed url="https://www.loom.com/share/7d292c8a50a34470b5dee861377f5660?sid=abf668f1-c53a-4973-85c7-edca5b5b90cb" %}

{% hint style="info" %}
Not using Secoda to manage your data knowledge yet? Sign up for free [here](https://app.secoda.co) 👈
{% endhint %}
