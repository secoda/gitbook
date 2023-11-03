# OneLogin SAML

## Steps

{% hint style="info" %}
If you're self-hosted, replace https://app.secoda.co with your domain.
{% endhint %}

1. In the OneLogin console go to **Applications > Add App** and search for "SAML Custom Connector (Advanced)" and select the option.
2. Name the app `Secoda` and click **Save.**
3. In the **Configuration** tab set the ACS (Consumer) URL Validator **and** ACS (Consumer) URL to your personalized endpoint: `https://app.secoda.co/api/v1/auth/saml/mycompany+com/acs/` Click **Save.**
4. Go to the **Parameters** tab and add a new parameter by clicking the **+** button.
   1. Put email as the Field name and click Enter
   2. Select your email attribute as the the Value
   3. Click **Save**
5. Go to the **SSO** tab and copy the **Issuer URL.**&#x20;
6. Provide the URL from **step 3** and the link from **step 5** to the Secoda team via the support@secoda.co email with the Subject "Secoda SAML Setup".
