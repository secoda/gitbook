# Google SAML

## Steps

1. Go to the Secoda app > Settings > Security > SAML. Copy the **ACS UR**L and **Entity ID** for use in the following steps.

<figure><img src="../.gitbook/assets/Screenshot 2025-04-23 at 10.43.53 AM (1).png" alt=""><figcaption><p>Secoda app > Settings > Security > SAML</p></figcaption></figure>

2. In your Google **Admin console** (at admin.google.com)...
3. Go to Menu ![""](https://storage.googleapis.com/support-kms-prod/JxKYG9DqcsormHflJJ8Z8bHuyVI5YheC0lAp)![and then](https://storage.googleapis.com/support-kms-prod/Th2Tx0uwPMOhsMPn7nRXMUo3vs6J0pto2DTn)![""](https://storage.googleapis.com/support-kms-prod/ocGtUSENh4QebLpvZcmLcNRZyaTBcolMRSyl) [Apps > Web and mobile apps](https://admin.google.com/ac/apps/unified).
4. Click **Add App**![and then](https://lh3.googleusercontent.com/QbWcYKta5vh_4-OgUeFmK-JOB0YgLLoGh69P478nE6mKdfpWQniiBabjF7FVoCVXI0g=h36)**Add custom SAML app**.
5. On the **App Details** page:
   1. Enter the name of the custom app.
   2. (Optional) Upload an **app icon**. The app icon appears on the Web and mobile apps list, on the app settings page, and in the app launcher. If you don't upload an icon, an icon is created using the first two letters of the app name.
6. Click **Continue**.
7. Copy the **SSO URL**
8. Click **Continue**.
9. In the **Service Provider Details** window, enter the appropriate URL for these 2 fields with the details from Step 1.
   * **ACS URL**
   * **Entity ID**
10. In the attributes, the following mappings **must be set**:

    <figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/1beaba43-f923-45b8-88a1-044e9e723b9f.png" alt=""><figcaption></figcaption></figure>
11. Navigate to the Secoda app > Settings > Security > SAML
12. Choose **Google** as the **SAML Provider (IdP)**
13. Paste the link from **Step 7** under **Metadata URL**
14. Save this configuration.

You will now be able to go to navigate to Secoda, click “Sign in with SAML”, and enter your domain to complete sign-in.
