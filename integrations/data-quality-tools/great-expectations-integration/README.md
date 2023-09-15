---
description: This page walks through the Secoda and GE integration that Secoda supports
---

# Great Expectations

{% content-ref url="metadata-extracted.md" %}
[metadata-extracted.md](metadata-extracted.md)
{% endcontent-ref %}

Secoda currently supports retrieving expectation and validation metadata from Google Cloud Storage and AWS S3.

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

### Connecting to Secoda

Log into your Secoda profile at [https://app.secoda.co](https://app.secoda.co)

1. From the Navigation panel on the left go **Integrations** > **Add new integration**
2. Select **Great Expectations** and fill in the fields based off of the Great Expectations configuration YAML file.
3. Make sure to upload the Great Expectations configuration YAML file.
4. You will be asked to map each datasource outlined in your configuration file to an existing integration in Secoda.

## Getting Started with Great Expectations and AWS S3 <a href="#h_21e27f5a15" id="h_21e27f5a15"></a>

There are two steps to get started using Great Expectations with Secoda through AWS S3

1. Create a new AWS IAM user
2. Connect AWS S3 to Secoda

### Create a AWS IAM user for Secoda

You can create an IAM user using one of three methods:

* [Creating IAM users (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id\_users\_create.html#id\_users\_create\_console)
* [Creating IAM users (AWS CLI)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id\_users\_create.html#id\_users\_create\_cliwpsapi)
* [Creating IAM users (AWS API)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id\_users\_create.html#id\_users\_create\_api)

**Note**: Ensure that _Access Key - Programmatic Access_ is checked.

Once you create the user you can save the Access Key ID and Secret Access Key generated for the user.

Attach the following policy to the newly created user. Make sure to change `<your-bucket-name>`&#x20;

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

### Connecting to Secoda

1. Log into your Secoda profile at [https://app.secoda.co](https://app.secoda.co)
2. From the Navigation panel on the left go **Integrations** > **Add new integration**
3. Select **Great Expectations** and fill in the fields based off of the Great Expectations configuration YAML file.
4. Make sure to upload the Great Expectations configuration YAML file.
5. You will be asked to map each datasource outlined in your configuration file to an existing integration in Secoda.

