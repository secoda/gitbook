---
description: This page walks through how to connect Secoda and Looker
---

# Connect Looker

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

Navigate to the Git tab on the Looker Integration Page and you will see your LookML projects. For each project you want to connect, click the toggle beside the project name**.**

Once the key is generate, you can select your LookML project and click **Copy public key** and head to your LookML repo in GitHub.

![](<https://secoda-public-media-assets.s3.amazonaws.com/image%20(7)%20(2).png>)

Once in your GitHub repo, click on **Settings > Deploy keys** on the sidebar.

![](https://downloads.intercomcdn.com/i/o/489714467/decf0b4194df7bc1671ed1b2/Screen+Shot+2022-03-31+at+4.31.54+PM.png)

A new key can be added by clicking on **Add deploy key** button in the top right corner.

![](https://downloads.intercomcdn.com/i/o/489718929/57a0c40bcf93056145475eda/image.png)

Set a title for your new key and then paste the key copied from Secoda into the **Key** text field.

Click **Add key**.

_Note: You **DO NOT** need to provide write access_

![](https://downloads.intercomcdn.com/i/o/489718165/18dea438e4ac144e091fc2bc/image.png)

Once the key has been added, go back into the Secoda App and click on **Run Extraction** in the top right corner to begin start the extraction process.

_Note: You **DO NOT** need to start the extraction process if you would rather wait until the next scheduled extraction._
