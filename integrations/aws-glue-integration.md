---
description: >-
  How to Integrate Secoda with AWS Glue, and what information and metadata is
  pulled from AWS Glue.
---

# AWS Glue Integration

## Integrating Secoda with AWS Glue&#x20;

The AWS Glue integration will pull metadata from your AWS Glue Catalog and the associated lineage information from the data sources for Glue. To connect AWS Glue to Secoda you'll need to create an IAM user that has permission to get Glue objects. Follow the instructions below to set up that user.

Log in to your [AWS console](https://us-east-1.console.aws.amazon.com/console/home?region=us-east-1) and then to the [IAM management console](https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/home)

Create a new IAM user by clicking "Add users"

Select "**Access key - Programmatic access"** under the "Select AWS access type" section and click "Next"

In the permissions section, select "Attach existing policies directly" and then click "Create policy".

Select the "JSON" option and paste in the following policy. Make sure to replace \<aws\_region> and \<aws\_account\_id> with the proper values. Then create the policy and return to the previous page for the IAM user creation.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "glue:GetDataflowGraph",
                "glue:GetJobs",
                "glue:GetTable",
                "s3:GetBucketLocation",
                "s3:GetObject",
                "s3:ListBucket",
                "s3:ListBucketMultipartUploads",
                "s3:AbortMultipartUpload",
                "s3:PutObject",
                "s3:ListMultipartUploadParts",
                "lambda:InvokeFunction",
                "athena:GetWorkGroup",
                "athena:StartQueryExecution",
                "athena:StopQueryExecution",
                "athena:GetQueryExecution",
                "athena:GetQueryResults",
            ],
            "Resource": [
                "arn:aws:athena:*:<athena_id>:workgroup/primary",
                "arn:aws:s3:::<athena_output_bucket>",
                "arn:aws:s3:::<athena_output_bucket>/*",
                "arn:aws:glue:<region>:<glue_id>:*"
                "arn:aws:s3:::<glue_bucket>",
                "arn:aws:s3:::<glue_bucket>/*",
            ]
        }
    ]
}
```

Refresh the policy list and search for your newly created policy. Select that policy and then create the user.&#x20;

Copy the Access Key ID and Secret Access Key that is generated for the user. Return to https://app.secoda.co/integrations and select the AWS Glue integration. Input your region, access key ID and secret access key and click "Test Connection". After the connection is established click "Run initial extraction" to begin the process of syncing your Glue Data Catalog.&#x20;
