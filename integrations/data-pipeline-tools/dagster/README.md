---
description: An overview of the Dagster integration with Secoda
---

# Dagster

{% content-ref url="metadata-extracted.md" %}
[metadata-extracted.md](metadata-extracted.md)
{% endcontent-ref %}

## Getting Started with Dagster

There are three steps to connect Dagster with Secoda:

1. Retrieve the host domain
2. Create a user token (Dagster Cloud only)
3. Connect Dagster to Secoda

#### Retrieve the host domain

To retrieve the host domain, navigate to the page where you normally interact with the project in Dagster. Take the part of the URL that does not change when navigating around the website as your host domain.

For example, if the page is on the 'Deployment' tab and the link is "https://example.dagster.cloud/ex/locations", then the host domain is "https://example.dagster.cloud/ex" in this case.

![](https://raw.githubusercontent.com/secoda/gitbook/master/.gitbook/assets/image%20\(1\).png)

#### Create a user token

If you are not using Dagster Cloud, you can skip this step.

If you are using Dagster Cloud, navigate to your Dagster Cloud domain found previously and use the following steps to create a user token:

1. Click on your profile in the top-right corner
2. Select **Organization settings** from the drop-down that appears
3. Click on the **Tokens** tab at the top of the page
4. Click on the **Create user token** button on the right hand side

![](https://raw.githubusercontent.com/secoda/gitbook/master/.gitbook/assets/image.png)

5. Click **Reveal token** on the newly created token
6. Click the text to copy the value

#### Connect Dagster to Secoda

After retrieving the host domain and a suer token as needed, the next step is to connect to Secoda:

1. In the Secoda App, select **Add Integration** on the integration tab
2. Search for and select Dagster
3. Enter your Dagster host domain and user token for Dagster cloud instances
4. Click connect
