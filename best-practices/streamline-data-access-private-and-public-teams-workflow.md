---
description: >-
  Check out this workflow for managing metadata access in your workspace by
  using Teams.
---

# Streamline data access: Private and public teams workflow

Hoping to set up your workspace so that only the right users have access to work-in-progress resources? So that business users are only viewing the most up-to-date, Verified, resources?&#x20;

Consider setting up [Private and Public Teams ](../user-management/teams.md)and only flow resources into a Public team once they are approved and tagged as "Verified". Viewers can still search and discover resources in that Private team, and request access to the metadata.&#x20;

## How to set this up

1. Set up a [Private team](../user-management/teams.md#team-settings) that only certain users have access to&#x20;
   * A Private team means that users must be invited by an Admin to accessing the resources in this team.&#x20;
   * This Private team should be shared with your data team, the Admins/Editors in your workspace, SMEs, or whoever you believe is approved to viewing and editing the "unpolished" data resources.
   * Add all of your new, "Draft", or work-in-progress resources into this team.&#x20;
2. Set up a Public team that all users have access to&#x20;
   * A Public team means that anyone can join this Team and access the resources added to it.&#x20;
   * Add all users, including end-users, to this team.
   * Add all of your "Published"/Verified resources to this team, so that users know that these are approved by your team and ready to be used.
3. Automations can help automatically move resources to the Public and Private teams, instead of doing this manually. Here are some examples:
   1. **Automation 1**: All new resources coming into Secoda through the integrations get added only to the Private team
      * This ensures that all new resources are getting approved before being exposed to end users
      *

          <figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/b77fa7ce-0ca8-4ed2-95a9-6dbc7d0c7ecc.png" alt=""><figcaption></figcaption></figure>
      * The users in that Private Team can edit the resource documentation and complete a[ verified workflow](verifying-resources-workflow.md) (optional) to verify the resource.
   2. **Automation 2:** All resources that have a description and owner set, should be tagged as Verified, marked as Published, and get added to the Public team for end-user consumption.
      * Note: You can choose to define Verification differently than "having a description and owner", this is just an example.&#x20;
      * This automation ensures that resources are tagged as Verified, Published, and made accessible to business users in the Public team.
      *

          <figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/8bdd5cf8-5478-429d-8d1a-1120a9c95046.png" alt=""><figcaption></figcaption></figure>

