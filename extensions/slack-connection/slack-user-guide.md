---
description: An end-user guide to using Secoda's Slack integration
---

# Slack user guide

There are many ways to interact with Secoda through Slack. You can use it to search and ask questions about the metadata in Secoda, and get notified about changes within the workspace. This document outlines all the capabilities of the Slack integration with Secoda.

## Secoda AI bot for Slack

You can interact with Secoda's AI Assistant directly in Slack, similar to how you would in the app. The questions and answers from the AI Assistant can then be pushed into Secoda Questions in your workspace!&#x20;

### How to use Secoda's AI Assistant in Slack

1. Ensure your Secoda Admin has enabled these features. Ask the Admin which Slack channel is connected to Secoda.
2. Ask your question in the designated Data Requests Slack channel that is connected to your workspace.
   * No need to prompt with a `/` command!
   * See [below](slack-user-guide.md#asking-questions-for-personal-use) if you'd rather not post these publicly to the channel
3. If Secoda AI has the answer, it will return that answer directly in the Slack thread
   * Your teammates are also able to hop in this thread and provide their insights
4. The answer will show two options, :white\_check\_mark:**Answered** or :x:**Incorrect**, to which any user can decide if the response was accurate
5. If marked :white\_check\_mark:**Answered**, the question and the response will then be pushed into Secoda's Question section for all users to see and reference
6. If marked :x:**Incorrect**, the question will be pushed to Secoda with the response and the Admins of the workspace will be notified.&#x20;
7. Check out our best practices documentation on how to best implement this workflow in your organization: [slack-less-than-greater-than-questions-workflow.md](../../best-practices/slack-less-than-greater-than-questions-workflow.md "mention")

![](https://secoda-public-media-assets.s3.amazonaws.com/Slack%20AI_2%20\(2\).gif)

**Note**: Further ability to edit and add context to Questions pushed to Secoda can be found in the [ask-questions-in-secoda.md](../../features/ask-questions-in-secoda.md "mention") section.

### Asking questions to Secoda AI for personal use

If you have a one off question that you don't want to be posted in Secoda Questions, you can ask the AI Assistant questions in any DM or channel by prompting it by typing `/secoda-ai` followed by the question.

The AI Assistant will reply in the channel, but this response will be _Only visible to you_.

**Note:** As you can see below, it may take around 10 seconds to load a response:relaxed:

## Push Slack thread into Secoda Questions

If a Slack conversation happens in another channel that is not listed in the Settings, you can still push this information into Secoda. Simply click the three dots, Push to Secoda, set a title of the question/conversation, and Submit.

This will be helpful for when questions are asked in Slack and a user chimes in with an answer. You won't have to copy this context into Secoda, but instead Push it into Questions with a few clicks.

![](https://secoda-public-media-assets.s3.amazonaws.com/7f341f05-88a4-45b6-a915-5ce137c8567a.gif)

## Receiving DMs from Slack

If you'd like to receive notifications as direct messages as well as in a channel, you can add the Secoda App to your Slack workspace.

If you're an owner or subscriber of a resource, you'll receive notifications about documentation or schema changes to that resource. Anyone who is an owner or assignee on a question, document, or dictionary term will receive a notification when there has been an update or change related to that resource or any related resources.

1.  Hover over "... More" in Slack and click Automations

    ![](https://secoda-public-media-assets.s3.amazonaws.com/3d0b7db2-adbb-458f-a15d-0a0713fcc387.png)
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

From here, you'll be prompted to ask your question and submit information to follow up. Admins are able to customize default [question template](../../resource-and-metadata-management/add-documentation/templates.md)s.

![](https://secoda-public-media-assets.s3.amazonaws.com/Screen%20Shot%202022-04-09%20at%202.09.20%20PM.png)

You can view your asked questions by going into the Secoda app and going to the Questions tab or going to the Slack channel that has been set up to receive notifications from Secoda.

![](https://secoda-public-media-assets.s3.amazonaws.com/Screen%20Shot%202022-04-09%20at%202.09.34%20PM.png)

When this question is answered, you'll receive a notification.

![](https://secoda-public-media-assets.s3.amazonaws.com/Screen%20Shot%202022-04-09%20at%202.10.05%20PM%20\(1\).png)

To respond to incoming and new questions, head to the Secoda app, click on Questions, and you’ll see all of the questions that have been asked and answered.

## Workspace-level notifications

Your workspace Admin can configure certain notifications to be sent to a specific channel. Ask your Secoda Admin which Slack channel they've set up and make sure you've joined.

## Send Announcements to Slack

You can also use Announcements with Slack if you'd like to send adhoc announcements to your users about a resource.

1. Click into a resource
2. Click on the Announcement button in the top right corner
3. Type up your announcement
4.  In the Recipients field, search for a Slack channel that you'd like to share it to and select!

    ![](https://secoda-public-media-assets.s3.amazonaws.com/Kapture%202023-05-16%20at%2016.28.49.gif)

## Video resource

{% embed url="https://www.loom.com/share/7d292c8a50a34470b5dee861377f5660?sid=abf668f1-c53a-4973-85c7-edca5b5b90cb" %}

{% hint style="info" %}
Not using Secoda to manage your data knowledge yet? Sign up for free [here](https://app.secoda.co) 👈
{% endhint %}
