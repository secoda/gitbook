# AWS Bucket with Access Keys (on-premise)

### **Step 1: Log In to AWS Management Console**

1. Go to the [AWS Management Console](https://aws.amazon.com/console/).
2. Log in with your AWS credentials.

***

### **Step 2: Create an S3 Bucket**

1. In the AWS Management Console, search for **S3** in the search bar and select the **S3 service**.
2. Click on **"Create bucket"**.
3. Provide a **unique bucket name.**
4. Configure settings:
   * **Object Ownership**: Choose disabled.
   * **Block Public Access Settings**: Block public access.
5. Enable encryption and versioning.
6. Click **"Create bucket"**.

***

### **Step 3: Create Access Keys**

#### **A. Go to the IAM Console**

1. In the AWS Management Console, search for **IAM** (Identity and Access Management).
2. Click on **Users** in the IAM dashboard.

#### **B. Create or Select a User**

1. If creating a new user:
   * Click **"Add users"**.
   * Provide a username.
   * Select **"Programmatic access"** as the access type.
2. If using an existing user, click on the user name to edit their permissions.

#### **C. Attach Policies**

1. Assign a policy that allows access to S3, such as:
   * **Custom Policy**: Create a custom policy to restrict access to specific buckets or actions:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:*"
      ],
      "Resource": [
        "arn:aws:s3:::example-bucket/*",
        "arn:aws:s3:::example-bucket"
      ]
    }
  ]
}
```

#### **D. Generate Access Keys**

1. Go to the **Security Credentials** tab for the user.
2. Click **"Create access key"**.
3. Copy and securely store the **Access Key ID** and **Secret Access Key**.
   * These keys will not be shown again after creation.

#### **Security Best Practices**

* Regularly rotate access keys.
* Use least privilege policies to limit access.
