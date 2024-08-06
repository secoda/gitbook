---
description: An overview of the AWS S3 integration with Secoda
---

# AWS S3

{% content-ref url="s3-metadata-extracted.md" %}
[s3-metadata-extracted.md](s3-metadata-extracted.md)
{% endcontent-ref %}

## Getting started with S3

There are two steps to connect AWS S3 with Secoda

1. Create a new AWS IAM user or AWS Role
2. Connect S3 to Secoda

### **Create a new AWS IAM User or AWS Role**

**Create a Custom Permissions Policy**

1. Navigate to the 'Policies' page in IAM and 'Create Policy'&#x20;
2. Create the following custom permissions policy. Make sure to change `<your-bucket-name>` to the appropriate S3 bucket

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

**Option 1: Create a new AWS IAM user**

3. Navigate to the 'Users' page in IAM and 'Create User'
4. In the Set Permissions tab select 'Attach policies directly'. Attach the custom permissions policy to the user.
5. Navigate to the newly created user and click 'Create Access Key'  to gain Programmatic Access

**Option 2: Create a new AWS Role**

1. Navigate to the 'Roles' page in IAM and 'Create Role'&#x20;
2. In the 'Select trusted entity' page, click 'AWS account' and add the following account ID: 482836992928
3. Click on 'Require External ID' and copy the randomly generated value from Secoda in the S3 connection page
4. In the Add Permissions tab attach your custom permissions policy to the role.&#x20;

### **Connect S3 to Secoda**

After creating an IAM user, the next step is to connect S3 to Secoda

1. In the Secoda App, navigate to the 'Integrations' tab
2. Click on 'Connect Integration'
3. Search for and select 'S3'
4. Add the credentials from the newly created user (Access Key ID, Secret Access Key, Bucket Name, Region) or role (ARN Role, Bucket Name, Region)
5. Test the Connection - if successful, you'll be prompted to run your initial sync
