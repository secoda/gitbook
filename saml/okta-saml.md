# Okta SAML

## Steps:

1.  Go to the Secoda app > Settings > Security > SAML. Copy the **ACS URL** and **Entity ID** for use in the following steps.

    <figure><img src="../.gitbook/assets/Screenshot 2025-04-23 at 10.43.53 AM (7).png" alt=""><figcaption><p>Secoda app > Settings > Security > SAML</p></figcaption></figure>
2. In the Okta console: click the button “Create App Integration” (SAML2.0)
3. Name the app `Secoda`
4. Set the **SSO URL** and **Audience** to your personalized **ACS URL** copied from above.
5.  Add the following attribute statements. While Okta marks them as optional, this step is _required_.

    ![](https://imagedelivery.net/28-eDrK8lEif6_ED0iMQeg/f1c1ee1d-d138-4962-0c4c-b669b0e33100/public)
6. Click Next.
7. Click Finish. Assign users to this application if you want them to be able to sign in.
8. Go to the Sign On tab and expand the SAML 2.0 box to see the Metadata details. Copy the **Metadata URL**
9. Navigate to the Secoda app > Settings > Security > SAML
10. Choose Okta as the **SAML Provider (IdP)**
11. Paste the link from Step 8 under **Metadata URL**. Save this configuration.



Now you can logout, click “Sign in with SAML”, and enter your domain to complete sign-in.
