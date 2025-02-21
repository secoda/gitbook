---
description: An overview of the Confluence integration with Secoda
---

# Confluence

{% content-ref url="metadata-extracted.md" %}
[metadata-extracted.md](metadata-extracted.md)
{% endcontent-ref %}

## Getting Started with Confluence

There are 3 steps to connect Confluence with Secoda:

1. Create an API token and retrieve the email used to create it
2. Retrieve your domain name
3. Connect Confluence to Secoda

### Create an API Token

API tokens in Confluence are based on individual accounts, so [log into Confluence](https://id.atlassian.com/login) with an account that has access to the spaces desired.

Once logged in, follow these steps to create a token:

1. Click on the profile icon in the top right
2. Click on ‘Manage Account’

![](https://secoda-public-media-assets.s3.amazonaws.com/22b16b8c-cd43-4a20-b581-34b13e207927.png)

3. Ensure you are on the ‘Profile and visibility’ tab
4. Scroll to the bottom to retrieve the email address being used

![](https://secoda-public-media-assets.s3.amazonaws.com/a973ea4d-6939-4deb-8243-5c49d95b5231.png)

5. Select the ‘Security’ tab at the top of the page
6. Select the ‘[Create and manage API tokens](https://id.atlassian.com/manage-profile/security/api-tokens)’ link under the API token subtitle
7. Select the ‘Create API token’ button and give it a label

![](https://secoda-public-media-assets.s3.amazonaws.com/79f30228-62fb-4ee7-810c-b40344bb7098.png)

8. Copy and save the API token, as it can’t be accessed again

### Retrieve your Domain Name

The domain name is the name given to the Confluence workspace containing spaces. The name can be found in the URL when in the confluence workspace, in the format of https://{domain-name}.atlassian.net/. For example, the url could be "https://secoda.atlassian.net/wiki/home", so the domain name would be Secoda.

The domain name can also be retrieved from the [Atlassian Start](https://start.atlassian.com/) page, under the Confluence image.

![An example of a domain name is highlighted below the Confluence icon](https://secoda-public-media-assets.s3.amazonaws.com/e253f311-af26-4ea1-b581-2dae7ceb8521.png)

### Connect Confluence to Secoda

After retrieving the API token and domain name, the next step is to connect to Secoda:

1. In the Secoda App, select ‘Add Integration’ on the Integrations tab
2. Search for and select Confluence
3. Enter your Confluence domain name, email address and API token retrieved above
4. Once successfully connected, a prompt labeled `Schema` will appear which corresponds to Confluence spaces. Select the spaces you want to integrate into Secoda
5. Run the initial extraction

![](https://secoda-public-media-assets.s3.amazonaws.com/3a017795-d7a7-4cdb-984a-b70e64d72999.png)

## After Connecting to Secoda

Any spaces that are created or deleted will not be updated under the spaces tab on the integration page. Any new public spaces created will be automatically imported during the next sync, and any deleted space contents will be removed. If you do not want any new spaces brought in, then the confluence integration must be deleted and re-connected for the space options to be updated.

:warning:Warning that any changes made to the Confluence documents in Secoda will be overwritten the next time a Confluence sync is run. Any changes that are desired to be made to these documents should be done in confluence, then run a sync in Secoda.
