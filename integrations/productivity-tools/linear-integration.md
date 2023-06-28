---
description: This page walks through the Secoda and Linear integration that Secoda supports
---

# Linear Integration

## Push questions and replies to Linear

First head to [Linear's API](https://linear.app/secoda/settings/api/) page and generate a personal access token.

![](https://secoda-public-media-assets.s3.amazonaws.com/Screen%20Shot%202022-04-29%20at%209.37.43%20AM.png)

Next head to your Secoda workspace's settings page and find the Linear tab from the left hand menu. There you can enter the personal access key you generated.

![](https://secoda-public-media-assets.s3.amazonaws.com/Screen%20Shot%202022-04-29%20at%209.34.51%20AM.png)

This will enable a one way sync of Secoda's questions and question replies to Linear. To enable a bidirectional sync between Linear and Secoda, you will have to add Secoda's webhook to Linear.

### Push updates from Linear to Secoda

Head to [this page](https://linear.app/secoda/settings/api/webhooks/new) and create a new webhook according to the screenshot below

![](https://secoda-public-media-assets.s3.amazonaws.com/Screen%20Shot%202022-04-29%20at%209.44.19%20AM.png)

To enable webhook integration with Linear, you will have to find out what your webhook endpoint is. If you are an on-prem customer, it will be `https://your-domain.com/api/v1/integration/linear/webhook` and if you are a cloud customer, your webhook will be `https://api.secoda.co/integration/linear/webhook`

### Testing the integration

If the integration is working properly, any question asked on Secoda, should automatically get added to your Linear triage.

![](https://secoda-public-media-assets.s3.amazonaws.com/Screen%20Shot%202022-04-29%20at%209.57.55%20AM.png)

* Assignee of the question is bi-directionally synced based on the email address of the assignee existing in both Secoda and Linear.
* Updating the status of the question on Linear, automatically updates it on Secoda
* Priority of the issue is bi-directionally synced with the priority of the question on Secoda
