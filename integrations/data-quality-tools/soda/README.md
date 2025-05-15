---
description: An overview of the Soda Cloud integration with Secoda
---

# Soda

{% content-ref url="soda-metadata-extracted.md" %}
[soda-metadata-extracted.md](soda-metadata-extracted.md)
{% endcontent-ref %}

Getting started with Soda

There are two steps to get started using Soda Cloud with Secoda

1. Creating a Soda API key and secret
2. Connecting Soda to Secoda

#### Creating a Soda API key and secret

To generate an API key and secret go to your profile by clicking on the icon with your initials in the top right corner of the page, then clicking **"Profile"**.

In the profile go to the API Keys tab. From there generate a new API key and save the Key and Secret.

#### Connecting Soda to Secoda

After retrieving the API key and secret, the next step is to connect it to Secoda:

1. In the Secoda App, select Connect Integration on the Integrations tab
2. Search for and select Soda Cloud
3. Enter your Soda key and secret
4. For the base URL, this depends on the region you registered with \
   US: [https://cloud.us.soda.io](https://cloud.us.soda.io/api/v1/checks)\
   EU: [https://cloud.soda.io](https://cloud.soda.io/api/v1/checks)
5. Once successfully connected, a prompt will ask you to run the initial extraction

## After Connecting to Secoda

Soda checks are automatically associated their respective tables in Secoda. The checks show up in the "Tests" tab on the table page.

{% hint style="info" %}
Tables monitored in Soda that do not exist in Secoda will not have their checks ingested into Secoda.
{% endhint %}
