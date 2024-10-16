---
description: An overview of the AWS Glue integration with Secoda
---

# Glue

{% content-ref url="metadata-extracted.md" %}
[metadata-extracted.md](metadata-extracted.md)
{% endcontent-ref %}

### Getting Started with Glue&#x20;

The AWS Glue integration will pull metadata from your AWS Glue Catalog and the associated lineage information from the data sources for Glue. To connect AWS Glue to Secoda you'll need to create an IAM user that has permission to get Glue objects. Follow the instructions below to set up that user.

The following steps are taken to connect AWS Glue to Secoda

1.  Set up Glue Access

    a. Option 1: Create a Secoda Glue User\
    b. Option 2: Create a Secoda Glue Role&#x20;
2. Update the Lake Formation permissions
3. Connect the AWS Glue integration to Secoda

### Set up Glue Access

#### Option 1: Create a Secoda Glue User

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
                "glue:GetJobRuns",
                "glue:GetTable",
                "glue:GetDatabases",
                "glue:SearchTables",
                "s3:GetBucketLocation",
                "s3:GetObject",
                "s3:ListBucket",
                "s3:ListBucketMultipartUploads",
                "s3:AbortMultipartUpload",
                "s3:PutObject",
                "s3:ListMultipartUploadParts",
                "athena:GetWorkGroup",
                "athena:StartQueryExecution",
                "athena:StopQueryExecution",
                "athena:GetQueryExecution",
                "athena:GetQueryResults",
                "athena:ListWorkGroups",
                "athena:ListDataCatalogs",
                "athena:ListQueryExecutions",
                "s3:ListMultipartUploadParts",
                "sts:AssumeRole"
            ],
            "Resource": [
                "arn:aws:athena:*:<athena_id>:workgroup/primary",
                "arn:aws:s3:::<athena_output_bucket>",
                "arn:aws:s3:::<athena_output_bucket>/*",
                "arn:aws:glue:<region>:<glue_id>:*",
                "arn:aws:s3:::<glue_bucket>",
                "arn:aws:s3:::<glue_bucket>/*"
            ]
        }
    ]
}
```

Refresh the policy list and search for your newly created policy. Select that policy and then create the user.&#x20;

#### Option 2: Create a Secoda Glue Role

Prior to creating the AWS IAM role, go to the Secoda application > Integrations > Create Integration > Glue. Copy the "External ID" that's prefilled in the integration form. This will be used when creating your IAM role.

Log in to your [AWS console](https://us-east-1.console.aws.amazon.com/console/home?region=us-east-1) and then to the [IAM management console](https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/home) then go to the Policies section and click "Create policy".&#x20;

Select the JSON tab and enter in the following policy.&#x20;

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
                "glue:GetDatabases",
                "glue:SearchTables",
                "s3:GetBucketLocation",
                "s3:GetObject",
                "s3:ListBucket",
                "s3:ListBucketMultipartUploads",
                "s3:AbortMultipartUpload",
                "s3:PutObject",
                "s3:ListMultipartUploadParts",
                "athena:GetWorkGroup",
                "athena:StartQueryExecution",
                "athena:StopQueryExecution",
                "athena:GetQueryExecution",
                "athena:GetQueryResults",
                "athena:ListWorkGroups",
                "athena:ListDataCatalogs",
                "athena:ListQueryExecutions",
                "s3:ListMultipartUploadParts",
                "sts:AssumeRole"
            ],
            "Resource": [
                "arn:aws:athena:*:<athena_id>:workgroup/primary",
                "arn:aws:s3:::<athena_output_bucket>",
                "arn:aws:s3:::<athena_output_bucket>/*",
                "arn:aws:glue:<region>:<glue_id>:*",
                "arn:aws:s3:::<glue_bucket>",
                "arn:aws:s3:::<glue_bucket>/*"
            ]
        }
    ]
}
```

Name the policy `secoda-glue-policy` or a name of your choice.

Next, go to the Roles section and create a new IAM role by clicking "Create role".

Select the "AWS account" option, then select "Another AWS account", enter the account number `482836992928` , click "Require external ID" and copy in the value from the first step. Then click "Next".

Add the `secoda-glue-policy` to the role, and then copy the Role ARN.

### Update your Lake Formation Permissions

Go to AWS Lake Formation > Permissions > Data Lake Permissions and ensure that the Secoda Glue user has `SELECT` permission on all the necessary tables.

### Connect the AWS Glue integration to Secoda

Return to https://app.secoda.co/integrations and select the AWS Glue integration. If using a AWS IAM User, copy the Access Key ID and Secret Access Key that is generated for the user. If using the Role, input the role ARN. Next input your region, access key ID and secret access key and click "Test Connection". After the connection is established click "Run initial extraction" to begin the process of syncing your Glue Data Catalog.&#x20;
