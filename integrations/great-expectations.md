---
description: This page walks through the Secoda and GE integration that Secoda supports
---

# Great Expectations

Secoda currently supports retrieving expectation and validation metadata from Google Cloud Storage.

## Getting Started with Great Expectations and Google Cloud Storage <a href="#h_21e27f5a15" id="h_21e27f5a15"></a>

There are two steps to get started using Great Expectations with Secoda through Google Cloud Storage:

1. Create a service account for Secoda
2. Connect Google Cloud Storage to Secoda

### Create a service account for Secoda

To provide [least privilege](https://en.wikipedia.org/wiki/Principle\_of\_least\_privilege) to Secoda for extracting Big Query metadata, you can create a new service account following the steps below. Refer to [Google Cloud’s documentation about service accounts](https://cloud.google.com/iam/docs/creating-managing-service-accounts) for more information.

1. From the Navigation panel on the left, go to **IAM & admin** > **Service accounts**
2. Click **Create Service Account** along the top
3. Enter a name (for example: “secoda”) and click **Create**
4. When assigning permissions, make sure to grant the following roles:

```
Storage Object Viewer
```

5\. [Create a JSON key](https://cloud.google.com/iam/docs/creating-managing-service-account-keys). The downloaded file will be used to create your warehouse in the next section.

### Connect Google Cloud Storage to Secoda

1. Log into your Secoda profile at [https://app.secoda.co](https://app.secoda.co)
2. From the Navigation panel on the left go **Integrations** > **Add new integration**
3. Select **Great Expectations** and fill in the fields based off the Great Expectations Data Context YAML file.

