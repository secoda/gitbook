---
description: An overview of the Monte Carlo integration with Secoda
---

# Monte Carlo

{% content-ref url="monte-carlo-metadata-extracted.md" %}
[monte-carlo-metadata-extracted.md](monte-carlo-metadata-extracted.md)
{% endcontent-ref %}

## Getting started with Monte Carlo

There are two steps to get started using Monte Carlo with Secoda

1. Create a Monte Carlo API key and secret for Secoda
2. Connect  Monte Carlo to Secoda

#### Create a Monte Carlo API key for Secoda

Once logged in to Monte Carlo, follow these steps to create an API token:

1. Click on the **Settings** button in the nav bar and select the **API**  section

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/2b0bc800-39b3-473b-977c-60ddb9ca8226.png" alt=""><figcaption></figcaption></figure>

2. Click **Create key** fill out the details and click **Create**
3. Copy and save your API token and secret, as it can't be accessed again

#### Connect Monte Carlo to Secoda

After retrieving the API token token and secret, the next step is to connect it to Secoda:

1. In the Secoda App, select Connect Integration on the Integrations tab
2. Search for and select Monte Carlo
3. Enter your Monte Carlo API token and secret
4. Once successfully connected, a prompt will ask you to run the initial extraction

## After Connecting to Secoda

Monte Carlo monitors are automatically associated their respective tables in Secoda. The monitors show up in the "Tests" tab on the table page.

:warning:Tables monitored in Monte Carlo that do not exist in Secoda will not have their monitors ingested into Secoda.

