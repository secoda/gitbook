---
description: An overview of the Jira integration with Secoda
---

# Jira

{% content-ref url="metadata-extracted.md" %}
[metadata-extracted.md](metadata-extracted.md)
{% endcontent-ref %}

You might consider integrating your Secoda workspace with Jira if your team receives data requests through Jira.&#x20;

## **Getting Started with Jira** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

There are three steps to getting started using Jira with Secoda

1. Create an Jira project to upload your issues, or locate an existing project
2. Prepare your Jira credentials
3. Connect Jira to Secoda

### Create a Jira Project <a href="#h_0f245132d2" id="h_0f245132d2"></a>

**Note:** if you have an existing project that you would like to connect, skip this step

Navigate to [this url](https://id.atlassian.com/login) and login to or sign up for Jira with the same email used for Secoda. Navigate to Jira Software and find the Projects tab. If you do not have one, create a new project with a name similar that of the Secoda team it will be connected to for easy management. This can be either a team-managed or company-managed project.

Once created or found, you should see the project with its respective boards and issues:

![](https://secoda-public-media-assets.s3.amazonaws.com/5ac92ac5-952e-4535-91f0-f37b1f5f2e86.png)

### Prepare Your Jira Credentials <a href="#h_1255353919" id="h_1255353919"></a>

There are five items you will need in order to integrate your Jira project into Secoda:

1. Project URL
2. Project name
3. Project key
4. Jira API token
5. Account email

#### Project URL

To find your project's URL, name, and key, remain on your project's main page.

Note the website URL. You will take the section of URL resembling 'https://your-domain.atlassian.net/' and enter it into the Project URL section of Secoda's Jira integration setup. In the example screenshot above, this URL would be [https://secoda-elai.atlassian.net/](https://secoda-elai.atlassian.net/).

#### Project Name and Key

The project name and key will also be found on this page. Click the Projects tab to see a list of your projects, and find the one that you would like to integrate with Secoda. The project name will be the full name, while the project key is the 2 or 3 letter string inside of the brackets beside your project name

![](https://secoda-public-media-assets.s3.amazonaws.com/d90311b6-58e5-4f1b-bda4-d56c33010fbb.png)

In this example, the project name is Marketing, and the project key is MAR. Enter these values into Secoda's Jira integration setup.

#### API Token

Next, you must obtain an API token for Jira. Login to [this page](https://id.atlassian.com/manage-profile/security/api-tokens) and click "Create API token". When prompted, name the token the same name as your project, copy and save it somewhere secure, as it cannot be accessed afterwards. Enter this token into the respective section on Secoda's Jira integration setup.

Note: multiple API tokens can link to the same Jira project

![](https://secoda-public-media-assets.s3.amazonaws.com/fbf0e0db-663e-4b87-9773-6025728db2ca.png)

#### Account Email

To find your account email, you can click on the icon in the top right corner of any Jira page, and enter it into the Account Email section of Secoda's Jira integration setup.

Note: For Jira users to appear as assignees on Secoda, they **must** change email visibility to "Anyone" by going through Manage Account -> Profile and Visibility -> Contact

### Connect Jira to Secoda <a href="#h_448e650cba" id="h_448e650cba"></a>

1. Open your Secoda integrations page
2. Click on "New Integration" on the top left
3. Select Jira from the list of integrations
4. Input your Jira credentials from **Prepare Your Jira Credentials** above. This includes the project URL, name, key, API token, and your Jira email
5. Select the Teams that you wish to receive the Jira issues (appearing as Questions in Secoda)
6. Click on "Test Connection" to save the integration.
7. Once integration is created, click on “Run Extraction” from history tab to run your first extraction

![](https://secoda-public-media-assets.s3.amazonaws.com/3ca7f135-38a1-4e05-8a7a-ac59d5888ed5.png)

Once the Jira extraction finishes running, you will be able to view all issues from your Jira project in the desired team's Question page.
