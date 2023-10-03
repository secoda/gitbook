---
description: An overview of the AWS QuickSight integration with Secoda
---

# QuickSight

{% content-ref url="metadata-extracted.md" %}
[metadata-extracted.md](metadata-extracted.md)
{% endcontent-ref %}

## Integrating Secoda with AWS QuickSight&#x20;

The AWS QuickSight integration will pull metadata from your AWS QuickSight workspace and the associated lineage information from the data sources for QuickSight. To connect AWS QuickSight to Secoda you'll need to create an IAM user that has permission to get QuickSight objects. Follow the instructions below to set up that user.

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
            "Action": [
                "quicksight:ListAnalyses",
                "quicksight:DescribeAnalysis",
                "quicksight:ListDashboards",
                "quicksight:DescribeDashboard",
                "quicksight:ListDataSets",
                "quicksight:DescribeDataSet",
                "quicksight:DescribeDataSource",
            ],
            "Resource": "*",
            "Effect": "Allow"
        },
    ]
}
```

Refresh the policy list and search for your newly created policy. Select that policy and then create the user.&#x20;

Copy the Access Key ID and Secret Access Key that is generated for the user. Return to https://app.secoda.co/integrations and select the AWS QuickSight integration. Input your AWS Account ID, region, access key ID and secret access key and click "Test Connection". After the connection is established click "Run initial extraction" to begin the process of syncing your Quicksight workspace.&#x20;
