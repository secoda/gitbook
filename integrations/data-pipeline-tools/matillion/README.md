---
description: An overview of the Matillion integration with Secoda
---

# Matillion

{% content-ref url="matillion-metadata-extracted.md" %}
[matillion-metadata-extracted.md](matillion-metadata-extracted.md)
{% endcontent-ref %}

## Getting Started with Matillion

There are four steps to connect your Matillion ETL instance with Secoda:

1. Retrieve your Matillion ETL host domain
2. Retrieve Username and Password credentials
3. Retrieve the Project name and Group name you want to connect to
4. Connect Matillion to Secoda

#### Retrieve the host domain

The host domain is the url through which you access Matillion ETL on your browser. For example, if you login to your Matillion ETL instance at "https://12.345.678.901/Login", then your host domain is "https://12.345.678.901/".\


#### Retrieve the access credentials

The same username and password used to login to your Matillion instance can be used to connect with Secoda.

(Optional)&#x20;

Since these credentials will be accessible to organization users who have access to your Matillion integration, we recommend creating a new username and password specifically for the integration.

#### Retrieve the project name and group name

In your Matillion ETL instance, navigate to your desired resources, in the URL, the group name is the first section after the host domain, and the project name is the second.\
For example, if you have the resource URL: "https://12.345.678.901/#MyGroup/MyProject/Version/example\_resource", then set your group to MyGroup and your project to MyProject.

#### Connect Matillion to Secoda

After retrieving the host domain and user credentials, the next step is to connect to Secoda:

1. In the Secoda App, select **Add Integration** on the integration tab
2. Search for and select Matillion
3. Enter your Matillion host domain, username, and password, as well as the group name and project name you want to link.
4. Click connect
