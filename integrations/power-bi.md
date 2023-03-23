---
description: >-
  This page walks through the Secoda and Power BI integration that Secoda
  supports
---

# Power BI Integration

## **Getting Started with Power BI** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

{% hint style="info" %}
The user that connects Power BI to Secoda must be both:

* An administrator for Azure Active Directory
* An administrator for Power BI
{% endhint %}

The PowerBI integration uses OAuth 2.0 to connect Secoda to your Power BI workspace. To connect Power BI to Secoda follow the steps below:

1. Go to [https://app.secoda.co/integrations/new](https://app.secoda.co/integrations/new) and select the Power BI option
2.  Click "Connect". You'll be brought to the consent page that asks for the following permissions on your Power BI workspace

    ![](<../.gitbook/assets/image (2) (1) (3).png>) ![](<../.gitbook/assets/Screen Shot 2022-04-21 at 12.17.05 PM (1).png>)
3. After you've connected Power BI to Secoda go to [https://app.secoda.co/integrations](https://app.secoda.co/integrations)
4. Select your Power BI integration and go to **History > Run extraction > Metadata extraction** which will start an extraction for your Power BI integration. ![](<../.gitbook/assets/image (4) (1).png>)

To extract Power BI datasets, the "Enhance admin APIs responses with detailed metadata" option in the admin panel must be toggled on.

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>
