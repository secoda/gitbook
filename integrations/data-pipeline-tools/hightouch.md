---
description: >-
  This page walks through the Secoda and Hightouch integration that Secoda
  supports
---

# Hightouch Integration

## **Getting Started with Hightouch** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

There are three steps to get started using Hightouch with Secoda:

1. Retrieve a Hightouch session cookie
2. Connect Hightouch to Secoda

#### Retrieve a Hightouch session cookie <a href="#h_088224f7c9" id="h_088224f7c9"></a>

Secoda uses the Hightouch GraphQL API, which requires a session cookie. To get a session cookie follow these steps:

1\. Open up [https://app.hightouch.io](https://app.hightouch.io) and login

2\. Open up the developer tools by _right clicking_ and selecting **Inspect**

![](https://downloads.intercomcdn.com/i/o/446146255/56f44332f61ede10942b19e3/image.png)

3\. Click the **Network** tab

![](https://downloads.intercomcdn.com/i/o/446146891/30626a8d04b80620740149ce/image.png)

4\. Navigate to the "Syncs" page (refresh if you're currently on this page)

5\. Click on the first `graphql` network request

![](https://downloads.intercomcdn.com/i/o/446148444/54b2830bff8c65639f302730/image.png)

6\. Navigate to the **Headers** tab

![](https://downloads.intercomcdn.com/i/o/446148662/66635763842871aab522600e/image.png)

7\. Copy and save the **set-cookie** header to somewhere you can retrieve later. This is the "Cookie" parameter that Secoda requires

![](https://downloads.intercomcdn.com/i/o/446148976/78fdf9b19fef88249553d0f6/image.png)

#### **Connect Hightouch to Secoda** <a href="#h_276d2819e7" id="h_276d2819e7"></a>

After retrieving the cookie, the next step is to connect Secoda:

1. In the Secoda App, select ‘Add Integration’ on the Integrations tab
2. Search for and select ‘Hightouch’
3. Enter your Cookie. This information is kept encrypted.
4. Click 'Connect'
5. After the extraction is complete your Hightouch Syncs will be in Secoda\\
