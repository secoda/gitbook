---
description: >-
  This page walks through Connecting an integration via an AWS Cross Account
  Role
---

# Connecting via AWS Cross Account Role

### **Getting Started with AWS Cross Account Roles** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

To start the process of connecting your AWS account to Secoda, navigate to the [New Integrations](https://app.secoda.co/integrations/new) page and select an AWS integration. Select the "Role" Option.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/image%20(15)%20(1).png" alt=""></figure>

Cross-account roles are a mechanism provided by AWS to allow you to grant secure access to Secoda without requiring that you hand over sensitive secrets like Secret Access Keys.

The Secoda UI will display an **AWS Account ID** and a randomly generated **External ID**, as shown below, which must be plugged into an IAM Role you create in your AWS account. Store these values for future reference.

Neither the Account ID nor the External ID are secrets, so don't worry about keeping them somewhere secure.

1. From your AWS console, navigate to **IAM** > **Roles** and click **Create Role**.
2. Under **Select type of trusted entity**, choose **Another AWS account**.
3.

```
<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/cross-account-2-create-role.png" alt=""></figure>
```

4. Proceed to attach permissions to the role, choose a name, then create the role.
   * The exact permission policies you attach depend on which Secoda features you intend to use. Consult the documentation for those services for further guidance. Regardless, make sure to add the permissions `sts:AssumeRole` to your policy.
5. Copy the **Role ARN** from AWS IAM and paste it into the **Role ARN** field in Seoda. Click **Create** to complete the process.

For more information, read [AWS's tutorial](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial\_cross-account-with-roles.html) on delegating access cross-account using IAM Roles.
