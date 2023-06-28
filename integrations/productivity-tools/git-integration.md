---
description: This page walks through the Secoda and Git integration that Secoda supports
---

# Git Integration for data docs

## **Getting Started with Git** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

There are three steps to getting started using Git with Secoda

1. Create an empty Git repository for Secoda to push data to.
2. Prepare your Git credentials
3. Connect Git to Secoda

The following guide contains screenshots and links from Github but Secoda’s Git integration works with every other Git host as well.

#### Create an Empty Git Repository <a href="#h_0f245132d2" id="h_0f245132d2"></a>

Navigate to [this url](https://github.com/new) to create a new repo. Please ensure you set your repo to be private, otherwise you risk exposing your company’s private data to the public.

![](https://secoda.intercom-attachments-1.com/i/o/436142123/0be2233ad5e024e388c18901/Screen\_Shot\_2021-12-17\_at\_11.19.54\_AM.png)

Once the repo is created. Please note the HTTPs URL of the repo.

![](https://secoda.intercom-attachments-1.com/i/o/436142128/75acb19462d5dc116c597aff/Screen\_Shot\_2021-12-17\_at\_11.29.34\_AM.png)

#### Prepare Your Git Credentials <a href="#h_1255353919" id="h_1255353919"></a>

Your git username password are the same as your Git hosting credentials. However, If you have enabled 2FA on your account, you will have to generate a new personal token.

1. Open this [link on](https://github.com/settings/tokens) Github
2. Click on “Generate new Token” at the top right
3. Name your token “Secoda Git Integration” or any other name you see fit
4. Set the expiration to “No Expiration”
5. Check the “repo” checkbox
6. Scroll to the bottom and click on “Generate Token”
7. Please note the generated token for the next step.

![](https://secoda.intercom-attachments-1.com/i/o/436142134/847a8df89ec800c2f717a5ef/Screen\_Shot\_2021-12-17\_at\_11.27.51\_AM.png)

#### Connect Git to Secoda <a href="#h_448e650cba" id="h_448e650cba"></a>

1. Open your Secoda integrations page
2. Click on "New Integration" on the top left
3. Select git from the list of integrations
4. Input your Git credentials from step 2 for “Git Username” and “Git Password”
5. Click on "Test Connection" to save the integration.
6. Once integration is created, click on “Run Extraction” from history tab to run your first extraction

![](<https://secoda-public-media-assets.s3.amazonaws.com/Screen%20Shot%202022-07-25%20at%203.38.24%20PM.png>)

Once the git extraction finishes running, you will receive a notification on Secoda if you have enabled the setting to receive extraction success notifications.
