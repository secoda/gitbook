---
description: >-
  Learn how to precisely control access to individual resources in Secoda,
  enabling tailored sharing settings distinct from broader team-based
  permissions.
---

# Sharing Individual Resources

## **Introduction**

Sharing individual resources effectively in Secoda allows for precise control over who can access specific data. This document focuses on direct resource sharing, distinct from broader permissions management covered in our separate [..](../ "mention") guide on using Teams, Collections, and Groups.

### Sharing Resources at the Individual Level

1.  **Direct Resource Sharing:**

    * To share a specific resource, navigate to the resource within Secoda and click on the 'Share' button located at the top right corner. This opens the permissions panel for that resource.

    <figure><img src="../../.gitbook/assets/Screenshot 2024-02-27 at 4.42.23 PM.png" alt=""><figcaption></figcaption></figure>

    * **Existing Permissions:** You will initially see the current access settings, which reflect any inherited permissions from the resource's parent entity (like a Team or Collection). See Image 1 below for reference, where the Collection is shared with all users in the General Team.
2. **Modifying Access:**
   * **Granting Access:** To allow a new user or group to access the resource, you can add them directly through the 'Share' panel. They will then be able to view or edit the resource based on the permissions you assign.
   * **Restricting Access:** To tailor access for specific users (or Groups) within a broader Team, you can adjust their permissions to more restrictive levels. For instance, you may want to change an Editor’s permissions to "Can read" only, limiting their ability to make changes while still allowing them to view the resource (Image 2).&#x20;
   * **Removing Access:** If access needs to be removed from an individual, select their permission next to their name and choose "Remove access." This action can be reversed by clicking "Reset permissions," which reverts to the previous settings if the change was made in error or needs to be undone (Image 3).
3. **Copy Link:** For easy sharing, click 'Copy link' to copy the resource's unique URL to your clipboard. Note that only users with the necessary permissions can view the resource, even if they have the link.

<div>

<figure><img src="../../.gitbook/assets/Screenshot 2024-02-27 at 4.43.22 PM (3).png" alt=""><figcaption><p>Image 1</p></figcaption></figure>

 

<figure><img src="../../.gitbook/assets/Screenshot 2024-02-27 at 4.57.00 PM (3).png" alt=""><figcaption><p>Image 2</p></figcaption></figure>

 

<figure><img src="../../.gitbook/assets/Screenshot 2024-02-27 at 4.51.38 PM (3).png" alt=""><figcaption><p>Image 3</p></figcaption></figure>

</div>

{% hint style="warning" %}
If a parent document or a Collection has custom resource-level permissions set, users who are not in that permissions set will not be able to access anything nested within it.&#x20;

Make sure that when you're sharing a resource with someone, if it's nested in a Collection or under a Parent document, that parent resource permissions include the user you're hoping to share it with.
{% endhint %}
