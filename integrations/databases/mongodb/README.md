# MongoDB

### Getting started with MongoDB

There are 3 steps to get started using MongoDB with Secoda

1. Create a database user
2. Whitelist Secoda IP Address
3. Connect MongoDB to Secoda

### Requirements

* The MongoDB cluster must be running version 5.0 or above. Prior MongoDB versions do not support MongoDB's Stable API. You can read more about Stable API in the [MongoDB documentation](https://www.mongodb.com/docs/manual/reference/stable-api/)

### Creating a database user

If you are using cloud MongoDB (Atlas), you may need to create a new database user to connect to Secoda. To do that, repeat the following steps.

1. Log into your Atlas account
2.  On the sidebar go to `Security -> Database Access` and click on `ADD NEW DATABASE USER` on the top right

    ![](https://raw.githubusercontent.com/secoda/gitbook/master/.gitbook/assets/Screenshot%202023-08-18%20at%2011.51.36%20AM.png)
3.  Use the password authentication method and save both the user name and password. The role given to the database user can be `Only read any database` under `built-in role` but it may need to be updated at a later date when Secoda comes out with new features

    ![](https://raw.githubusercontent.com/secoda/gitbook/master/.gitbook/assets/Screenshot%202023-08-18%20at%2012.46.43%20PM.png)

### Whitelist Secoda IP Address

Once you have created the new database user, you need to add Secoda's IP address to the allowlist. To do that, repeat the following steps.

1. Log into your Atlas Account
2.  On the side, navigate to `Security -> Network Access` and click on `ADD IP ADDRESS` on the top right

    ![](https://raw.githubusercontent.com/secoda/gitbook/master/.gitbook/assets/Screenshot%202023-08-18%20at%2012.32.29%20PM.png)
3. Add `35.175.75.15/32` and `34.230.160.245/32`

### Connect MongoDB to Secoda

To connect to MongoDB to Secoda, repeat the following steps.

1. In the Secoda App, select "Add Integration" on the Integrations tab
2. Click on `MongoDB`
3.  Enter the URI, cluster name, and the team the integration will be associated with

    ![](https://raw.githubusercontent.com/secoda/gitbook/master/.gitbook/assets/Screenshot%202023-08-18%20at%2012.39.43%20PM%20\(3\).png)

    1.  The URI can be found by navigating to `Deployment -> Database` on Atlas and clicking on the cluster you are trying to connect to

        ![](https://raw.githubusercontent.com/secoda/gitbook/master/.gitbook/assets/Screenshot%202023-08-18%20at%2012.51.56%20PM%20\(1\).png)
    2.  Click on `Driver` to see a sample URI of the cluster

        ![](https://raw.githubusercontent.com/secoda/gitbook/master/.gitbook/assets/Screenshot%202023-08-18%20at%2012.53.29%20PM%20\(1\).png)
    3.  Copy and paste the `connection string` to the URI field, replacing `<username>` and `<password>` with the username and password that was used to create the database user in step 1

        ![](https://raw.githubusercontent.com/secoda/gitbook/master/.gitbook/assets/Screenshot%202023-08-18%20at%2012.37.27%20PM%20\(1\).png)
4.  Once successfully connected, choose the databases and collections you want to extract to Secoda

    ![](https://raw.githubusercontent.com/secoda/gitbook/master/.gitbook/assets/Screenshot%202023-08-18%20at%2012.40.30%20PM.png)
5. Run the initial extraction

### Data type conversion

{% content-ref url="data-type-conversion.md" %}
[data-type-conversion.md](data-type-conversion.md)
{% endcontent-ref %}
