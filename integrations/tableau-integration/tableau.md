---
description: This page walks through how to connect Secoda and Tableau
---

# Connect Tableau

There are three steps to connect Tableau with Secoda:

1. Enable Metadata API
2. Create an Access Token
3. Retrieve your host name, API version, and site name
4. Connect Tableau to Secoda

#### Enable Metadata API (Tableau Server ONLY) <a href="#h_741406548f" id="h_741406548f"></a>

If you're on Tableau Online, you can skip this step. If you're on Tableau Server reach out to your administrator to enable the metadata API. Instructions for enabling the API can be found in this [Tableau documentation](https://help.tableau.com/current/api/metadata\_api/en-us/docs/meta\_api\_start.html) under the section **Enable the Tableau Metadata API for Tableau Server.**

1. Open a command prompt as an admin on the initial node (where TSM is installed) in the cluster.
2. Run the command: `tsm maintenance metadata-services enable`

#### **Create an Access Token** <a href="#h_741406548f" id="h_741406548f"></a>

To create a Tableau access token for Secoda log into your account. Use the following steps to generate an access token:

1. Click on your avatar in the top right and select 'My Account Settings' from the dropdown menu.
2. Scroll to the section 'Personal Access Tokens'
3. Enter in a token name and press 'Create new token'. Save the token name and secret, this will be used to connect to Secoda.

#### **Retrieve your host name and API version** <a href="#h_3cbb90f2a5" id="h_3cbb90f2a5"></a>

Your **host** is the first part of the url in Tableau Online before the `#` and should be in the form of `https://<location>.online.tableau.com`. For example:

_**`https://prod-useast-b.online.tableau.com`**_`/#/site/secoda/home`

Use the table from this page to determine your API version. [https://help.tableau.com/current/api/rest\_api/en-us/REST/rest\_api\_concepts\_versions.htm](https://help.tableau.com/current/api/rest\_api/en-us/REST/rest\_api\_concepts\_versions.htm)

The site name can be found in the url on Tableau Online which immediately follows `/#/site`. For example:

`https://prod-useast-b.online.tableau.com/#/site/`_**`secoda`**_`/home`

#### **Connect Tableau to Secoda** <a href="#h_ee8fd0e047" id="h_ee8fd0e047"></a>

After creating a Tableau access token, the next step is to connect to Secoda:

1. In the Secoda App, select ‘Add Integration’ on the Integrations tab
2. Search for and select ‘Tableau’
3. Enter your Tableau credentials you created above
4. Click 'Connect'

## Troubleshooting

#### Tableau previews are not working
Error: `iframe is denied by “X-Frame-Options“ directive set to “SAMEORIGIN“`.
You must disable clickjack defense if you are hosting tableau on-premise. Please refer to this article for more details: https://help.tableau.com/current/server/en-us/clickjack_protection.htm. The relevant commands are:
```
tsm configuration set -k wgserver.clickjack_defense.enabled -v false
tsm pending-changes apply
```