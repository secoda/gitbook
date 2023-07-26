# Google SAML

Set up your own custom SAML app

1. In your Google **Admin console** (at admin.google.com)...
2. Go to Menu ![""](https://storage.googleapis.com/support-kms-prod/JxKYG9DqcsormHflJJ8Z8bHuyVI5YheC0lAp)![and then](https://storage.googleapis.com/support-kms-prod/Th2Tx0uwPMOhsMPn7nRXMUo3vs6J0pto2DTn)![""](https://storage.googleapis.com/support-kms-prod/ocGtUSENh4QebLpvZcmLcNRZyaTBcolMRSyl) [Apps > Web and mobile apps](https://admin.google.com/ac/apps/unified).
3. Click **Add App**![and then](https://lh3.googleusercontent.com/QbWcYKta5vh\_4-OgUeFmK-JOB0YgLLoGh69P478nE6mKdfpWQniiBabjF7FVoCVXI0g=h36)**Add custom SAML app**.
4. On the **App Details** page:
   1. Enter the name of the custom app.
   2. (Optional) Upload an **app icon**. The app icon appears on the Web and mobile apps list, on the app settings page, and in the app launcher. If you don't upload an icon, an icon is created using the first two letters of the app name.
5. Click **Continue**.
6. Download the **IDP metadata** and send the file to the Secoda SAML team.
7. Click **Continue**.
8. In the **Service Provider Details** window, enter the appropriate URL for these 2 fields, based on the domain you use Secoda and your email domain: `https://secoda.placeholder.com/api/v1/auth/saml/placeholder+com/acs/`:
   * **ACS URL**
   * **Entity ID**
9.  In the attributes, the following mappings **must be set**:

    <figure><img src="../../.gitbook/assets/Screenshot 2023-06-19 at 10.06.35 AM.png" alt=""><figcaption></figcaption></figure>
