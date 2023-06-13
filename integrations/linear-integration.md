---
description: This page walks through the Secoda and Linear integration that Secoda supports
---

# Linear

## Push questions and replies to Linear&#x20;

First head to [Linear's API](https://linear.app/secoda/settings/api/) page and generate a personal access token.

![](<https://secoda-public-media-assets.s3.amazonaws.com/Screen Shot 2022-04-29 at 9.37.43 AM.png>)

Next head to your Secoda workspace's settings page and find the Linear tab from the left hand menu. There you can enter the personal access key you generated.&#x20;

![](<https://secoda-public-media-assets.s3.amazonaws.com/Screen Shot 2022-04-29 at 9.34.51 AM.png>)

This will enable a one way sync of Secoda's questions and question replies to Linear. To enable a bidirectional sync between Linear and Secoda, you will have to add Secoda's webhook to Linear.

### Push updates from Linear to Secoda

Head to [this page](https://linear.app/secoda/settings/api/webhooks/new) and create a new webhook according to the screenshot below

![](<https://secoda-public-media-assets.s3.amazonaws.com/Screen Shot 2022-04-29 at 9.44.19 AM.png>)

To enable webhook integration with Linear, you will have to find out what your webhook endpoint is. If you are an on-prem customer, it will be `https://your-domain.com/api/v1/integration/linear/webhook` and if you are a cloud customer, your webhook will be `https://api.secoda.co/integration/linear/webhook`

### Testing the integration

If the integration is working properly, any question asked on Secoda, should automatically get added to your Linear triage.

![](<https://secoda-public-media-assets.s3.amazonaws.com/Screen Shot 2022-04-29 at 9.57.55 AM.png>)

* Assignee of the question is bi-directionally synced based on the email address of the assignee existing in both Secoda and Linear.
* Updating the status of the question on Linear, automatically updates it on Secoda
* Priority of the issue is bi-directionally synced with the priority of the question on Secoda

