---
description: An overview of the SQL Server Reporting Services integration with Secoda
---

# SQL Server Reporting Services

{% content-ref url="sql-server-reporting-services-metadata-extracted.md" %}
[sql-server-reporting-services-metadata-extracted.md](sql-server-reporting-services-metadata-extracted.md)
{% endcontent-ref %}

## Getting Started with SQL Server Reporting Services

There are 3 steps to connect SQL Server Reporting Services with Secoda:

1. Retrieve the host domain for your SQL Server Reporting Services workspace&#x20;
2. Retrieve an account username and password with access to the workspace
3. Connect SSRS to Secoda

**Retrieve the host domain**

To retrieve the host domain, navigate to the home page of your report services workspace. Take the part of the URL that does not change when navigating around the workspace as your host domain.

For example, if the page is on the 'browse' tab and the link is "https://example.secoda/reports/browse", then the host domain is "https://example.secoda/reports" in this case.

**Retrieve account credentials**

Your username and password is required to connect SQL Server Reporting Services to Secoda. Note that the display name in the top right of the home page may not be the username for your account. If you unsure of your username, it can be found by following these steps:

1. Enter your host domain into your browser, and add the following after it “/api/v2.0/me?%24select=Username”
2. To the right of the “username” field, your account username is found

**Connect SQL Server Reporting Services**

After retrieving the host domain and user credentials, the next step is to connect to Secoda:

1. In the Secoda App, select "Connect Integration" on the [Integrations page](https://app.secoda.co/integrations)
2. Search for and select SQL Server Report Services
3. Enter your host, username and password you retrieved
4. Click connect
