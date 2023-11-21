---
description: An overview of the MongoDB integration with Secoda
---

# MongoDB

{% content-ref url="data-type-conversion.md" %}
[data-type-conversion.md](data-type-conversion.md)
{% endcontent-ref %}

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

    ![](https://secoda-public-media-assets.s3.amazonaws.com/5c4fc0e4-ea34-4fc5-a862-a54b8b6f3043.png)
3.  Use the password authentication method and save both the user name and password. The role given to the database user can be `Only read any database` under `built-in role` but it may need to be updated at a later date when Secoda comes out with new features

    ![](https://secoda-public-media-assets.s3.amazonaws.com/01d7bc51-e61e-4fa3-bc23-b2c1dc36a5ee.png)

### Whitelist Secoda IP Address

Once you have created the new database user, you need to add Secoda's IP address to the allowlist. To do that, repeat the following steps.

1. Log into your Atlas Account
2.  On the side, navigate to `Security -> Network Access` and click on `ADD IP ADDRESS` on the top right

    ![](https://secoda-public-media-assets.s3.amazonaws.com/5efdc668-7d49-48fb-9286-e2c96e75cc30.png)
3. Add `35.175.75.15/32` and `34.230.160.245/32`

### Connect MongoDB to Secoda

To connect to MongoDB to Secoda, repeat the following steps.

1. In the Secoda App, select "Add Integration" on the Integrations tab
2. Click on `MongoDB`
3.  Enter the URI, cluster name, and the team the integration will be associated with

    ![](https://secoda-public-media-assets.s3.amazonaws.com/c95da3dc-78e8-4774-a404-8e827982e0b2.png)

    1.  The URI can be found by navigating to `Deployment -> Database` on Atlas and clicking on the cluster you are trying to connect to

        ![](https://secoda-public-media-assets.s3.amazonaws.com/77ab7a8c-417c-465c-a19d-82f6cd8ff8ce.png)
    2.  Click on `Driver` to see a sample URI of the cluster

        ![](https://secoda-public-media-assets.s3.amazonaws.com/90dedcff-64af-4a13-8660-4037bb387d31.png)
    3.  Copy and paste the `connection string` to the URI field, replacing `<username>` and `<password>` with the username and password that was used to create the database user in step 1

        ![](https://secoda-public-media-assets.s3.amazonaws.com/39361fa5-1bea-4858-a5f2-57fc13ab064d.png)
4.  Once successfully connected, choose the databases and collections you want to extract to Secoda

    ![](<../../../.gitbook/assets/Screen Shot 2023-11-21 at 4.19.53 PM.png>)
5. Run the initial extraction

### Data type conversion
