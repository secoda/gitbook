---
description: An overview of the Retool integration with Secoda
---

# Retool



{% content-ref url="metadata-extracted.md" %}
[metadata-extracted.md](metadata-extracted.md)
{% endcontent-ref %}

## Getting Started with Session Cookies <a href="#h_21e27f5a15" id="h_21e27f5a15"></a>

There are two steps to get started using Retool with Secoda through session cookies:

1. Retrieve a Retool session cookie
2. Connect Retool to Secoda

### Retrieve Session Cookie

_Secoda uses a series of REST APIs that Retool uses for its platform, which requires a session cookie. To get a session cookie follow these steps:_

1. Login to your Retool workspace and open developer tools by right-clicking and selecting **Inspect**

![](https://secoda-public-media-assets.s3.amazonaws.com/image%20\(3\).png)

2. Click on the **Network** tab and enter `url:<yourworkspace>.retool.com` in the filter head

![](https://secoda-public-media-assets.s3.amazonaws.com/image%20\(2\)%20\(1\).png)

3. Refresh the page and you should see some requests populate
4. Click on `user` network request, navigate to **Headers** tab, scroll down to the **Request Headers** section and copy the `cookie` header.

![](https://secoda-public-media-assets.s3.amazonaws.com/image%20\(1\)%20\(1\)%20\(1\)%20\(1\).png)

### Connect to Retool

_After retrieving the session cookie, you can connect Retool to Secoda by following these steps:_

1. In Secoda, head to the **Integrations** page and click **New integration**
2. Select **Retool**
3. Paste the cookie into the **Cookie** text input field
4. Click **Connect**
