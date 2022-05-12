# AWS Glue

The AWS Glue integration will pull metadata from your AWS Glue Catalog and the associated lineage information from the data sources for Glue. To connect AWS Glue to Secoda you'll need to create an IAM user that has permission to get Glue objects. Follow the instructions below to set up that user.

Log in to your [AWS console](https://us-east-1.console.aws.amazon.com/console/home?region=us-east-1) and then to the [IAM management console](https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/home)

Create a new IAM user by clicking "Add users"

![](<../.gitbook/assets/image (3).png>)

Select "**Access key - Programmatic access"** under the "Select AWS access type" section and click "Next"

![](<../.gitbook/assets/image (6).png>)

In the permissions section, select "Attach existing policies directly" and then click "Create policy".

![](<../.gitbook/assets/image (8).png>)

Select the "JSON" option and paste in the following policy. Make sure to replace \<aws\_region> and \<aws\_account\_id> with the proper values. Then create the policy and return to the previous page for the IAM user creation.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "glue:GetDatabases",
                "glue:GetTables"
            ],
            "Resource": [
                "arn:aws:glue:<aws_region>:<aws_account_id>:catalog",
                "arn:aws:glue:<aws_region>:<aws_account_id>:database/*",
                "arn:aws:glue:<aws_region>:<aws_account_id>:table/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "glue:GetDataflowGraph",
                "glue:GetJobs"
            ],
            "Resource": "*"
        }
    ]
}
```

Refresh the policy list and search for your newly created policy. Select that policy and then create the user.&#x20;

![](<../.gitbook/assets/image (1).png>)

Copy the Access Key ID and Secret Access Key that is generated for the user. Return to https://app.secoda.co/integrations and select the AWS Glue integration. Input your region, access key ID and secret access key and click "Test Connection". After the connection is established click "Run initial extraction" to begin the process of syncing your Glue Data Catalog.&#x20;
