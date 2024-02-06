---
description: An overview of the Looker integration with Secoda
---

# Looker

{% content-ref url="looker-metadata.md" %}
[looker-metadata.md](looker-metadata.md)
{% endcontent-ref %}

There are three steps to connect Looker with Secoda:

1. Retrieve your Looker Client ID and Client Secret
2. Retrieve your Looker host
3. Connect Looker to Secoda
4. Looker Lineage (Optional)

#### **Retrieve you Looker Client ID and Client Secret** <a href="#h_fe76e01a02" id="h_fe76e01a02"></a>

Create API3 credentials on the [Users page](https://docs.looker.com/admin-options/settings/users) in the Admin section of your Looker instance. If you’re not a Looker admin, ask your Looker admin to create the API3 credentials for you.

To create an API3 credential, click **Edit** on a user and then under **API3 Keys** click **Edit Keys**.

![](https://downloads.intercomcdn.com/i/o/378332385/8e16211840f3aa4d3a3aade6/Screen+Shot+2021-08-19+at+10.45.42+PM.png)

Create a key, and then save the **Client ID** and **Client Secret**

#### **Retrieve your host** <a href="#h_75eb18a905" id="h_75eb18a905"></a>

Your **host** is the url of your Looker instance **including** the port. For example if your site is: `https://company.cloud.looker.com` the **host** is `https://company.cloud.looker.com:443`

Sometimes an admin will have specified a custom API url. If that's the case, reach out to your admin and ask them to provide that url.

#### **Connect Looker to Secoda** <a href="#h_f136e3163c" id="h_f136e3163c"></a>

After retrieving your Looker Client ID, Client Secret, and host , the next step is to connect to Secoda:

1. In the Secoda App, select **Add Integration** on the Integrations tab
2. Search for and select Looker
3. Enter your Looker Client ID, Client Secret, and host you retrieved above
4. Click 'Connect'

#### Connect LookML repo to Secoda (Optional) <a href="#h_306dadb3b4" id="h_306dadb3b4"></a>

To get lineage between Looker and your data warehouse, Secoda will need access your GitHub repo where Looker records changes and manages file versions. Secoda will then automatically detect LookML projects connected to your Looker instance.

Navigate to the Git tab on the Looker Integration Page and you will see your LookML projects. For each project you want to connect, click the toggle beside the project name\*\*.\*\*

Once the key is generate, you can select your LookML project and click **Copy public key** and head to your LookML repo in GitHub.



<figure><img src="../../../.gitbook/assets/image (7) (2).png" alt=""><figcaption></figcaption></figure>

#### GitHub

Once in your GitHub repo, click on **Settings > Deploy keys** on the sidebar.

A new key can be added by clicking on **Add deploy key** button in the top right corner.



<figure><img src="../../../.gitbook/assets/image (49).png" alt=""><figcaption></figcaption></figure>

Set a title for your new key and then paste the key copied from Secoda into the **Key** text field.

<figure><img src="../../../.gitbook/assets/image (50).png" alt=""><figcaption></figcaption></figure>

#### GitLab

Once in your GitLab repo, click on **Settings > Deploy keys** on the sidebar.

<figure><img src="../../../.gitbook/assets/a5a7be37-f09c-4e27-8a66-2b0ca87d84ed.png" alt=""><figcaption></figcaption></figure>

Set a title for your new key and then paste the key copied from Secoda into the **Key** text field.

Click **Add key**. You **DO NOT** need to provide write access

Once the key has been added to GitHub or GitLab go back to your Looker integration in the Secoda App and go to the **Sync History** tab and click on **Run Sync** in the top right corner to start the sync process.

Note: You **DO NOT** need to start the sync process if you would rather wait until the next scheduled sync.
