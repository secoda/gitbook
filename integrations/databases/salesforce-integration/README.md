# Salesforce Integration

### Getting Started with Salesforce

There are 4 steps to get started using Salesforce with Secoda:

1. Pick a method to connect to Salesforce, there are 2 options:
   1. Use your Salesforce account's username and password (tab **Password**)
   2. Use Salesforce OAuth (tab **OAuth**)
2. Setup User Permissions, Connected App, and retrieve Consumer Key and Consumer Secret
3. Retrieve your host
4. Connect Salesforce to Secoda

### Setup User Permissions, Connected App, and retrieve Consumer Key and Consumer Secret

Make sure the profile associated with your user has API Enabled permission. You can verify this:

1. Go to Setup > Administration > Users > Users and click your user's profile

![](https://secoda-public-media-assets.s3.amazonaws.com/image%20\(3\)%20\(1\).png)

2. Make sure `API Enabled` is ticked

![](https://secoda-public-media-assets.s3.amazonaws.com/image%20\(1\)%20\(4\).png)

If you haven't already, create a new Salesforce Connected App:

1. Go to Setup > Platform Tools > Apps > App Manager and click New Connected App

![](https://secoda-public-media-assets.s3.amazonaws.com/image%20\(6\)%20\(3\).png)

2. Follow the instruction below to complete the form to create new Connected App (or modify your existing one)
3. If you're using Username & Password flow (tab **Password**):
   * Tick `Enable OAuth Settings`
   * For `Oauth Scopes`, we need at least `Manage user data via APIs (api)`
   * For Callback URL, you can use `http://localhost`

![](https://secoda-public-media-assets.s3.amazonaws.com/image%20\(5\).png)

4. If you're using Salesforce OAuth flow (tab **OAuth**):
   * For Callback URL, enter `https://app.secoda.co/api/v1/oauth/from_oauth/` (or `https://<your-app>.secoda.co/api/v1/oauth/from_oauth/`)
   * For `Oauth Scopes`, we need at least `Manage user data via APIs (api)`and `Perform requests at any time (refresh_token, offline_access)`
   * Tick `Enable OAuth Settings` and `Enable Authorization and Credentials Flow`

![](https://secoda-public-media-assets.s3.amazonaws.com/image%20\(3\)%20\(2\).png)

5. In the next step, Go to API (Enable OAuth Settings) > Manage Consumer Details to **retrieve your Consumer Key and Consumer Secret**.
   1. Add Secoda's IP to Trusted IP Range for OAuth Web Server Flow. If not, see step 6.2 below to relax IP restriction.

![](https://secoda-public-media-assets.s3.amazonaws.com/image%20\(16\)%20\(1\).png)

6. Go to Setup > Platform Tools > Apps > Connected Apps > Manage Connected Apps and click Edit next to your App.
   1. If you're using Salesforce OAuth flow (**OAuth** tab), set Refresh Token Policy to `Refresh Token is valid until revoked`
   2. If you want to relax IP restrictions. Select `Relax IP restrictions` for IP Relaxation.

![](https://secoda-public-media-assets.s3.amazonaws.com/image%20\(12\).png)

### Retrieve your host

Your **host** is the url for your Salesforce instance. For example: `https://secoda.my.salesforce.com`

### **Connect Salesforce to Secoda** <a href="#h_757a3b000b" id="h_757a3b000b"></a>

After retrieving your Salesforce host, Consumer Key and Consumer Secret, the next step is to connect to Secoda:

1. In the Secoda App, select "Add Integration" on the Integrations tab
2. Search for and select "Salesforce", and select the either "Password" or "Oauth" tab
3. Enter your Salesforce host, Consumer Key, and Consumer Secret
4. If you selected "Password" tab, enter your Salesforce account's username and password
5. Click 'Connect'
