---
description: List of all the metadata that Secoda pulls from Jira
---

# Jira Metadata Extracted

### **What does Secoda extract from Jira?** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

* Requests from Jira Issues (Requests are referred to as Questions in Secoda)
  * Comments on the ticket
  * Priority set on the ticket
  * User that the ticket is assigned to
  * User that wrote the ticket
  * Tags on the ticket
  * URL for the Jira Issue

### Jira page transformation to Secoda question <a href="#confluence-page-transformation-to-secoda-document" id="confluence-page-transformation-to-secoda-document"></a>

When a Jira issue is brought into Secoda, it'll transfer over as a question. These questions can be found in the questions section of the team the integration is assigned to, and can be identified by looking at the source and type in the metadata side-bar.

In the example below, you'll see that the main difference is that Secoda has the additional side-bar metadata. This is extracted from the Jira issue metadata and includes info like the issue owner, created and updated timestamps.

Example Jira issue:

<figure><img src="../../../.gitbook/assets/Screenshot 2024-05-09 at 4.40.46 PM.png" alt=""><figcaption><p>Example of an issue created in Jira</p></figcaption></figure>

Same Jira issue in Secoda:&#x20;

<figure><img src="../../../.gitbook/assets/Screenshot 2024-05-09 at 4.40.27 PM.png" alt=""><figcaption><p>Example Jira issue after extraction by Secoda</p></figcaption></figure>
