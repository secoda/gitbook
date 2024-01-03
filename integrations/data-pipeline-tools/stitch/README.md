---
description: An overview of the Stitch integration with Secoda
---

# Stitch

{% content-ref url="stitch-metadata-extracted.md" %}
[stitch-metadata-extracted.md](stitch-metadata-extracted.md)
{% endcontent-ref %}

## Getting Started with Stitch <a href="#h_21e27f5a15" id="h_21e27f5a15"></a>

&#x20;There are two steps to get started using Stitch with Secoda:

1. Retrieve your Stitch Client ID
2. Generate an API Key on Stitch
3. Connect Stitch to Secoda with your API Key and API Secret

{% hint style="info" %}
Secoda pulls the following metadata from the Stitch API: jobs, run times, owners, destinations, and other general metadata around jobs.
{% endhint %}

### Retrieve your Stitch Client ID

Your Stitch client ID can be found in the URL of your Stitch instance. For example, the client ID for`https://app.stitchdata.com/client/210396/pipeline/v2/welcome` is 210396.

### Generate an API Key

1. Login to Stitch and head to the Settings > Account Settings section.
2. Generate an API Access Key

### Connect Stitch to Secoda

1. In Secoda, head to the **Integrations** page and click **New Integration**
2. Select **Stitch**
3. Paste the API Key
4. Head to the **Sync History** tab on the side bar and click **Run sync**
