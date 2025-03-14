---
description: List of all the metadata that Secoda pulls from Confluence
---

# Confluence metadata extracted

### What does Secoda extract from Confluence?

* Spaces (Spaces are referred to in the Confluence integration settings, under the "Spaces" tab)
  * Key (similar to the Space Name, except it is a unique identification)
* Pages (Pages are referred to as Documents in Secoda)
  * Title
  * Parent page
  * Owners
  * Updated At
  * Body

## Confluence page transformation to Secoda document

When a Confluence page is brought into Secoda, it'll transfer over and appear very similar to how it does in Confluence. These pages can be found in the Documents section of the team the integration is assigned to, and can be identified by looking at the source in the metadata side-bar.&#x20;

In the example below, you'll see that the main difference is that Secoda has the additional side-bar metadata. This is extracted from the Confluence page metadata and includes info like the page owner, created and updated timestamps.&#x20;

Example Confluence Page in Confluence:&#x20;

![Example Confluence page in Confluence](https://secoda-public-media-assets.s3.amazonaws.com/72384c09-7e35-4d8c-a24f-5ea5ba58ac95.png)

Same Confluence page in Secoda:&#x20;

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/6b92be98-59e6-425c-a3f5-3bf003024cfc.png" alt=""><figcaption><p>Example Confluence page after extraction by Secoda</p></figcaption></figure>

{% hint style="info" %}
**Note:** Some basic Confluence body elements (such as header links, some emojis, etc.) do not directly transfer into Secoda, and may appear different in Secoda Documents.\
Confluence plug-ins are not supported, so in-body plugins will have inconsistent transformation to Secoda Documents.
{% endhint %}

Read more about why you might integrate with Confluence [**here**](../../../best-practices/integrating-secoda-into-existing-workflows.md#integration-1).
