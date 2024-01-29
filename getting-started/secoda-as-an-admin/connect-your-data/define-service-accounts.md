---
description: >-
  To make your popularity calculations more accurate, you'll want to mark emails
  as Service Accounts.
---

# Define Service Accounts

## Overview of service accounts

Service accounts are emails associated with the integration that **do not** exist as Members in the Secoda Workspace. These emails can fall under two categories: actual humans (your coworkers) who are not yet members in Secoda yet; or bot accounts associated with the integration.

{% hint style="info" %}
Ideally, you'd want to have the human-related emails checked off so that they are calculated towards the popularity of a resource. However, for bot accounts you may not want them included because it would alter the accuracy of the popularity metric.
{% endhint %}

To define which emails should be counted, please navigate to the Popularity tab of the integration settings. You'll see a list of emails captured from the integration that do not exist as Members in the Secoda Workspace. You'll need to select all the emails that you'd like to count towards Popularity, and uncheck those that should not be counted.

For example, if `bob@company.com` runs a query against your Redshift instance, but is not a member of the Secoda workspace, `bob@company.com` will be considered a Service Account in Secoda and will show up in the Popularity tab of the integrations settings as seen below.&#x20;

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/1720d699-2b8b-4bc6-b385-b771b3d328e4.png" alt=""></figure>

If an email associated with a Service Account signs into Secoda, it will be converted from a Service Account to a Secoda user and show up in the Members tab of the workspace settings.&#x20;

To learn more about how Popularity is calculated, please see the documentation [here](https://docs.secoda.co/faq#how-is-the-popularity-calculated).&#x20;

{% hint style="info" %}
Not using Secoda to manage your data documentation yet? Sign up for free [here](https://app.secoda.co/) 👈
{% endhint %}
