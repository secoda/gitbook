---
description: >-
  To make your popularity calculations more accurate, you'll want to mark your
  users as Service Accounts.
---

# Define Service Accounts

## Overview of service accounts

Service accounts are emails associated with the integration that **do not** exist as Members in the Secoda Workspace. To count these emails towards the popularity calculation of a resource, you'll need to mark them as such.

To do this, please navigate to the Popularity tab of the integration settings. You'll see a list of emails captured from the integration that do not exist as Members in the Secoda Workspace. You'll need to select all the emails that you'd like to count towards Popularity.&#x20;

For example, if `bob@company.com` runs a query against your Redshift instance, but is not a member of the Secoda workspace, `bob@company.com` will be considered a Service Account in Secoda and will show up in the Popularity tab of the integrations settings as seen below.&#x20;

<figure><img src="../../../.gitbook/assets/Screenshot 2023-07-24 at 11.22.49 AM.png" alt=""><figcaption></figcaption></figure>

If an email associated with a Service Account signs into Secoda, it will be converted from a Service Account to a Secoda user and show up in the Members tab of the workspace settings.&#x20;

To learn more about how Popularity is calculated, please see the documentation [here](https://docs.secoda.co/faq#how-is-the-popularity-calculated).&#x20;

{% hint style="info" %}
Not using Secoda to manage your data documentation yet? Sign up for free [here](https://app.secoda.co/) 👈
{% endhint %}
