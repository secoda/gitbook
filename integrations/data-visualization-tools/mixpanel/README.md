---
description: An overview of the Mixpanel integration with Secoda
---

# Mixpanel

{% content-ref url="metadata-extracted.md" %}
[metadata-extracted.md](metadata-extracted.md)
{% endcontent-ref %}

## Getting Started with Mixpanel

There are 2 steps to connect Mixpanel with Secoda:

1. Create a service account for your organization
2. Connect Mixpanel to Secoda

#### Create a Service Account

To create a service account, navigate to [Mixpanel](https://mixpanel.com/login/) and log into your account. Use the following steps to create a service account:

1. Click on the ‘settings’ button in the top right corner
2. Click on ‘organization settings’
3. Click on ‘service accounts’ on the left side bar
4. Click the ‘add service account’ button in the top right
5. Give it a name, select ‘member’, select all projects you want to be integrated with Secoda, select ‘analyst’ and ‘never’
6. **Save the username and secret, as the secret can not be accessed again**

> Note: Any service account settings will work for Secoda, so an existing account can be used as well. These are just our recommended settings.

#### Connect Mixpanel to Secoda

#### After creating your service account, the next step is to connect it to Secoda:

1. In Secoda app, select ‘add integration’ on the integration tab
2. Search for and select ‘Mixpanel’
3. Enter the service account username and secret, and the desired teams it will be linked to
4. Click ‘connect'

### After Connecting to Secoda

Due to [mixpanel rate limits](https://docs.mixpanel.com/docs/other-bits/rate-limits), some event properties may be missing after the initial extraction(s). Each time an extraction is run in Secoda, more event properties will be added until all events have been populated.
