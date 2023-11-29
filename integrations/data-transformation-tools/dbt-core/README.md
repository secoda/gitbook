---
description: An overview of the dbt Core integration with Secoda
---

# dbt Core

{% content-ref url="metadata-extracted.md" %}
[metadata-extracted.md](metadata-extracted.md)
{% endcontent-ref %}

## **Getting Started with dbt Core** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

{% hint style="info" %}
dbt is a secondary integration that adds additional metadata on to your data warehouse or relational database tables. Before connecting dbt make sure to connect a data warehouse or relational database first. These include Snowflake, BigQuery, Postgres, Redshift, etc.

The metadata extracted from dbt core is: Descriptions, Lineage, SQL Query, and Tags (optional).
{% endhint %}

There are several options to connect dbt core with Secoda:

1. Connect an AWS S3 or GCP GCS bucket (Recommended)
2. Upload a `manifest.json` and `run_results.json` through the UI
3. Upload a `manifest.json` and `run_results.json` through the Secoda API

## **Option 1 -> Connect a Bucket (Recommended)** <a href="#h_d49e98be3a" id="h_d49e98be3a"></a>

This option is recommended to ensure that Secoda always has the latest `manifest.json` and `run_results.json` files from dbt Core. Secoda will only sync these files from the bucket.

### **Connect an AWS S3 bucket**

You can connect to the AWS S3 bucket using an AWS IAM user, or AWS Roles.&#x20;

<details>

<summary>AWS IAM User</summary>

1. Create a new AWS IAM user and ensure that **Access Key - Programatic access is checked.** Once you create the user save the Access Key ID and Secret Access Key that are generated for the user.
2. Attach the following policy to the user. Make sure to change `<your-bucket-name>`.

```
{
    "Statement": [
        {
            "Action": [
                "s3:PutObject",
                "s3:PutObjectAcl",
                "s3:ListBucket",
                "s3:GetObject",
                "s3:GetObjectAcl",
                "s3:DeleteObject"
            ],
            "Effect": "Allow",
            "Resource": [
                "arn:aws:s3:::<your-bucket-name>",
                "arn:aws:s3:::<your-bucket-name>/*"
            ]
        }
    ],
    "Version": "2012-10-17"
}
```

3. Connect your S3 bucket to Secoda
   * Navigate to [https://app.secoda.co/integrations/new](https://app.secoda.co/integrations/new) and click dbt Core
   * Choose the Access Key tab and add the credentials from AWS (Region, Bucket Name, Access Key ID, Secret Access Key)
   * Test the Connection - if successful, you'll be prompted to run your initial sync

</details>

<details>

<summary>AWS Roles</summary>

1. Create a new AWS IAM role. In the Select type of trusted entity page, click Another AWS account and add the following account ID: 482836992928.&#x20;
2. Click on Require External ID, and copy the randomly generated value from Secoda, in the dbt Core connection page.&#x20;
3. Attach the following policy to the role. Make sure to change `<your-bucket-name>`.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::<your-bucket-name>",
                "arn:aws:s3:::<your-bucket-name/*"
            ]
        }
    ]
}
```

4. Once the role is created, you'll receive an Amazon Resource Name (ARN) for the role.&#x20;
5. Connect your S3 bucket to Secoda
   * Navigate to [https://app.secoda.co/integrations/new](https://app.secoda.co/integrations/new) and click dbt Core
   * Choose the Role tab and add the credentials from AWS (Role ARN, Region, Bucket Name)
   * Test the Connection - if successful you'll be prompted to run your initial sync

</details>

### **Connect a GCS GCP bucket**

1. Login to GCP cloud console.
2. Create a service account.
3. Grant access to the service account from the Bucket page as “Storage Object Viewer”.
4. Turn on interoperability on the bucket. Generate HMAC keys for a service account with read access to the bucket. Both located here:

![](https://secoda-public-media-assets.s3.amazonaws.com/Screen%20Shot%202022-10-21%20at%202.22.34%20PM.png)

5. Setup CORS. GCP requires this be done over CLI. Like the following:

```
gsutil cors set cors.json gs://bucket-name
```

**cors.json**

```
[
  {
    "origin": ["*"],
    "method": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    "responseHeader": ["Content-Type"],
    "maxAgeSeconds": 3600
  }
]
```

6. Save the HMAC keys to be used in the connection form.
   * **Acess Key Id**
   * **Secret**
   * **Region** bucket region for GCP
   * **S3 Endpoint** must be added and set to `https://storage.googleapis.com`
7. Connect your S3 bucket to Secoda
   * Navigate to [https://app.secoda.co/integrations/new](https://app.secoda.co/integrations/new) and click dbt Core
   * Choose the Access Key tab and add the HMAC keys saved above to the relevant fields.&#x20;
   * Test the Connection - if successful you'll be prompted to run your initial sync

### **Upload manifest.json** <a href="#h_d49e98be3a" id="h_d49e98be3a"></a>

This is a one time sync with your manifest.json file. You can upload the file following these steps:

1. Navigate to [https://app.secoda.co/integrations/new](https://app.secoda.co/integrations/new) and click dbt Core
2. Choose the File Upload tab and select your manifest.json and run\_results.json files using the file select
3. Test the Connection - if successful you'll be prompted to run your initial sync

### **Secoda API**

The API provides an endpoint to upload your manifest.json and run\_results.json file. This is convenient if you run dbt with Airflow because you can upload the manifest.json at the end of a dbt run. Follow these instructions to upload your manifest.json via the API:

1. Create a blank dbt core integration by going to [https://app.secoda.co/integrations/new](https://app.secoda.co/integrations/new) and selecting the "dbt Core" integration and then click "Test Connection". And run the initial extraction. This extraction will fail, but that's intended.
2. Return to https://app.secoda.co/integrations and click on the dbt Core integration that was just created. Save the ID which is contained in the URL.
3. Use the endpoints below to upload your files. This will trigger an extraction to run on the integration you created in step #1.

Endpoints  ->&#x20;

Manifest.json: `https://api.secoda.co/integration/dbt/manifest/`

Run\_results.json: `https://api.secoda.co/integration/dbt/run_results/`

Method -> `POST`

Sample Request for Manifest file (Python) ->&#x20;

```python
import requests

headers = {
    "Authorization": "Bearer <Your Key>"
}
response = requests.post(
	"<https://api.secoda.co/integration/dbt/manifest/>",
	files={"manifest_file": open("manifest.json", "rb")},
	data={"integration_id": "Your Integration ID"},
	headers=headers
)
print(response.json())
```

Sample Response ->&#x20;

```json
{
   "message":"Successfully ran extraction for dbt"
}
```
