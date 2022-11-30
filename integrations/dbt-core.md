---
description: >-
  This page walks through the Secoda and dbt Core integration that Secoda
  supports
---

# dbt Core Integration

## **Getting Started with dbt Core** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

{% hint style="info" %}
dbt is a secondary integration that adds additional metadata on to your data warehouse or relational database tables. Before connecting dbt make sure to connect a data warehouse or relational database first. These include Snowflake, BigQuery, Postgres, Redshift, etc.
{% endhint %}

There are four options to connect dbt core with Secoda:

1. Upload a manifest.json
2. Connect an AWS S3 bucket
3. Connect a GCP GCS bucket&#x20;
4. Secoda API

#### **Upload manifest.json** <a href="#h_d49e98be3a" id="h_d49e98be3a"></a>

This is a one time sync with your manifest.json file. You can upload the file following these steps:

1. Navigate to [https://app.secoda.co/integrations/new](https://app.secoda.co/integrations/new)
2. Click "dbt Core"
3. Select your manifest.json file using the file selector
4. Click "Test Connection"
5. Click "Submit"

After clicking submit an extraction will run to sync the metadata from the uploaded manifest.json.



#### **Connect an AWS S3 bucket**

If you upload your manifest.json files to an AWS S3 bucket, you can connect that bucket to Secoda which will run a daily extraction to sync the latest manifest.json files. Only files from the bucket that contain `manifest.json` in the name will be synced to Secoda. You can connect the bucket following these steps:

Create a new AWS IAM user and ensure that **Access Key - Programatic access is checked.** Once you create the user save the Access Key ID and Secret Access Key that are generated for the user.

![](<../.gitbook/assets/image (3) (1) (1).png>)

![](<../.gitbook/assets/image (2) (1).png>)



Attach the following policy to the user. Make sure to change `<your-bucket-name>`.

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

Connect your S3 bucket to Secoda

1. &#x20;Navigate to [https://app.secoda.co/integrations/new](https://app.secoda.co/integrations/new)
2. Click "dbt Core"
3. Add the credentials that you've saved from AWS
   * Region
   * Bucket Name
   * Access Key ID
   * Secret Access Key
4. Click "Test Connection"
5. Click "Submit"

After clicking submit an extraction will run to sync the metadata from the manifest.json files in the S3 bucket that you've connected.

#### **Connect a GCS GCP bucket**

1. Login to GCP cloud console.
2. Turn on interoperability on the bucket. Generate HMAC keys for a service account with full access to the bucket. Both located here:

<figure><img src="../.gitbook/assets/Screen Shot 2022-10-21 at 2.22.34 PM.png" alt=""><figcaption></figcaption></figure>

3\. Fill in the integration page in Secoda based on the screenshot:

<figure><img src="../.gitbook/assets/Screen Shot 2022-10-28 at 11.14.56 AM.png" alt=""><figcaption></figcaption></figure>

**Secoda API**

The API provides an endpoint to upload your manifest.json file. This is convenient if you run dbt with Airflow because you can upload the manifest.json at the end of a dbt run. Follow these instructions to upload your manifest.json via the API:

1. Create a blank dbt core integration by going to [https://app.secoda.co/integrations/new](https://app.secoda.co/integrations/new) and selecting the "dbt Core" integration and then click "Test Connection". And run the initial extraction. This extraction will fail, but that's intended.
2. Return to https://app.secoda.co/integrations and click on the dbt Core integration that was just created. Save the ID which is contained in the URL.
3. Use the endpoint below to upload your manifest.json file. This will trigger an extraction to run on the integration you created in step #1.

* Endpoint - `https://api.secoda.co/integration/dbt/manifest/`&#x20;
* Method - `POST`
*   Sample Response

    ```json
    {
       "message":"Successfully ran extraction for dbt"
    }
    ```
*   Python Example

    ```python
    import requests

    headers = {
        "Authorization": "Bearer <Your Key>"
    }
    response = requests.post(
    	"<https://api.secoda.co/integration/dbt/manifest/>",
    	files={"manifest_file": open("manifest.json", "rb")},
    	data={"integration_id": "km1dhjql3xgxy9p8"},
    	headers=headers
    )
    print(response.json())
    ```
