# ThoughtSpot

There are four steps to connect ThoughtSpot with Secoda:

1. Retrieve your ThoughtSpot host
2. Retrieve your ThoughtSpot username and password
3. Retrieve your ThoughtSpot Organization Id (Optional)
4. Connect Looker to Secoda

#### **Retrieve your host** <a href="#h_75eb18a905" id="h_75eb18a905"></a>

Your **host** is the url of your ThoughtSpot instance **not including** the port. For example if your site is: `https://my2.thoughtspot.cloud/#/` the **host** is `my2.thoughtspot.cloud`



**Retrieve your username and password**

This will be the account that you want to use to connect to Secoda. It is recommended that you create a new account for Secoda in ThoughtSpot and connect to Secoda using the corresponding credentials.&#x20;



**Note:** The ThoughtSpot integration requires the account to have `ADMINISTRATION` permissions in ThoughtSpot to be able to grab all the metadata.



**Retrieve your ThoughtSpot Organization Id (Optional)**

If you are part of multiple ThoughtSpot organizations, you can specify which organization you want to pull the metadata from by entering the organization Id. This is available in the admin Tab under `Orgs`

#### &#x20;<a href="#h_f136e3163c" id="h_f136e3163c"></a>

#### **Connect ThoughtSpot to Secoda** <a href="#h_f136e3163c" id="h_f136e3163c"></a>

After retrieving your Looker Client ID, Client Secret, and host , the next step is to connect to Secoda:

1. In the Secoda App, select **Add Integration** on the Integrations tab
2. Search for and select ThoughtSpot
3. Enter your username, password, host, and organization ID (Optional) you retrieved above
4. Click 'Connect'
