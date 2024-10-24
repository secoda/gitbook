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

<figure><img src="../../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>

2. Search and select **Incoming Webhook**

<figure><img src="../../.gitbook/assets/image (18).png" alt=""><figcaption></figcaption></figure>

3. Name your incoming webhook **Secoda,** and add Secoda icon, you can download the following image

<figure><img src="../../.gitbook/assets/secoda-app-icon.png" alt="" width="188"><figcaption></figcaption></figure>

4. Copy the URL in the modal and select **Done.**

You can also follow the [guide by Microsoft on how to create an Incoming Webhook](https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook).

## Connect with Secoda and update notification settings

1. Use the Incoming Webhook URL in the previous step in the Microsoft Teams connection form.
2. Test connection. Secoda will send a test message to see if the connection was made.
3. After connected, you can select which notifications should be sent to the Teams channel.

<figure><img src="../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>
