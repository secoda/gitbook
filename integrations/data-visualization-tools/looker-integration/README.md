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

{% hint style="info" %}
Secoda will automatically detect LookML projects connected to your Looker instance.&#x20;
{% endhint %}

