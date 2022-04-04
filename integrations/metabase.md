# Metabase

**Getting Started**

There are three steps to get started using Metabase with Secoda:

1. Authentication
   1. Option A: Retrieve your Metabase username and password
   2. Option B: Retrieve your Session ID (SSO)
2. Retrieve your Metabase host
3. Connect Metabase to Secoda

#### **Authentication** <a href="#h_34678d4ef9" id="h_34678d4ef9"></a>

#### **Option A: Retrieve you Metabase username and password** <a href="#h_41f435a11d" id="h_41f435a11d"></a>

To get the most out of the Metabase integration, use the username and password of a Metabase admin user. The username is in an email format.

**Option B: Retrieve your Session ID (SSO)**

If you use Google, Azure, or another SSO option you must follow the steps below to retrieve your Session ID. The following video also outlines the steps to retrieve your Session ID [https://www.loom.com/share/fd3f422022b041a0a757045064a2a2d6](https://www.loom.com/share/fd3f422022b041a0a757045064a2a2d6).

1. Sign out of Metabase
2. Open up the Developer console (Right click and click "Inspect")
3. Go the the "Network" tab and check the box for "Preserve log"
4. Login to Metabase
5. Go back to the Developer console and click the `google_auth` request. Go to the "Response" tab and copy the `id`
6. Go to Secoda and add the Metabase integration and instead of a password use a session token

#### **Retrieve your host** <a href="#h_efb437bf15" id="h_efb437bf15"></a>

Your **host** is the url for your Metabase instance. For example: `https://secoda.metabaseapp.com`

#### **Connect Metabase to Secoda** <a href="#h_757a3b000b" id="h_757a3b000b"></a>

After retrieving your Metbase username, password, and host , the next step is to connect to Secoda:

1. In the Secoda App, select ‘Add Integration’ on the Integrations tab
2. Search for and select ‘Metabase’
3. Enter your Metabase username, password, OR session ID and host you retrieved above
4. Click 'Connect'

\
