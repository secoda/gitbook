# MongoDB

### Getting started with MongoDB

There are 3 steps to get started using MongoDB with Secoda

1. Create a database user
2. Whitelist Secoda IP Address
3. Connect MongoDB to Secoda

### Creating a database user

If you are using cloud MongoDB (Atlas), you may need to create a new database user to connect to Secoda. To do that, repeat the following steps.

1. Log into your Atlas account
2.  On the sidebar go to `Security -> Database Access` and click on `ADD NEW DATABASE USER` on the top right&#x20;



    <figure><img src="../../../.gitbook/assets/Screenshot 2023-08-18 at 11.51.36 AM.png" alt=""><figcaption><p>Navigating to Database Access and adding new database user</p></figcaption></figure>
3.  Use the password authentication method and save both the user name and password. The role given to the database user can be `Only read any database` under `built-in role` but it may need to be updated at a later date when Secoda comes out with new features

    <figure><img src="../../../.gitbook/assets/Screenshot 2023-08-18 at 12.46.43 PM.png" alt=""><figcaption><p>Form to create new database user</p></figcaption></figure>



### Whitelist Secoda IP Address

Once you have created the new database user, you need to add Secoda's IP address to the allowlist. To do that, repeat the following steps.

1. Log into your Atlas Account
2.  On the side, navigate to `Security -> Network Access` and click on `ADD IP ADDRESS` on the top right

    <figure><img src="../../../.gitbook/assets/Screenshot 2023-08-18 at 12.32.29 PM.png" alt=""><figcaption><p>Network access page</p></figcaption></figure>
3. Add `35.175.75.15/32` and `34.230.160.245/32`

### Connect MongoDB to Secoda

To connect to MongoDB to Secoda, repeat the following steps.

1. In the Secoda App, select "Add Integration" on the Integrations tab
2. Click on `MongoDB`
3.  Enter the URI, cluster name, and the team the integration will be associated with&#x20;

    <figure><img src="../../../.gitbook/assets/Screenshot 2023-08-18 at 12.39.43 PM (3).png" alt=""><figcaption><p>MongoDB integration page</p></figcaption></figure>

    1.  The URI can be found by navigating to `Deployment -> Database` on Atlas and clicking on the cluster you are trying to connect to

        <figure><img src="../../../.gitbook/assets/Screenshot 2023-08-18 at 12.51.56 PM (1).png" alt=""><figcaption><p>Navigating to Connect button</p></figcaption></figure>
    2.  Click on `Driver` to see a sample URI of the cluster

        <figure><img src="../../../.gitbook/assets/Screenshot 2023-08-18 at 12.53.29 PM (1).png" alt=""><figcaption><p>Driver option</p></figcaption></figure>
    3.  Copy and paste the `connection string` to the URI field, replacing `<username>` and `<password>` with the username and password that was used to create the database user in step 1

        <figure><img src="../../../.gitbook/assets/Screenshot 2023-08-18 at 12.37.27 PM (1).png" alt=""><figcaption><p>Sample connection string</p></figcaption></figure>
4.  Once successfully connected, choose the databases and collections you want to extract to Secoda

    <figure><img src="../../../.gitbook/assets/Screenshot 2023-08-18 at 12.40.30 PM.png" alt=""><figcaption><p>Sample database and collections</p></figcaption></figure>
5. Run the initial extraction



### Data type conversion

{% content-ref url="data-type-conversion.md" %}
[data-type-conversion.md](data-type-conversion.md)
{% endcontent-ref %}
