# OneLogin SAML

## Steps

1. We will assume you sign in to Secoda with john@\<MYCOMPANY.COM> and the domain where Secoda is hosted is \<APP.SECODA.CO>. This may be \<MYCOMPANY.SECODA.CO> or different for on-premise.
2. In the OneLogin console go to **Applications > Add App** and search for "SAML Custom Connector (Advanced)" and select the option.
3. Name the app `Secoda` and click **Save.**
4. In the **Configuration** tab set the ACS (Consumer) URL Validator **and** ACS (Consumer) URL to your personalized endpoint: `https://app.secoda.co/api/v1/auth/saml/mycompany+com/acs/` for the first example or `https://mycompany.secoda.co/api/v1/auth/saml/mycompany+com/acs/` for the latter example. Click **Save.**
5. Go to the **SSO** tab and copy the **Issuer URL.**&#x20;
6. Provide the URL from **step 4** and the link from **step 5** to the Secoda team via the support@secoda.co email with the Subject "Secoda SAML Setup".
