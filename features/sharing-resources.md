---
description: >-
  Learn how to precisely control access to individual resources in Secoda,
  enabling tailored sharing settings distinct from broader team-based
  permissions.
---

# Sharing

**Introduction**

Sharing individual resources effectively in Secoda allows for precise control over who can access specific data. This document focuses on direct resource sharing, distinct from broader permissions management covered in our separate [user-management](../user-management/ "mention") guide on using Teams, Collections, and Groups.

### Sharing Resources at the Individual Level

1. **Direct Resource Sharing:**
   * To share a specific resource, navigate to the resource within Secoda and click on the 'Share' button located at the top right corner. This opens the permissions panel for that resource.

<figure><img src="../.gitbook/assets/image (102).png" alt=""><figcaption></figcaption></figure>

* **Existing Permissions:** You will initially see the current access settings, which reflect any inherited permissions from the resource's parent entity (like a Team or Collection). See Image 1 below for reference, where the Collection is shared with all users in the General Team.

1. **Modifying Access:**
   * **Granting Access:** To allow a new user or group to access the resource, you can add them directly through the 'Share' panel. They will then be able to view or edit the resource based on the permissions you assign.
   * **Restricting Access:** To tailor access for specific users (or Groups) within a broader Team, you can adjust their permissions to more restrictive levels. For instance, you may want to change an Editor’s permissions to "Can read" only, limiting their ability to make changes while still allowing them to view the resource (Image 2).
   * **Removing Access:** If access needs to be removed from an individual, select their permission next to their name and choose "No access."&#x20;
2. **Copy Link:** For easy sharing, click 'Copy link' to copy the resource's unique URL to your clipboard. Note that only users with the necessary permissions can view the resource, even if they have the link.

<figure><img src="../.gitbook/assets/Screenshot 2025-08-18 at 2.53.59 PM.png" alt=""><figcaption><p>Image 3</p></figcaption></figure>

{% hint style="warning" %}
If a parent document or a Collection has custom resource-level permissions set, users who are not in that permissions set will not be able to access anything nested within it.

Make sure that when you're sharing a resource with someone, if it's nested in a Collection or under a Parent document, that parent resource permissions include the user you're hoping to share it with.
{% endhint %}

## Request access

If you come across a resource within Secoda Search that you'd like to access, you can request access. Once you click **Request access**, this will send a notification to the resource owner, or if there are no designated owner(s), the workspace admins. The notification will appear in their **Tasks** tab in Inbox.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/4a00b5b8-5b2c-4f9c-a32b-83e45af538d2.png" alt=""><figcaption></figcaption></figure>
