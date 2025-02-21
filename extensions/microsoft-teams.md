---
description: Seamlessly integrate Secoda with your Microsoft Teams
---

# Microsoft Teams

## Getting Started with Microsoft Teams

Connecting your workspace to Microsoft Teams allows you to receive notifications from Secoda regarding changes in your workspace.

There are three steps to get started with Microsoft Teams

1. Create a channel for Secoda notifications
2. Create incoming webhook for channel
3. Connect with Secoda and update notification settings

## Create a channel for Secoda notifications

Create a channel for Secoda notifications. This can be done by going to your Team -> Manage Team -> Channels -> Add Channel. Name your channel, e.g, secoda-notifications.

## Create incoming webhook for the channel

1. Go to your channel -> Manage Channel -> Connectors -> Edit

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/5743fcb0-e423-4957-b533-424df150c28b.png" alt=""><figcaption></figcaption></figure>

2. Search and select **Incoming Webhook**

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/f854f482-dc8f-467f-8ff0-8c577b3c3152.png" alt=""><figcaption></figcaption></figure>

3. Name your incoming webhook **Secoda,** and add Secoda icon, you can download the following image

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/35b53a2c-98ab-4d3a-9e6d-7765caa2285f.png" alt="" width="188"><figcaption></figcaption></figure>

4. Copy the URL in the modal and select **Done.**

You can also follow the [guide by Microsoft on how to create an Incoming Webhook](https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook).

## Connect with Secoda and update notification settings

1. Use the Incoming Webhook URL in the previous step in the Microsoft Teams connection form.
2. Test connection. Secoda will send a test message to see if the connection was made.
3. After connected, you can select which notifications should be sent to the Teams channel.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/c94b5aaa-2bf5-4da3-8e9c-e814a93d5e36.png" alt=""><figcaption></figcaption></figure>
