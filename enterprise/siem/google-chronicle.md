---
description: Integrating Secoda logs with Google Chronicle SIEM
---

# Google Chronicle

#### Introduction

This guide outlines the steps for customers to connect to Secoda's AWS CloudWatch Logs via Google Chronicle Security Information and Event Management (SIEM). Secoda manages a single-tenant instance on AWS, ensuring that each customer can securely access their designated CloudWatch logs for advanced monitoring and security analytics using Google Chronicle.

#### Prerequisites

Before initiating this process, ensure you have:

1. **Access Credentials**: Provided by Secoda for accessing the AWS environment.
2. **Google Chronicle Account**: Access with necessary permissions to configure data sources.
3. **Secoda Support Contact**: For any assistance required during the setup.

#### Steps to Connect Secoda's AWS CloudWatch Logs to Google Chronicle SIEM

**Step 1: Obtain AWS Credentials from Secoda**

Contact Secoda to obtain the necessary credentials and access configurations for the AWS environment where your logs are stored. Secoda will provide:

* **AWS Access Key ID and Secret Access Key**: For programmatic access to AWS.
* **Specific CloudWatch Log Group Name**: Identifying the log group that contains your logs.

**Step 2: Configure Google Chronicle to Receive Logs**

**Set Up a New Data Source in Google Chronicle**

1. **Log into your Google Chronicle account**.
2. Navigate to **Settings** and then to **Sources**.
3. Select **Add Source** to configure a new data source for receiving logs from AWS CloudWatch.
4. Chronicle will provide a URL endpoint; this will be used to configure the log export in AWS.

**Step 3: Set Up CloudWatch Log Export to Google Chronicle**

**Configure Export Task in AWS**

Utilize the AWS CLI with the credentials provided by Secoda to set up an export task that forwards logs to Google Chronicle.

1. **Open your command line interface**.
2. Configure the AWS CLI with the credentials provided by Secoda.
3.  Execute the following command to create an export task:

    ```bash
    aws logs create-export-task --task-name "ExportToChronicle" \
    --log-group-name "<provided-log-group-name>" \
    --from <start-time-epoch> --to <end-time-epoch> \
    --destination "<Google-Chronicle-endpoint>" \
    --destination-prefix "<log-data-prefix>"
    ```

    Replace placeholders with the details specific to your configuration.

**Monitor Export Task**

It's important to ensure that the logs are being transferred correctly.

```bash
aws logs describe-export-tasks --task-id "<task-id>"
```

**Step 4: Validate Log Reception in Google Chronicle**

**Verify Incoming Data**

After setting up the data source and export task, monitor the Google Chronicle interface to confirm that logs are being ingested correctly. Check for any discrepancies and ensure the data matches the logs sent from AWS.

#### Troubleshooting Common Issues

* **Authentication and Permissions**: If there are issues accessing AWS or exporting logs, please verify the credentials and permissions provided by Secoda.
* **Configuration Errors**: Double-check all entered configurations for accuracy, especially the endpoint URLs and log group names.
* **Data Discrepancies**: If logs do not appear as expected in Google Chronicle, contact Secoda support for assistance in verifying log configurations and export settings.

#### Conclusion

Connecting to Secoda's AWS CloudWatch Logs via Google Chronicle SIEM allows customers to utilize powerful security analytics and monitoring tools for enhanced visibility and security of their systems managed by Secoda. Should you encounter any difficulties during setup or operation, Secoda's support team is available to assist with resolving issues and ensuring a smooth integration process.
