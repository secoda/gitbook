# OneLogin SAML

## Steps

{% hint style="info" %}
If you're self-hosted, replace https://app.secoda.co with your domain.
{% endhint %}

1. In the OneLogin console go to **Applications > Add App** and search for "SAML Custom Connector (Advanced)" and select the option.
2. Name the app `Secoda` and click **Save.**
3. In the Configuration tab set the Audience, Recipient, ACS, and ACS consumer paths to the endpoints provided by the [https://app.secoda.co/settings/security](https://app.secoda.co/settings/security) page.&#x20;

<figure><img src="../.gitbook/assets/Group 6.png" alt=""><figcaption><p>Configuration tab values. <em>These values are an example, do not copy these values.</em></p></figcaption></figure>

4. Go to the **Parameters** tab and add a new parameter by clicking the **+** button. Add the `email`, \` `firstName`, and `lastName` parameters.&#x20;

<figure><img src="../.gitbook/assets/Group 9.png" alt=""><figcaption><p><em>Check "Include in SAML assertion" for all of these parameters</em></p></figcaption></figure>

<figure><img src="../.gitbook/assets/Group 5 (1).png" alt=""><figcaption><p><em>The Parameters page after completing the step</em></p></figcaption></figure>

5. Check **"Both"** for the SAML signature element field.

<figure><img src="../.gitbook/assets/Group 7.png" alt=""><figcaption><p><em>Both signatures must be enabled</em></p></figcaption></figure>

6. Change the SAML Signature Algorithm to **SHA-256**. Then save all of your changes. Copy the **Issuer URL** and submit that on [**https://app.secoda.co/settings/security**](https://app.secoda.co/settings/security) as the **Metadata URL** with SAML Provider **Generic**.



Once the Secoda team approves your request, you will be able to go to navigate to Secoda, click “Sign in with SAML”, and enter your domain to complete sign-in.
