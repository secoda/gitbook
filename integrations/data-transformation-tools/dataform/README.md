---
description: An overview of the Dataform integration with Secoda
---

# Dataform

{% content-ref url="dataform-metadata-extracted.md" %}
[dataform-metadata-extracted.md](dataform-metadata-extracted.md)
{% endcontent-ref %}

## Getting Started with Dataform

{% hint style="info" %}
Dataform is a secondary integration that adds additional metadata on to your data warehouse or relational database tables. Before connecting Dataform make sure to connect a data warehouse or relational database first. These include BigQuery, Redshift, etc.
{% endhint %}

There are three steps to connect Dataform with Secoda:

1. Enable Dataform API
2. Create a service account for Secoda
3. Connect Dataform to Secoda

#### Enable Dataform API for GCP&#x20;

1. Go to Google Cloud Console and login.
2. Make sure you’re working in the project where you want to connect Dataform to Secoda.
3. Navigate to the **APIs & Services** page:
   * In the left-hand menu, go to **APIs & Services** > **Dashboard**.
   * Go to **Enable** **APIs & Services** at the top and search for Dataform
4. Navigate back to **APIs & Services** pag&#x65;**:**
   * In the list of APIs, check if “Dataform API” appears. If it’s listed and says **Enabled**, it’s active

#### Create a service account for Secoda

To provide [least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege) to Secoda for extracting Big Query metadata, you can create a new service account following the steps below. Refer to [Google Cloud’s documentation about service accounts](https://cloud.google.com/iam/docs/creating-managing-service-accounts) for more information.

1. From the Navigation panel on the left, go to **IAM & admin** > **Service accounts**
2. Click **Create Service Account** along the top
3. Enter a name (for example: “secoda”) and click **Create**
4. When assigning permissions, make sure to grant the following permissions:

a) If you're creating the service account via the GCP console add the following roles:

```
Dataform Viewer 
```

b) If you're programatically creating the service account add the following roles:

```
roles/dataform.viewer
```

5\. [Create a JSON key](https://cloud.google.com/iam/docs/creating-managing-service-account-keys). The downloaded file will be used to create your warehouse in the next section.

#### Connect Dataform to Secoda <a href="#h_724f251572" id="h_724f251572"></a>

* Log into your Secoda profile at [https://app.secoda.co](https://app.secoda.co)
* From the Navigation panel on the left go **Integrations** > **Add new integration**
* Select **Dataform**
* Enter in the project name and project location and paste the JSON key file contents that was downloaded
* Click "Connect"

