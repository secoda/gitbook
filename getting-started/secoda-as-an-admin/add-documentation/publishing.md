---
description: >-
  Secoda is built with functionality that allows you to "publish" your workplace
  once you feel it is ready for viewers to see.
---

# Publishing

## **About Publishing** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

### **Understanding Status**

* Each resource in Secoda is marked with a "Status" indicating whether it is "Published" or "Draft".
* **Auto-Publish Setting:** Admins can configure settings to automatically set all new or imported resources to "Published" or "Draft". If auto-publish is enabled, all resources become visible to editors, viewers, and guests within their respective teams upon creation.

### **Managing Resource Visibility**

* **Draft Resources:** Admins and editors can move resources to the "Draft" status, which hides them from viewers and guests. This ensures that only fully prepared and relevant resources are accessible.
* **Auto-Publish Children:** If a table is set to "Published", all its columns are automatically published as well. The status for these columns is read-only, as demonstrated in the provided video:

<figure><img src="../../../.gitbook/assets/Kapture 2024-05-16 at 13.44.54 (2).gif" alt=""><figcaption><p>Read-only columns</p></figcaption></figure>

## Publishing settings

* **Toggle Auto-Publish:** This option, found under "Publishing" in the [Settings](../../../readme/secoda-as-an-admin/settings.md) menu, allows admins to decide whether new resources should automatically be "Published" or remain as "Draft" until manually changed.
* **Publish All Resources:** A single click on the 'Publish all resources' button will change the status of all draft resources in the workspace to "Published", including dictionary terms and documents.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/deb074f5-0a14-4066-b6d8-7b817f10c396.png" alt=""><figcaption><p>Publishing Settings</p></figcaption></figure>

## Steps to edit Publishing Status

1. Toggle on auto-publish, if desired.
2. Create new resources (Documents, Dictionary terms, Metrics etc) or bring in resources through connecting an integration.
3. Resources will automatically be labeled "Published" based on your auto-publish setting.
4. To set a resource to "Draft", double-click on the resource’s metadata and uncheck the appropriate option.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/48243ab1-eb09-4a37-83c3-436feb60d444.gif" alt=""><figcaption><p>Publish > Draft</p></figcaption></figure>

5. Use the [drag-and-drop feature ](../../../resource-and-metadata-management/add-documentation/bulk-editing-resources.md)to bulk edit multiple resources to "Draft" if they are not ready for wider visibility.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/5ddc2263-0032-4156-b437-971313eba254.gif" alt=""><figcaption><p>Bulk Draft</p></figcaption></figure>

6. To publish, either double-click the metadata and check "Published" or use the 'Publish all resources' button for bulk action.

## **Automating Publishing Status**

You can automate the process of setting the publishing status of your resources using Secoda's [automations.md](../../../features/automations.md "mention") feature. This capability allows you to configure rules that automatically set resources to "Published" or "Draft" based on specified conditions, streamlining how content is managed and shared within your workspace.

* **Configuring Automations:** To automate the publishing status, navigate to the Automations section in the left sidebar. Here, you can create a new automation or modify an existing one to include publishing actions.
* **Setting Properties:** Within the automation setup, you can choose 'Mark as Published/Draft' as a property to configure. This allows you to specify whether resources meeting your automation criteria will be automatically published or set to draft.

<figure><img src="../../../.gitbook/assets/image (28).png" alt=""><figcaption><p>Automating Publishing</p></figcaption></figure>

## Audit log

Admins can access the workspace audit log through Secoda [Settings](../../../readme/secoda-as-an-admin/settings.md). This log tracks all historical changes from the users in your workspace, whereas the [activity-log.md](../../../features/activity-log.md "mention") shows only changes to the specific resource that you're looking at.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/60cf2f4b-092b-42f2-9800-c46a2ef80be3.gif" alt=""><figcaption><p>Audit Log</p></figcaption></figure>
