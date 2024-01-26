# SingleStore

Getting Started with SingleStore

To integrate SingleStore with Secoda, follow these three steps:

1. Create a SingleStore database user
2. Whitelist Secoda IP Addresses
3. Connect SingleStore to Secoda

{% hint style="info" %}
Please ensure the workspace in Singlestore is not suspended. Secoda is unable to connect to a suspended workspace. To prevent your Singlestore workspace from suspending due to inactivity, disable the auto-suspend setting in Singlestore.
{% endhint %}

**Create a Database User**

The username and password you’ve already created for your cluster is your admin password, which you should keep for your own usage. For Secoda, and any other 3rd-parties, it is best to create distinct users.

To create a new user, you’ll need to log into the SingleStore database directly and run the following SQL commands. You

```
-- Create a user named "secoda" with appropriate privileges that Secoda will use when connecting to your SingleStore database. 
CREATE USER 'secoda'@'%' IDENTIFIED BY '<enter password here>'
GRANT SELECT, PROCESS, SHOW METADATA ON *.* TO 'secoda'@'%';
```

When connecting to SingleStore in Secoda, use the username/password you’ve created here instead of your admin account.

**Retrieve the host domain**

To retrieve the host domain and port number, sign into SingleStore portal and navigate on the sidebar to `Cloud > Group > Workspaces`.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/a97af923-076b-4e03-b2cb-fab280af89d7.png" alt=""><figcaption><p>Navigate on the sidebar to <code>Cloud > Group > Workspaces</code></p></figcaption></figure>

Click `Connect` on the workspace you want to connect

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/2d56193b-daf6-4ad7-a2c3-33b1879bd964.png" alt=""><figcaption><p>Click <code>Connect</code> on the workspace you want to connect</p></figcaption></figure>

Then you can navigate to `SQL IDE` tab to see the host and port.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/1653ed33-3c2c-4670-8bff-f1964635b506.png" alt=""><figcaption><p>Navigate to <code>SQL IDE</code> tab</p></figcaption></figure>

**Connect SingleStore to Secoda**

After creating a SingleStore user, the next step is to connect Secoda:

1. In the Secoda App, select ‘Add Integration’ on the Integrations tab
2. Search for and select SingleStore
3. Enter your SingleStore credentials (host domain, port, username, password)
4. Click 'Connect'

#### **Security** <a href="#h_fb194eceed" id="h_fb194eceed"></a>

VPCs keep servers inaccessible to traffic from the internet. With VPC, you’re able to designate specific web servers access to your servers. In this case, you will be whitelisting the Secoda IPs to read from your data warehouse.

Allow Secoda to read into your SingleStore database using the [Secoda IP address](../../../faq.md#what-are-the-ip-addresses-for-secoda).
