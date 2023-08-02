---
description: >-
  This page walks through the Secoda and Looker Studio integration that Secoda
  supports
---

# Looker Studio

{% content-ref url="metadata-extracted.md" %}
[metadata-extracted.md](metadata-extracted.md)
{% endcontent-ref %}

Secoda has two methods of integrating with Looker Studio: retrieving a session cookie and using Google OAuth

**NOTE:** _Using the Google OAuth method does not extract upstream (datasources) and downstream (charts) lineage due to the limitations of the Google Looker Studio API_

**NOTE:** _The session cookies expire after 12 hours and you need to re-retrieve the cookie each time you wish to run the extraction._

## Getting Started with Google OAuth <a href="#h_21e27f5a15" id="h_21e27f5a15"></a>

There are two steps to get started using Looker Studio with Secoda through Google OAuth:

1. Authorize Secoda for your Organization
2. Connect Looker Studio to Secoda

### Authorize Secoda on Google Admin

1. Sign in to your Google Admin console and navigate to [domain wide delegation](https://admin.google.com/ac/owl/domainwidedelegation).
2. In `API clients`, click **Add new**.
3. Enter the Client ID: `884425733446-7lao52vmjg9k7hovpgba2qd5b7qeo8l2.apps.googleusercontent.com`
4. Enter the following OAuth scopes:
   * `https://www.googleapis.com/auth/datastudio`
   * `https://www.googleapis.com/auth/userinfo.profile`
5. Click **Authorize**.

### Connect to Looker Studio

1. In Secoda, head to the **Integrations** page and click **New integration**
2. Select **Looker** **Studio** and click on the **OAuth** tab
3. Click the `Google OAuth 2.0` button and login using your Google account
4. Head to the **History** tab on the side bar and click **Run extraction**

## Getting Started with Session Cookies <a href="#h_21e27f5a15" id="h_21e27f5a15"></a>

There are two steps to get started using Looker Studio with Secoda through session cookies:

1. Retrieve a Looker Studio session cookie
2. Connect Looker Studio to Secoda

### Retrieve Session Cookie

_Secoda uses a series of REST APIs that Looker Studio uses for its platform, which requires a session cookie. To get a session cookie follow these steps:_

1. Login to [Looker Studio](https://datastudio.google.com) and open the developer tools by _right-clicking_ and selecting **Inspect**

<figure><img src="../../../.gitbook/assets/Group 1.png" alt=""><figcaption><p><em>Login to Looker Studio and open the developer tools by right-clicking and selecting inspect</em></p></figcaption></figure>

2\. Click on the **Network** tab and put `https://lookerstudio.google.com` in the **filter** field

<figure><img src="../../../.gitbook/assets/Group 2.png" alt=""><figcaption></figcaption></figure>

3\. Refresh the page and you should see some requests populate

4\. Click on the `getShareableList` network request and then navigate to the **Headers** tab

<figure><img src="../../../.gitbook/assets/Group 3.png" alt=""><figcaption></figcaption></figure>

5\. In the **Headers** tab, scroll down to the **Request Headers** section and copy the `cookie` header.

<figure><img src="../../../.gitbook/assets/Group 4.png" alt=""><figcaption></figcaption></figure>

### Connect to Looker Studio

_After retrieving the session cookie, you can connect Looker Studio to Secoda by following these steps:_

1. In Secoda, head to the **Integrations** page and click **New integration**
2. Select **Looker Studio**
3. Paste the cookie into the **Cookie** text input field and submit
4. Head to the **History** tab on the side bar and click **Run extraction**

### Troubleshooting

#### Invalid authentication

Looker Studio uses session cookies for authentication, which often expire. In order to resolve this error, you’ll have to generate a new session cookie and add it to your Secoda workspace. The way to do this is outlined in the Looker Studio docs, found [here](https://docs.secoda.co/integrations/google-data-studio#h\_21e27f5a15-1).
