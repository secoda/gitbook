# Set your Integration Preferences

Once you've made the integration, you can alter some settings to determine the behaviour of your integrations. These settings can only be set in the UI. Navigate to the Preferences heading of your Integration.&#x20;

<figure><img src="../../.gitbook/assets/Screenshot 2023-06-09 at 2.55.24 PM.png" alt=""><figcaption></figcaption></figure>

By default the preferences are set to disabled for all integrations. Toggle them on if you'd like to:&#x20;

* **Use the Source as the Description Source of Truth:** This means that if the CSV with your resources has a description that differs from Secoda, the description in the CSV will over write the one in Secoda.&#x20;
* **Disable Automatic Staling:** The integration by default assumes that every upload will be off the same master CSV with **ALL** the resources in Secoda. This means that if a row is missing from the CSV, Secoda will stale (archive) that resource in Secoda. If you're planning on uploading net new resources with every CSV, you'll want to disable automatic staling so that missing rows don't result in archived resources.&#x20;

Now that you've set your preferences, navigate to the next page to Create your CSV.
