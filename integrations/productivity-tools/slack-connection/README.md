---
description: Seamlessly integrate Secoda with your Slack workspace
---

# Slack Integration

Connecting your workspace to Slack allows you to receive notifications from Secoda regarding changes in your workspace and ask questions about your data directly from Slack.

## Benefits to **Connecting Secoda to Slack** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

1. **Stay updated**: By connecting Slack to Secoda, you can receive notifications about changes to your data or data documentation directly in Slack. This allows you to stay up-to-date and informed about what's happening with your data, without having to constantly check Secoda or other data management tools.
2. **Collaboration**: Connecting Slack to Secoda allows users to ask and answer questions about your data directly from Slack. This can facilitate collaboration and help ensure that everyone has access to the information they need to make informed decisions.
3. **Convenience**: By integrating Slack and Secoda, you can access data-related information and communicate with team members directly from the Slack platform. This can save time and reduce the need to switch between different tools and applications.
4. **Improved productivity**: By streamlining communication and access to data-related information, connecting Slack to Secoda can help improve productivity and reduce the risk of errors or misunderstandings.

Overall, connecting Slack to Secoda can help your team stay updated, collaborate more effectively, and work more efficiently.

## How to Set Up

1. We recommend that you create a separate channel for Secoda purposes (i.e. #secoda-notifications), since you'll also receive notifications if there are things like schema changes or documentation edits there.
2. After this channel is created or you've decided which existing channel you'd like to use, go to **Integrations** in the Secoda App.
3. Click **New integration** and select **Slack**.
4. Choose which **Associated teams** you'd like to add; we recommend General so that everyone across your data org has access to the Slack integration.
5. Click **Connect** and choose the Slack channel that you'd like to receive [#slack-notifications](./#slack-notifications "mention") in.
6. Within the Slack app, go into the Slack channel you chose and connect it to the Secoda App. This can be done in the channel settings (upper right hand corner) by clicking **Integrations >** **Add an App.** _Note: you need to be a Slack Admin to do this._

![](https://raw.githubusercontent.com/secoda/gitbook/master/.gitbook/assets/Screenshot%202023-06-13%20at%202.28.52%20PM.png)

7. To set up the **Slack : AI connection**, go into Channels and choose a channel that you'd like to use for the AI Data Requests functionality. This channel can be the same as the Notifications channel, or a new / different channel.

![](https://raw.githubusercontent.com/secoda/gitbook/master/.gitbook/assets/Screenshot%202023-06-13%20at%2012.01.31%20PM.png)

{% hint style="info" %}
**Notifications Channel** = Where you'll receive notifications on everything that is checked off in the Notifications tab

**Data Requests Channel** = Where users can ask data questions and receive Secoda AI-generated responses
{% endhint %}

## Receiving DMs from Slack

If you'd like to receive notifications as direct messages as well as in a channel, you can add the Secoda App to your Slack workspace.

![](https://secoda-public-media-assets.s3.amazonaws.com/Screenshot%202023-05-18%20at%2012.24.58%20PM.png)</figcaption></figure>

## Secoda AI : Slack

The AI Assistant can now generate answers to your questions directly in Slack, then push these questions/answers into the Questions section of your workspace! Read more about it here [slack-ai-assistant.md](slack-ai-assistant.md "mention").

## Searching from Slack

To search Secoda from Slack, type `/secoda` into any channel or DM, followed by your search term. Once the results come up, you can open them to the page that you're looking for.

**Note**: Everyone in your Slack workspace can search Secoda, regardless of whether they have a Secoda account or not.

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

## Slack Notifications

You can receive updates from Secoda in a Slack channel of your choice. If you're an admin, you'll receive notifications about documentation or schema changes. Anyone who is an owner or assignee on a question, document, or dictionary term will receive a notification when there has been an update or change related to that resource or any related resources.

You can edit your Slack Notification preferences in the **Notifications** tab in the Slack Integration Settings, as well as in Account Settings.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/Screenshot%202023-06-12%20at%204.55.37%20PM.png" alt=""><figcaption></figcaption></figure>

## Send Announcements to Slack

You can also use Announcements with Slack if you'd like to send adhoc announcements to your users about a resource.

1. Click into a resource
2. Click on the Announcement button in the top right corner
3. Type up your announcement
4.  In the Recipients field, search for a Slack channel that you'd like to share it to and select!

    <figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/Kapture%202023-05-16%20at%2016.28.49.gif" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Not using Secoda to manage your data knowledge yet? Sign up for free [here](https://app.secoda.co) 👈
{% endhint %}
