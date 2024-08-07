---
description: An overview of the Coalesce Integration with Secoda
---

# Coalesce

{% content-ref url="coalesce-metadata-extracted.md" %}
[coalesce-metadata-extracted.md](coalesce-metadata-extracted.md)
{% endcontent-ref %}

## **Getting Started with Coalesce** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

There are three steps to get started using Coalesce with Secoda:

1. Retrieve your Coalesce Host
2. Retrieve your API key
3. Retrieve your Environment ID
4. Connect Coalesce to Secoda

#### **Retrieve your Coalesce Host** <a href="#h_89d08409d1" id="h_89d08409d1"></a>

You can determine your Coalesce host by logging into Coalesce and taking the base url from the link. In the example below, the host would be `https://app.coalescesoftware.io`

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

#### **Retrieve your API key** <a href="#h_a2cb9baed8" id="h_a2cb9baed8"></a>

For Secoda to retrieve metadata from Coalesce, you need to get your Access Token. To do this, go to **Deploy > Generate Access Token** and copy the token.

<figure><img src="../../../.gitbook/assets/Screen Shot 2024-08-07 at 9.45.50 AM.png" alt=""><figcaption></figcaption></figure>

**Retrieve your Environment ID**

On the **Deploy** page, get the ID of the environment that you want to import into Secoda. For the example below, it would be 3.

<figure><img src="../../../.gitbook/assets/Screen Shot 2024-08-07 at 9.48.53 AM.png" alt=""><figcaption></figcaption></figure>

**Connect Coalesce to Secoda**

The next step is to connect Secoda:

1. In the Secoda App, select **Add Integration** on the Integrations tab
2. Search for and select the **Coalesce** integration
3. Enter your Coalesce Host, Access Token, and Environment ID. This information is kept encrypted
4. Click on **Test Connection** to save the integration.
5. Once integration is created, click on **Run Sync** to run your first extraction
