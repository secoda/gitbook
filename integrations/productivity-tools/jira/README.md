---
description: An overview of the Jira integration with Secoda
---

# Jira

{% content-ref url="metadata-extracted.md" %}
[metadata-extracted.md](metadata-extracted.md)
{% endcontent-ref %}

You might consider integrating your Secoda workspace with Jira if your team receives data requests through Jira.

## **Getting Started with Jira** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

There are three steps to getting started using Jira with Secoda

1. Create a Jira project to upload your issues, or locate an existing project
2. Prepare your Jira credentials
3. Connect Jira to Secoda

### Create a Jira Project <a href="#h_0f245132d2" id="h_0f245132d2"></a>

**Note:** if you have an existing project that you would like to connect, skip this step

Navigate to [this url](https://id.atlassian.com/login) and login to or sign up for Jira with the same email used for Secoda. Navigate to Jira Software and find the Projects tab. If you do not have one, create a new project with a name similar that of the Secoda team it will be connected to for easy management. This can be either a team-managed or company-managed project.

Once created or found, you should see the project with its respective boards and issues:

![](https://secoda-public-media-assets.s3.amazonaws.com/5ac92ac5-952e-4535-91f0-f37b1f5f2e86.png)

### Prepare Your Jira Credentials <a href="#h_1255353919" id="h_1255353919"></a>

There are nine items you will need in order to integrate your Jira project into Secoda:

1. Project URL
2. Project name
3. Project key
4. Issues Filter (optional)
5. Jira API token
6. Account email
7. Organization ID
8. Organization Admin API key
9. Webhook secret

#### Project URL

To find your project's URL, name, and key, remain on your project's main page.

Note the website URL. You will take the section of URL resembling `https://your-domain.atlassian.net/` and enter it into the Project URL section of Secoda's Jira integration setup. In the example screenshot above, this URL would be [https://secoda-elai.atlassian.net/](https://secoda-elai.atlassian.net/).

#### Project Name and Key

The project name and key will also be found on this page. Click the Projects tab to see a list of your projects, and find the one that you would like to integrate with Secoda. The project name will be the full name, while the project key is the 2 or 3 letter string inside of the brackets beside your project name

![](https://secoda-public-media-assets.s3.amazonaws.com/d90311b6-58e5-4f1b-bda4-d56c33010fbb.png)

In this example, the project name is Marketing, and the project key is MAR. Enter these values into Secoda's Jira integration setup.

#### Issues Filter (optional)

If you want to filter the issues that will be synced to Secoda, you can enter a custom JQL query. Go to the Filters tab and click on/create a new filter. Once you are satisfied with the filter, change the switch found in the top right from Basic to JQL. The JQL query will pop up in the header bar, and you can copy that in the setup.

Note: The project in the filter must be the same as the project you entered from above, or no issues will be synced.

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

#### API Token

Next, you must obtain an API token for Jira. Login to [this page](https://id.atlassian.com/manage-profile/security/api-tokens) and click "Create API token". When prompted, name the token the same name as your project, copy and save it somewhere secure, as it cannot be accessed afterwards. Enter this token into the respective section on Secoda's Jira integration setup.

Note: Multiple API tokens can link to the same Jira project

![](https://secoda-public-media-assets.s3.amazonaws.com/fbf0e0db-663e-4b87-9773-6025728db2ca.png)

#### Account Email

To find your account email, you can click on the icon in the top right corner of any Jira page, and enter it into the Account Email section of Secoda's Jira integration setup.

Note: For Jira users to appear as assignees on Secoda, you can either get an organization admin key as seen below, or have users change email visibility to "Anyone" by going through Manage Account -> Profile and Visibility -> Contact

#### Organization ID

To find your organization ID, go to [this link](https://admin.atlassian.com/), and select the workspace that you want to import. Then, the page will redirect you to `https://admin.atlassian.com/o/{your-org-id}/overview` and you can copy the ID from the link.

#### Organization Admin API key

After you have logged into your organization on `https://admin.atlassian.com/`, head to the settings tab in the navbar. From here, click API keys on the left sidebar, and create a key with a label of your choosing. On creation, it will show you your organization ID as well as the API key.

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

#### Webhook secret

A Jira webhook is needed to use Secoda's bi-directional sync between issues and questions. To register a new webhook, go to your project's main page, open the settings menu in the top right, and click on System under Jira settings.

Note: A Jira admin is needed to do this step.

<figure><img src="../../../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

On this page, scroll down all the way on the left sidebar until you see the WebHooks option.

<figure><img src="../../../.gitbook/assets/image (55).png" alt=""><figcaption></figcaption></figure>

From there, click on the Create a WebHook button near the top right, which will open the webhook creation page.&#x20;

<figure><img src="../../../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>

Now, to ensure the webhook works correctly, fill in the following fields:

* Under URL, enter the Jira webhook endpoint. If you are an on-prem customer, it will be `https://your-domain.com/api/vi/integration/jira/jira-webhook/`. If you are a cloud customer, it will be `https://api.secoda.co/integration/jira/jira-webhook/`.
* Under Secret, either generate a secret token or create one yourself. Enter this secret into the `Webhook secret` field back on the Secoda integration creation page.
* Under Events, paste the following JQL filter into the text box: `issue.property[RestApiCall] != "True"`.
* Enable the "updated" event under Issue, as well as the "created", "updated", and "deleted" events under Comment.
* Scroll to the bottom and click Create to finish registering the webhook.

<figure><img src="../../../.gitbook/assets/image (64).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (73).png" alt=""><figcaption></figcaption></figure>

Your finished webhook should look something like this:

<figure><img src="../../../.gitbook/assets/image (65).png" alt=""><figcaption></figcaption></figure>

Secoda will now automatically sync a question's title, description, assignee, priority, and status with its linked Jira issue, as well as any comments that are created, updated, or deleted.

### Connect Jira to Secoda <a href="#h_448e650cba" id="h_448e650cba"></a>

1. Open your Secoda integrations page
2. Click on "Connect Integration" in the top right
3. Select Jira from the list of integrations
4. Input your Jira credentials from **Prepare Your Jira Credentials** above. This includes the project URL, name, key, issues filter, API token, your Jira email, organization ID, organization admin API key, and webhook secret
5. Select the Teams that you wish to receive the Jira issues (appearing as Questions in Secoda)
6. Click on "Test Connection" to save the integration
7. Once integration is created, click on “Run Sync” from Connection tab to run your first extraction

Once the Jira extraction finishes running, you will be able to view all issues from your Jira project in the desired team's Question page.
