# Access Requests

The Access requests feature in Secoda simplifies and centralizes the process of requesting, approving, and auditing access to data resources across multiple platforms. This feature helps organizations eliminate fragmented workflows, enhance security, and streamline compliance.

{% hint style="info" %}
**Access Requests** are available to customers on [**Enterprise** **plan**](https://www.secoda.co/pricing)**.** Interested in upgrade options? Click on the "Upgrade" button on the Access Request page or reach out to the Customer team (support@secoda.co).
{% endhint %}



### Key Features

* **Centralized Requests**: Users can create Access requests directly within Secoda, specifying the resources, access duration, and roles.
* **Automated Provisioning & Revocation**: Upon approval, access is provisioned automatically and revoked after the expiration period, reducing manual effort and improving security.
* **Detailed Audit Logs**: Track every access request, including resources, requester, roles, reviewers, and expiration timelines, ensuring transparency and compliance.
* **Identity Management**: Admins can browse and manage all ingested identities (users and roles) from integrated platforms.
* **Slack Integration**: Configure a dedicated Slack channel for access request notifications. Approvals can be handled directly in Slack with a ✅ reaction.
* **Secoda AI Integration**: Easily query Secoda AI to check if a specific user has access to a particular resource.

### How It Works

1.  **Creating a Request**: Users can create an Access request from Secoda specifying:

    1. Resources they want access to.
    2. An optional reason for access.
    3. An optional expiration period for access.

    <figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/bbd7225d-ae46-41b0-8255-da47fb72d5ee.png" alt=""><figcaption></figcaption></figure>
2. Review & Approval:
   1. Reviewers evaluate the request and choose the role or identity to update.
   2. Access requests can be approved via the Secoda interface or Slack.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/1b90b24c-98c0-4e7f-a77b-5d2da25d9687.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/0d589971-d599-46ac-a3bc-857d3f34ac2e.png" alt=""><figcaption></figcaption></figure>

3. Access Management: Upon approval:
   1. Access is granted automatically to the specified identity.
   2. Access is revoked automatically after the expiration period.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/8bae061d-7718-4df2-b2fa-0f6136054ccb.png" alt=""><figcaption></figcaption></figure>

### Getting Started

1. Setup Integrations: Connect supported platforms to Secoda to ingest user and role identities.
2. Configure Slack Channel: Enable the “Access Requests” channel for real-time notifications and approvals.
3. Manage Roles: Assign the Reviewer role to appropriate team members to streamline the review process.
4. Track Requests: Use the Access Requests dashboard to monitor, audit, and manage requests.

### Supported Integrations

Access Requests will be support the following platforms during the Beta period:

* Snowflake
* BigQuery
* Redshift
* Postgres

### Use Cases

* Data Access Governance: Ensure that only authorized users can access sensitive data and that access is tracked and time-bound.
* Streamlined Collaboration: Simplify the process of granting access to analysts, data scientists, or other team members needing data for their workflows.
* Enhanced Compliance: Maintain detailed audit trails for all access requests, meeting regulatory and organizational compliance needs.

### Troubleshooting

* `No actions Available` for certain requests
  * There are no actions available for `Closed` or `Denied` requests. `Active` requests can be revoked and `Open` requests can be approved, denied or deleted.&#x20;
