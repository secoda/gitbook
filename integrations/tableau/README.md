---
description: >-
  This page walks through the Secoda and Tableau integration that Secoda
  supports
---

# Tableau Integration

## **Connect Tableau** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

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

Use the table below to determine your **API version.**

The site name can be found in the url on Tableau Online which immediately follows `/#/site`. For example:

`https://prod-useast-b.online.tableau.com/#/site/`_**`secoda`**_`/home`

#### **Connect Tableau to Secoda** <a href="#h_ee8fd0e047" id="h_ee8fd0e047"></a>

After creating a Tableau access token, the next step is to connect to Secoda:

1. In the Secoda App, select ‘Add Integration’ on the Integrations tab
2. Search for and select ‘Tableau’
3. Enter your Tableau credentials you created above
4. Click 'Connect'

| **Tableau Server version**      | **REST API version** | **Schema version** |
| ------------------------------- | -------------------- | ------------------ |
| 8.3, 9.0                        | 2.0                  | 2.0                |
| 9.0.1 and later versions of 9.0 | 2.0                  | 2.0.1              |
| 9.1                             | 2.0                  | 2.0.1              |
| 9.2                             | 2.1                  | 2.1                |
| 9.3                             | 2.2                  | 2.2                |
| 10.0                            | 2.3                  | 2.3                |
| 10.1                            | 2.4                  | 2.4                |
| 10.2                            | 2.5                  | 2.5                |
| 10.3                            | 2.6                  | 2.6                |
| 10.4                            | 2.7                  | 2.7                |
| 10.5                            | 2.8                  | 2.8                |
| 2018.1                          | 3.0                  | 3.0                |
| 2018.2                          | 3.1                  | 3.1                |
| 2018.3                          | 3.2                  | 3.2                |
| 2019.1                          | 3.3                  | 3.3                |
| 2019.2                          | 3.4                  | 3.4                |
| 2019.3                          | 3.5                  | 3.5                |
| 2019.4                          | 3.6                  | 3.6                |
| 2020.1                          | 3.7                  | 3.7                |
| 2020.2                          | 3.8                  | 3.8                |
| 2020.3                          | 3.9                  | 3.9                |
| 2020.4                          | 3.10                 | 3.10               |
| 2021.1                          | 3.11                 | 3.11               |
| 2021.2                          | 3.12                 | 3.12               |
| 2021.3                          | 3.13                 | 3.13               |
| 2021.4                          | 3.14                 | 3.14               |
| 2022.1                          | 3.15                 | 3.15               |
| 2022.2                          | 3.16                 | 3.16               |
