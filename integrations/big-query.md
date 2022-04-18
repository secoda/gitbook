# Big Query

### Getting Started <a href="#h_21e27f5a15" id="h_21e27f5a15"></a>

There are three steps to get started using Big Query with Secoda:

1. Enable the Big Query API
2. Create a service account for Secoda
3. Connect Big Query to Secoda

#### Enable Big Query API for GCP <a href="#h_3ec8fd603e" id="h_3ec8fd603e"></a>

Log in to your existing project on GCP and [enable the BigQuery API](https://cloud.google.com/bigquery/docs/quickstarts/quickstart-web-ui). Once you’ve done so, you should see BigQuery in the [“Resources” section](https://cl.ly/0W2i2I2B2R0M) of Cloud Platform.

#### Create a service account for Secoda <a href="#h_f7ed2acb85" id="h_f7ed2acb85"></a>

To provide [least privilege](https://en.wikipedia.org/wiki/Principle\_of\_least\_privilege) to Secoda for extracting Big Query metadata, you can create a new service account following the steps below. Refer to [Google Cloud’s documentation about service accounts](https://cloud.google.com/iam/docs/creating-managing-service-accounts) for more information.

1. From the Navigation panel on the left, go to **IAM & admin** > **Service accounts**
2. Click **Create Service Account** along the top
3. Enter a name (for example: “secoda”) and click **Create**
4. When assigning permissions, make sure to grant the following roles:

```
BigQuery Metadata Viewer
BigQuery Resource Viewer
Job Viewer
Logs Viewer
Private Logs Viewer
BigQuery Data Viewer
```

\*BigQuery Data Viewer is not required for the catalog feature, but is required for the query and chart blocks feature. We recommend adding this role for the best experience on Secoda.

5\. [Create a JSON key](https://cloud.google.com/iam/docs/creating-managing-service-account-keys). The downloaded file will be used to create your warehouse in the next section.

#### Connect Big Query to Secoda <a href="#h_724f251572" id="h_724f251572"></a>

* Log into your Secoda profile at [https://app.secoda.co](https://app.secoda.co)
* From the Navigation panel on the left go **Integrations** > **Add new integration**
* Select **Big Query**
* Enter in the project name and paste the JSON key file contents that was downloaded
* Click "Connect"

After these steps are completed, Secoda will extract the metadata associated with Big Query once every 24 hours.

\\
