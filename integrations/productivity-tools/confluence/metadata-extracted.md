# Metadata Extracted

## What does Secoda extract from Confluence?

* Spaces (Spaces are referred to in the Confluence integration settings, under the "Spaces" tab)
  * Key (similar to the Space Name, except it is a unique identification)
* Pages (Pages are referred to as Documents in Secoda)
  * Title
  * Parent page
  * Owners
  * Updated At
  * Body

## Confluence page transformation to Secoda document

When a Confluence page is brought into Secoda, it'll transfer over and appear very similar to how it does in Confluence. In the example below, you'll see that the main difference is that Secoda has the additional side-bar metadata. This is extracted from the Confluence page metadata and includes info like the page owner, created and updated timestamps.

<figure><img src="../../../.gitbook/assets/image (8).png" alt=""><figcaption><p>Example Confluence page in Confluence</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (7).png" alt=""><figcaption><p>Example Confluence page after extraction by Secoda</p></figcaption></figure>

{% hint style="info" %}
**Note:** Some basic Confluence body elements (such as header links, some emojis, etc.) do not directly transfer into Secoda, and may appear different in Secoda Documents. \
Confluence plug-ins are not supported, so in-body plugins will have inconsistent transformation to Secoda Documents.
{% endhint %}