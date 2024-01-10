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
6. Navigate to the Secoda app > Settings > Security > SAML
7. Choose General as the SAML Provider (IDP)
8. Paste the link from Step 5 under "Metadata URL"
9. Click Request which will alert the Secoda team of your request.

Once Secoda has completed their steps, you will be able to go to navigate to Secoda, click “Sign in with SAML”, and enter your domain to complete sign-in.
