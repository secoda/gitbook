# Okta SAML

## Steps:

1. We will assume your company domain is [company.com](http://company.com) and the domain where Secoda is hosted is [app.secoda.co](http://app.secoda.co) ([secoda.company.com](http://secoda.company.com), if on-premise).
2. In the Okta console: click the button “Create App Integration” (SAML2.0)
3. Name the app `Secoda`
4. Set the SSO URL **and** Audience to your personalized endpoint: `https://app.secoda.co/api/v1/auth/saml/company+com/acs/`
5. Add the following attribute statements. While Okta says Optional, this step is Required.
   *   Image

       ![](https://imagedelivery.net/28-eDrK8lEif6\_ED0iMQeg/f1c1ee1d-d138-4962-0c4c-b669b0e33100/public)
6. Click Next.
7. Click Finish. Assign users to this application if you want them to be able to sign in.
8. Go to the SSO tab and click “View IDP metadata” on the _active SHA-2_ certificate. Copy that URL.
   *   Image

       ![](https://imagedelivery.net/28-eDrK8lEif6\_ED0iMQeg/7435f5a6-d04f-4996-11d4-07927251b200/public)
9. Provide the URL from **step 4** and the link from **step 8** to the Secoda team.
