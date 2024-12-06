---
description: An overview of Cyera integration with Secoda
---

# Cyera

Cyera helps you define data sensitivity levels and automates the tagging and classification of your data. It also includes an access control component to ensure that only authorized personnel can access sensitive data.

Secoda's integration with Cyera not only retrieves these sensitivity tags but also matches them with existing tables and columns within Secoda. This functionality enhances data governance by making sensitivity labels visible and actionable within the Secoda environment, ensuring compliance with your organization's data privacy standards.

## Getting started with Cyera

There are two steps to get started using Cyera with Secoda

1. Create a Cyera API key for Secoda
2. Connect  Cyera to Secoda

#### Create a Cyera API key for Secoda

Once logged in to Cyera, follow these steps to create an API token:

1. Click on the **Settings** icon on the bottom left

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/0fffabf6-8568-4993-93cb-529747e53297.png" alt=""><figcaption></figcaption></figure>

2. Click on **API Token** on the popup

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/98bf146b-f098-4c75-a7ca-f815dd4b90f7.png" alt=""><figcaption></figcaption></figure>

3. Generate a token name `secoda`. For lowest level of permissions, select `Viewer` role

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/708b0b7f-e8d1-48ff-9f90-4aca42a3a8b9.png" alt=""><figcaption></figcaption></figure>

4. Copy and save your API token and secret, as it can't be accessed again

#### Connect Cyera to Secoda

After retrieving the API token token and secret, the next step is to connect it to Secoda:

1. In the Secoda App, select Add Integration on the Integrations tab
2. Search for and select Cyera
3. Enter your Cyera API token (in the Client ID field) and secret retrieved above
4. Once successfully connected, a prompt will ask you to run the initial extraction

## After Connecting to Secoda

Resources classified in Cyera are automatically tagged with the same classifications in Secoda. You can view the list of Cyera tags in the [Tags](../../resource-and-metadata-management/tags/) tab under Workspace Settings.&#x20;

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/f09efcd8-3441-482e-b894-bcedc0b846e0.png" alt=""><figcaption><p>Example of Cyera Tags in Secoda</p></figcaption></figure>

:warning:Resources tagged in Cyera that do not exist in Secoda will not have their classifications ingested into Secoda.
