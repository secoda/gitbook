# Git Integration

#### Getting Started <a href="#h_7149df32f0" id="h_7149df32f0"></a>

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

1. Open your Secoda settings.
2. Navigate to the “Git” tab on the left
3. Input your repo https web address from the first step into “Repository Origin”
4. Input your Git credentials from step 2 for “Git Username” and “Git Password”

![](https://secoda.intercom-attachments-1.com/i/o/436142140/96b913c1a99f3b05ec862a89/Screen\_Shot\_2021-12-17\_at\_12.00.27\_PM.png)

1. Click on add repo to save the integration.
2. Once integration is created, click on “Push to Git” to run your first extraction

![](https://secoda.intercom-attachments-1.com/i/o/436142146/7f210e6d4e2fdf779fee7109/Screen\_Shot\_2021-12-17\_at\_11.33.07\_AM.png)

Once the git extraction finishes running, you will receive an email indicating the extraction has been completed.
