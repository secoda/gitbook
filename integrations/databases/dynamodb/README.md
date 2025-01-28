---
description: An overview of the DynamoDB integration with Secoda
---

# DynamoDB

## Getting Started with DynamoDB

There are 3 steps to get started using DynamoDB with Secoda:

1. Create an IAM User or AWS Role
2. Get AWS credentials
3. Connect DynamoDB to Secoda

### Create an IAM User or AWS Role

**Create a Custom Permissions Policy**

1. Navigate to the 'Policies' page in IAM and 'Create Policy'&#x20;
2. Create the following custom permissions policy. You may modify "Resource" to only allow access to certain tables

```
{
    "Statement": [
        {
            "Action": [
                "dynamodb:ListTables",
                "dynamodb:DescribeTable",
                "dynamodb:Scan"
            ],
            "Effect": "Allow",
            "Resource": "*"
        }
    ],
    "Version": "2012-10-17"
}
```

**Option 1: Create a new AWS IAM user**

3. Navigate to the 'Users' page in IAM and 'Create User'
4. In the Set Permissions tab select 'Attach policies directly'. Attach the custom permissions policy to the user.
5. Navigate to the newly created user and click 'Create Access Key'  to gain Programmatic Access

**Option 2: Create a new AWS Role**

1. Navigate to the 'Roles' page in IAM and 'Create Role'&#x20;
2. In the 'Select trusted entity' page, click 'AWS account' and add the following account ID: 482836992928
3. Click on 'Require External ID' and copy the randomly generated value from Secoda in the DynamoDB connection page
4. In the Add Permissions tab attach your custom permissions policy to the role.&#x20;

### Get AWS Credentials

#### Access Key

* AWS Access Key ID
* AWS Secret Access Key
* AWS Session Token
* AWS Region where your DynamoDB tables are located

#### Role

* ARN Role
* AWS Region where your DynamoDB tables are located

### Connect DynamoDB to Secoda

1. In the Secoda App, select 'Add Integration' on the Integrations tab
2. Search for and select DynamoDB
3. Enter your AWS credentials
4. Click 'Test connection' - if successful, you'll be prompted to run your initial sync

