# Okta SAML

## Steps:

{% hint style="info" %}
If you're self-hosted, replace https://app.secoda.co with your domain.
{% endhint %}

1. In the Okta console: click the button “Create App Integration” (SAML2.0)
2. Name the app `Secoda`
3. Set the SSO URL **and** Audience to your personalized endpoint: `https://app.secoda.co/api/v1/auth/saml/mycompany+com/acs/`
4. Add the following attribute statements. While Okta says Optional, this step is Required.
   *   Image

       ![](https://imagedelivery.net/28-eDrK8lEif6\_ED0iMQeg/f1c1ee1d-d138-4962-0c4c-b669b0e33100/public)
5. Click Next.
6. Click Finish. Assign users to this application if you want them to be able to sign in.
7. Go to the SSO tab and click “View IDP metadata” on the _active SHA-2_ certificate. Copy that URL.
   *   Image

       ![](https://imagedelivery.net/28-eDrK8lEif6\_ED0iMQeg/7435f5a6-d04f-4996-11d4-07927251b200/public)
8. Provide the URL from **step 3** and the link from **step 7** to the Secoda team.
