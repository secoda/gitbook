---
description: An overview of the Amplitude integration with Secoda
---

# Amplitude

{% content-ref url="metadata-extracted.md" %}
[metadata-extracted.md](metadata-extracted.md)
{% endcontent-ref %}

## Getting Started with Amplitude <a href="#h_21e27f5a15" id="h_21e27f5a15"></a>

There are two steps to get started using Amplitude with Secoda:

1. Find your API Key and an API Secret (`Secret Key`) on Amplitude
2. Connect Amplitude to Secoda with your API Key and API Secret (`Secret Key`)

### Generate an API Key

1. Login to Amplitude and head to the Settings/Project/`Project Name` section.
2. Copy your API Key and API Secret (`Secret Key`).

### Connect to Amplitude

1. In Secoda, head to the **Integrations** page and click **New Integration**
2. Select **Amplitude**
3. Paste the API Key and API Secret (`Secret Key`)
4. Head to the **Sync** **History** tab on the side bar and click **Run sync**

{% hint style="info" %}
Currently only one environment gets extracted from the integration. [This documentation ](https://www.docs.developers.amplitude.com/analytics/apis/taxonomy-api/#authorization)from Amplitude explains how you can control which environment gets extracted
{% endhint %}

