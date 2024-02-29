---
description: >-
  Secoda is built to be collaborative, so there's a number of ways to share
  content and resources with other people.
---

# Sharing Resources

## **How to share resources in Secoda**

There are a few different ways that you can organize permissions in Secoda. Entities will inherit permissions from their parent, so if you give someone access to a Team, they will have access to all of the resources within that Team. If you give someone access to a Collection, they will have access to all of the resources within the Collection. If you give someone access to a resource, they will have access to that resource only.

### Teams permissions

[teams.md](../teams.md "mention") are the highest level of organization in Secoda. You can create teams for different departments, projects, or any other way that makes sense for your organization. You can then assign resources to teams, and all members of that team will have access to those resources.

### Collection permissions

[collections-1.md](../../features/collections-1.md "mention") are a way to organize your resources within a team. You can create collections for different projects, or any other way that makes sense for your organization. You can then assign resources to collections, and all members of the Team that collection is in will have access to those resources.

### Group permissions

[groups.md](../groups.md "mention") are a way to organize the members within your workspace. It's common to create groups so that it's easier to assign [ownership](../../resource-and-metadata-management/assigning-owners.md) at the Group level, or add Groups to Teams instead of individually adding users to a Team one-by-one.

### Entity-level permissions

You can edit inherited permissions (permissions based on Teams) by clicking **Share** in the top right of your resource.

<figure><img src="../../.gitbook/assets/Screenshot 2024-02-27 at 4.42.23 PM.png" alt=""><figcaption></figcaption></figure>

Clicking **Share** opens up existing Permissions (Image 1). In the case below, the Collection is shared with all users in the General Team.&#x20;

To remove select users from viewing this Collection, but keep them in the Team, you can click "Can read" and select "Remove access" (Image 2).&#x20;

After removing the user, you'll see "Reset permissions" appear (Image 3). This button is helpful if this was done in error, or if you'd like to re-open up access to those users.&#x20;

<div>

<figure><img src="../../.gitbook/assets/Screenshot 2024-02-27 at 4.43.22 PM (3).png" alt=""><figcaption><p>Image 1</p></figcaption></figure>

 

<figure><img src="../../.gitbook/assets/Screenshot 2024-02-27 at 4.57.00 PM (3).png" alt=""><figcaption><p>Image 2</p></figcaption></figure>

 

<figure><img src="../../.gitbook/assets/Screenshot 2024-02-27 at 4.51.38 PM (3).png" alt=""><figcaption><p>Image 3</p></figcaption></figure>

</div>

Clicking **Copy link** copies the resource's unique URL to your clipboard so that you can share it with whoever you want. Still, only people with access to the resource can see it.

{% hint style="warning" %}
If a parent document or a Collection has custom entity-level permissions set, users who are not in that permissions set will not be able to access anything nested within it.&#x20;

Make sure that when you're sharing a resource with someone, if it's nested in a Collection or under a Parent document, that parent resource permissions include the user you're hoping to share it with.
{% endhint %}
