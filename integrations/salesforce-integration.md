# Salesforce Integration

### Getting Started with Salesforce

There are 4 steps to get started using Salesforce with Secoda:

1. Retrieve your Salesforce username and password
2. Setup User Permissions, Connected App, and retrieve Consumer Key and Consumer Secret
3. Retrieve your host&#x20;
4. Connect Salesforce to Secoda

### Retrieve your Salesforce username and password

These are your Salesforce account's **username** and **password**

### Setup User Permissions, Connected App, and retrieve Consumer Key and Consumer Secret

Make sure the profile associated with your user has API Enabled permission. You can verify this:

1. Go to Setup > Administration > Users > Users and click your user's profile&#x20;

![](<../.gitbook/assets/image (3).png>)

2. Make sure `API Enabled` is ticked

![](<../.gitbook/assets/image (1).png>)

If you haven't already, create a new Salesforce Connected App:

1. Go to Setup > Platform Tools > Apps > App Manager and click New Connected App

![](<../.gitbook/assets/image (6).png>)

2. Complete the form to create new Connected App
   * Make sure to tick `Enable OAuth Settings` and give appropriate `Oauth Scopes`. We'd recommend selecting `Full access (full)`
   * For Callback URL, you can use `http://localhost`

![](<../.gitbook/assets/image.png>)

3. In the next step, Go to API (Enable OAuth Settings) > Manage Consumer Details to **retrieve your Consumer Key and Consumer Secret**. You will need to store them in a secure place.
   * Add Secoda's IP to Trusted IP Range for OAuth Web Server Flow. If not, follow step 4 below to relax IP restriction.
   * _Note that this page is not available to revisit later if you're using Lighting Experience mode. To revisit this page, go to classic view Setup > Build > Create > Apps > Connected Apps and click Manage._&#x20;

![](<../.gitbook/assets/image (16).png>)

4. If you want to relax IP restrictions, Go to Setup > Platform Tools > Apps > Connected Apps > Manage Connected Apps and click Edit next to your App. Next, select `Relax IP restrictions` for IP Relaxation.&#x20;

![](<../.gitbook/assets/image (2).png>)

### Retrieve your host

Your **host** is the url for your Salesforce instance. For example: `https://secoda.my.salesforce.com`

### **Connect Metabase to Secoda** <a href="#h_757a3b000b" id="h_757a3b000b"></a>

After retrieving your Salesforce host, username, password, Consumer Key and Consumer Secret, the next step is to connect to Secoda:

1. In the Secoda App, select "Add Integration" on the Integrations tab
2. Search for and select "Salesforce"
3. Enter your Salesforce host, username, password, Consumer Key, and Consumer Secret
4. Click 'Connect'
