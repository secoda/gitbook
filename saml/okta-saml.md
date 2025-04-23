# Okta SAML

## Steps:

1. Go to the Secoda app > Settings > Security > SAML. Copy the **ACS UR**L and **Entity ID** for use in the following steps.

<figure><img src="../.gitbook/assets/Screenshot 2025-04-23 at 10.43.53 AM.png" alt=""><figcaption><p>Settings > Security tab</p></figcaption></figure>

1. In the Okta console: click the button “Create App Integration” (SAML2.0)
2. Name the app `Secoda`
3. Set the **SSO URL** and **Audience** to your personalized **ACS URL** copied from above.
4.  Add the following attribute statements. While Okta marks them as optional, this step is _required_.

    ![](https://imagedelivery.net/28-eDrK8lEif6_ED0iMQeg/f1c1ee1d-d138-4962-0c4c-b669b0e33100/public)
5. Click Next.
6. Click Finish. Assign users to this application if you want them to be able to sign in.
7. Go to the Sign On tab and expand the SAML 2.0 box to see the Metadata details. Copy the **Metadata URL**
8. Navigate to the Secoda app > Settings > Security > SAML
9. Choose Okta as the **SAML Provider (IdP)**
10. Paste the link from Step 7 under **Metadata URL**



Now you can logout, click “Sign in with SAML”, and enter your domain to complete sign-in.

{% hint style="info" %}
If you want to add multiple domains to Okta reach out to Secoda at support@secoda.co for assistance.&#x20;
{% endhint %}
