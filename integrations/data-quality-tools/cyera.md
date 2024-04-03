---
description: An overview of Cyera integration with Secoda
---

# Cyera

Secoda currently supports retrieving tags from Cyera and matching those tag with existing tables and columns inside Secoda.

## Getting started with Cyera

There are two steps to get started using Cyera with Secoda

1. Create a Cyera API key for Secoda
2. Connect  Cyera to Secoda

#### Create a Cyera API key for Secoda

Once logged in to Cyera, follow these steps to create an API token:

1. Click on the **Settings** icon on the bottom left

<figure><img src="../../.gitbook/assets/Screenshot 2024-03-15 at 11.07.19 AM (1).png" alt=""><figcaption></figcaption></figure>

2. Click on **API Token** on the popup

<figure><img src="../../.gitbook/assets/Screenshot 2024-03-15 at 11.07.34 AM.png" alt=""><figcaption></figcaption></figure>

3. Generate a token name `secoda`. For lowest level of permissions, select `Viewer` role

<figure><img src="../../.gitbook/assets/Screenshot 2024-03-15 at 11.10.24 AM.png" alt=""><figcaption></figcaption></figure>

4. Copy and save your API token and secret, as it can't be accessed again

#### Connect Cyera to Secoda

After retrieving the API token token and secret, the next step is to connect it to Secoda:

1. In the Secoda App, select Add Integration on the Integrations tab
2. Search for and select Cyera
3. Enter your Cyera API token (in the Client ID field) and secret retrieved above
4. Once successfully connected, a prompt will ask you to run the initial extraction

### After Connecting to Secoda

Any resources that are classified in Cyera will get tagged with the same classifications in Secoda. The list of Cyera tags can be seen in the [Tags](../../resource-and-metadata-management/tags/custom-tags.md) tab of the Workspace Settings.

:warning:Resources that are tagged in Cyera but doesn't exist in Secoda will not get their classifications ingested into Secoda.

