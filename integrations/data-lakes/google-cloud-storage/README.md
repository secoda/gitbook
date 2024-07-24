---
description: An overview of Google Cloud Storage integration with Secoda
---

# Google Cloud Storage

{% content-ref url="gcs-metadata-extracted.md" %}
[gcs-metadata-extracted.md](gcs-metadata-extracted.md)
{% endcontent-ref %}

## Getting started with Google Cloud Storage

There are 3 steps to connect Google Cloud Storage with Secoda

1. Create a service account for Secoda
2. Create access key
3. Connect Google Cloud Storage to Secoda

### Create a service account for Secoda <a href="#h_f7ed2acb85" id="h_f7ed2acb85"></a>

To provide [least privilege](https://en.wikipedia.org/wiki/Principle\_of\_least\_privilege) to Secoda for extracting Google Cloud Storage metadata, you can create a new service account following the steps below.&#x20;

Refer to [Google Cloud’s documentation about service accounts](https://cloud.google.com/iam/docs/creating-managing-service-accounts) for more information.

1. From the Navigation panel on the left, go to **IAM & admin** > **Service accounts**
2. Click **Create Service Account** along the top
3. Enter a name (for example: “secoda”) and click **Create**
4. When assigning permissions, make sure to grant the following permission:

a) If you're creating the service account via the GCP console add the following role:

```
Storage Object Viewer
```

b) If you're programatically creating the service account add the following role:

```
roles/storage.objectViewer
```

### Create access key

On the GCP console, goto **Cloud Storage** and navigate to **Settings** on the panel on the left. Click on the **Interoperability** tab.

Generate HMAC keys for the newly created service account. Access key and the secret will be used to connect GCS to Secoda.



<figure><img src="../../../.gitbook/assets/Screenshot 2024-07-24 at 1.59.18 PM.png" alt=""><figcaption></figcaption></figure>

### &#x20;Connect Google Cloud Storage to Secoda

1. In Secoda, head to the **Integrations** page and click **New Integration**
2. Find **Google Cloud Storage** under **Data Storage**
3. Fill in the connection form with the Access Key and the Secret that were previously generated. Also, provide the name of the GCS bucket from which metadata is extracted
4. Click **Test Connection** to make sure everything is correct
5. Head to the **Sync History** tab on the side bar and click **Run sync**
