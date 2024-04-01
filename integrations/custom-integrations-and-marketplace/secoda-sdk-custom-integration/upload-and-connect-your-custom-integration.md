# Upload and Connect your Custom Integration

Once your integration code is ready and fully tested locally. The next step is to upload it and connect your custom integration in Secoda.

### Upload your Custom Integration

1. **Navigate to the Create Integration Page**: Click on the Integrations in the side bar, navigate to the Create tab, and select Create Integration.

<figure><img src="../../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

2. **Enter Integration Details**: Fill in the submission form with the integration name, upload an integration icon, and provide a detailed description of your integration.

<figure><img src="../../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

3. **Script Upload**: Next, upload your integration script in the form of a python file.

<figure><img src="../../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

4. **Configure User Inputs**: List the user input fields that your script requires. In the example below, the fields for `email` and `password` are mandatory. `password` must also be flagged as sensitive to maintain the security of user credentials. The fields listed **must** directly match the code.&#x20;

<figure><img src="../../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

5. **List Endpoint Permissions**: Clearly list all the HTTP/HTTPS endpoints your script interacts with. This is a critical step that allows Secoda to validate the endpoints and allow the outbound traffic safely. This step ensures secure and seamless operation of your integration.

<figure><img src="../../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>



Once your custom integration has been created, the next step is to Connect your custom integration.

### Connect your Custom Integration

Your custom integration is now available to connect. The integration will be immediately available in the Browse tab of the Integration Marketplace as a `Draft`. Integrations in Draft are only visible to the workspace that the integration was uploaded in.&#x20;

<figure><img src="../../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

You can also connect to the integration through the Create tab, by expanding the menu of the integration card.&#x20;

<figure><img src="../../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

Now you can connect to your integration by filling in the credential details listed previously. Submit the details, and a sync will begin to run!

<figure><img src="../../../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

### Create a New Version&#x20;

You also have the option to create new version of your custom integration to update details such as icon, description, or implementation.&#x20;

<figure><img src="../../../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

##

Once fully tested, you can submit your integration (or new version) to the Marketplace. See [publishing-to-marketplace.md](publishing-to-marketplace.md "mention") for more details.
