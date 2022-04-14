---
description: Connecting dbt core to Secoda
---

# dbt Core

### **Getting Started** <a href="#h_0703b4d233" id="h_0703b4d233"></a>

There are two options to connect dbt core with Secoda:

1. Upload a manifest.json
2. Connect an AWS S3 bucket

#### **Upload manifest.json** <a href="#h_d49e98be3a" id="h_d49e98be3a"></a>

This is a one time sync with your manifest.json file. You can upload the file following these steps:

1. Navigate to [https://app.secoda.co/integrations/new](https://app.secoda.co/integrations/new)
2. Click "dbt Core"
3. Select your manifest.json file using the file selector
4. Click "Test Connection"
5. Click "Submit"

After clicking submit an extraction will run to sync the metadata from the uploaded manifest.json.



**Connect an AWS S3 bucket**

If you upload your manifest.json files to an AWS S3 bucket, you can connect that bucket to Secoda which will run a daily extraction to sync the latest manifest.json files. Only files from the bucket that contain `manifest.json` in the name will be synced to Secoda. You can connect the bucket following these steps:

Create a new AWS IAM user and ensure that **Access Key - Programatic access is checked.** Once you create the user save the Access Key ID and Secret Access Key that are generated for the user.

![](<../.gitbook/assets/image (3).png>)

![](<../.gitbook/assets/image (1).png>)



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
