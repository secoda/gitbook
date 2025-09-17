# OneLogin SAML

## Steps

1.  Go to the Secoda app > Settings > Security > SAML. Copy the **ACS URL** and **Entity ID** for use in the following steps.

    <figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/834bbc4a-4653-45e8-a8e2-95af881045de.png" alt=""><figcaption><p>Secoda app > Settings > Security > SAML</p></figcaption></figure>
2. In the OneLogin console go to **Applications > Add App** and search for "SAML Custom Connector (Advanced)" and select the option.
3. Name the app `Secoda` and click **Save.**
4. In the Configuration tab set the **Audience** to the **Entity ID (Identifier)** from Step 1. Set the **Recipient**, and **ACS (Consumer)** paths to the **ACS URL** from Step 1.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/d8e24d7d-1675-4020-b218-b9db199f2b15.png" alt=""><figcaption><p>Configuration tab values. <em>These values are an example, do not copy these values.</em></p></figcaption></figure>

5. Go to the **Parameters** tab and add a new parameter by clicking the **+** button. Add the `email`, \` `firstName`, and `lastName` parameters.&#x20;

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/4a8875cb-79a1-4da3-afff-1e9c40da33f2.png" alt=""><figcaption><p><em>Check "Include in SAML assertion" for all of these parameters</em></p></figcaption></figure>

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/d2f8b68b-f242-4622-bac3-e2d1f42c277f.png" alt=""><figcaption><p><em>The Parameters page after completing the step</em></p></figcaption></figure>

6. Check **Both** for the SAML signature element field.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/df8900ac-0d27-434e-b1ac-03ae72c421ba.png" alt=""><figcaption><p><em>Both signatures must be enabled</em></p></figcaption></figure>

7. Change the SAML Signature Algorithm to **SHA-256**. Then save all of your changes. Copy the **Issuer URL** and submit that at Secoda app > Settings > Security > SAML as the **Metadata URL** with IdP Provider set to **Generic**. Save this configuration.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/71eacfc5-218c-4312-86b7-9911b332515b.png" alt=""><figcaption><p><em>Set SHA-256</em></p></figcaption></figure>

You will now be able to go to navigate to Secoda, click “Sign in with SAML”, and enter your domain to complete sign-in.
