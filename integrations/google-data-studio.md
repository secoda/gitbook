# Google Data Studio

### Getting Started <a href="#h_21e27f5a15" id="h_21e27f5a15"></a>

There are three steps to get started using Google Data Studio with Secoda:

1. Retrieve a Google Data Studio session cookie
2. Connect Google Data Studio to Secoda

#### Retrieving a Google Data Studio Session Cookie

_Secoda uses a series of REST APIs that Google Data Studio uses for its platform, which requires a session cookie. To get a session cookie follow these steps:_

1. Login to [Google Data Studio](https://datastudio.google.com) and open the developer tools by _right-clicking_ and selecting **Inspect**

![Login to Google Data Studio and open the developer tools by right-clicking and selecting Inspect](<../.gitbook/assets/image (6).png>)

&#x20; 2\.  Click on the **Network** tab and put `https://datastudio.google.com` in the **filter** field

![](<../.gitbook/assets/image (4) (1).png>)

&#x20; 3\.  Refresh the page and you should see some requests populate

&#x20; 4\.  Click on the `getShareableList` network request and then navigate to the **Headers** tab

![](<../.gitbook/assets/image (2) (1) (1).png>)

&#x20; 5\.  In the **Headers** tab, scroll down to the **Request Headers** section and copy the `cookie` header.

![](<../.gitbook/assets/image (5) (1).png>)

#### Connecting Google Data Studio to Secoda

&#x20;_After retrieving the session cookie, you can connect Google Data Studio to Secoda by following these steps:_

1. In Secoda, head to the **Integrations** page and click **New integration**
2. Select **Google Data Studio**
3. Paste the cookie into the **Cookie** text input field and submit
4. Head to the **History** tab on the side bar and click **Run extraction**
