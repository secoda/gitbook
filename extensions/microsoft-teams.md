---
description: Seamlessly integrate Secoda with your Microsoft Teams
---

# Microsoft Teams

## Overview

The Secoda extension for Microsoft Teams provides access to Secoda AI and notifications in Teams, enabling users to ask questions and get answers from company data within channels. This guide outlines installing and configuring the app, including uploading the custom app, setting up the Secoda bot with an API key, and creating a channel with an incoming webhook for Secoda notifications. This setup ensures seamless data interaction and real-time workspace updates.

## Secoda AI in Microsoft Teams <a href="#id-69a6bfc2-329e-4a36-9359-a3305861cb29" id="id-69a6bfc2-329e-4a36-9359-a3305861cb29"></a>

To install the Secoda AI for Microsoft Teams App, follow these steps.

#### Access Your Team <a href="#id-9c82b7b3-cf18-4543-9030-108bd323bf5c" id="id-9c82b7b3-cf18-4543-9030-108bd323bf5c"></a>

1. Open Microsoft Teams
2. Navigate to your desired team
3. Click on the **Apps** tab at the top of the team interface

#### Step 2: Upload the Custom App <a href="#d079554c-6dc7-44a3-90cb-f73a48922b35" id="d079554c-6dc7-44a3-90cb-f73a48922b35"></a>

1. In the Apps section, click **Upload an app** in the top right
2. Select **Upload a custom app** from the dropdown menu
3. Choose the Secoda app package file:
4. Click **Upload** to proceed

{% file src="../.gitbook/assets/secoda_ai_microsoft_teams_app.zip" %}

#### Step 3: Review and Install <a href="#id-8a36b728-a5df-4732-9396-96a7e54bb9d0" id="id-8a36b728-a5df-4732-9396-96a7e54bb9d0"></a>

1. The Secoda app information dialog will appear, showing:
   * App overview and description
   * Features and permissions
   * Version information
2. Review the app details and permissions
3. Click **Add** to install the app to your team

#### Step 4: Initial Setup and Configuration <a href="#e0fe5f4b-5c37-4019-8249-949dbcdbc37f" id="e0fe5f4b-5c37-4019-8249-949dbcdbc37f"></a>

1. After installation, go to any channel in your team
2. Type `@Secoda` to mention the app
3. The app will respond with a **Bot Setup Required** message
4. Click on **Configure Secoda Bot** or follow the setup link provided
5. Enter your **Secoda API key** when prompted
6. Complete the configuration process

### Using the App <a href="#id-74ab90f6-7464-4f9c-94c0-c4c4e9fd8134" id="id-74ab90f6-7464-4f9c-94c0-c4c4e9fd8134"></a>

Once installed and configured, you can interact with the Secoda app by mentioning `@Secoda` in any message within channels where it's available. The app will help you ask questions and get answers from your company data through Secoda AI.

## Secoda Notifications in Microsoft Teams

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
