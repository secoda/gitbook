---
description: >-
  On this page you will find some tips and tricks for troubleshooting common
  integration failures.
---

# Troubleshooting Guide

### GoogleDataStudio

#### Error: Invalid Authentication

GoogleDataStudio uses session cookies for authentication, which often expire. In order to resolve this error, you’ll have to generate a new session cookie and add it to your Secoda workspace. The way to do this is outlined in the Google Data Studio docs, found [here](https://docs.secoda.co/integrations/google-data-studio#h\_21e27f5a15-1). &#x20;

### Tableau

#### Error: Authorization Failed

Please re-generate an access token in Tableau and add it to your Tableau integration in Secoda.

### Snowflake

#### Error: Account Usage Not Authorized

In order to resolve this error, please run the following command:

`GRANT imported privileges on database SNOWFLAKE to ROLE SECODA;`

#### Error: Could not connect to Snowflake backend after 0 attempt(s)

This error could be the result of an incorrect Account name. For Secoda, the Snowflake Account name is the Account ID of the cluster, which maps to a substring of the Snowflake URL.

For example, if the url is https://oya5096.us-east-1.snowflakecomputing.com, the account name would be `oya5096.us-east-1`. If the url is https://abc1234.west-europe.azure.snowflakecomputing.com then, the account name would be `abc1234.west-europe.azure`. Please ensure the **entire** [Account Locator](https://docs.snowflake.com/en/user-guide/admin-account-identifier#label-account-locator) is included.

### PowerBI

#### Error: Expired Access Token

This error indicates that the access\_token has expired and needs to be refreshed. In order to refresh the token, please click on the Connected button. You will then be taken through the OAuth flow to be able to refresh the token.&#x20;

![](https://lh3.googleusercontent.com/HsWowBEhrqyIi5-8xzM1TCZr33Tfxh\_qzQx-zzUasG-fig9GSncjcPhNvT3IjmstSNUs3MpNG1LRc2R9pE9annltj22DfeWaRL8ULmD\_U5DW0yYJxwx3d6QYkcgSuPEQ0-dN4NpD31jI7kNWvL\_zKh0)

Note: It must be a PowerBI Admin in order to successfully go through the OAuth flow.

## Microsoft SQL

If you are having errors connecting your Microsoft SQL, it might be because your Host IP Address is private. In this case, you'll need to set up an SSH Tunnel so that Secoda can access the Host. Instructions for setting up an SSH Tunnel can be found [here](connecting-via-ssh-tunnel.md). &#x20;

Once a tunnel has been created, make sure to choose the SSH Tunnel in the drop down list when inputting your credentials for the integration.

![](<https://secoda-public-media-assets.s3.amazonaws.com/Screenshot%202023-05-04%20at%203.37.09%20PM.png>)
