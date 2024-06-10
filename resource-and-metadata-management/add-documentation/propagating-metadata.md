---
description: This section will go over how to propagate properties between resources.
---

# Propagation

## Introduction

Secoda offers a robust feature that allows you to copy properties from one resource to related resources within your workspace. This can streamline the management of properties across related resources.

## Steps to Propagate

1. **Select the Resource:**
   * In the Catalog, identify the resource that contains the properties you wish to propagate. Check the box next to the resource to select it.
2. **Initiate Propagation:**
   * Click the three-dot Commands button.
   * Choose "Propagate" from the menu.
3. **Choose Properties:**
   * Select the specific properties you would like to propagate from the source resource, like Owners and Tags.
4. **Select Target Resources:**
   * Specify which related resources should receive the properties. You can filter for these resources by:
     * Exact Name
     * Similar Name
     * Downstream Lineage
5. **Configure Propagation Settings:**
   * You can select to propagate to one, multiple, or all related resources. Similarly, choose to apply one or multiple properties as needed.
   * Decide whether to override existing properties on the target resources:
     * **'Override existing properties' checked:** The selected properties will replace any existing properties on the target resources.
     * **'Override existing properties' unchecked:** Properties will only be added on the target resources that are currently empty.

#### Additional Options and Considerations

* **Bulk Selection:** If you need to propagate properties to several resources, consider using the 'Select All' option for efficiency.
* **Verification:** After propagation, verify that the properties have been correctly applied to the target resources. This can help ensure consistency and accuracy across your data ecosystem.

By following these steps, you can effectively manage and synchronize documentation across various resources in your Secoda workspace, enhancing data governance and usability.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/e5bf1716-a7fe-47b0-b6df-86db972a5c9e.gif" alt=""><figcaption></figcaption></figure>

Want to see this feature in action? Watch the Loom video below, or send us a message!

{% embed url="https://www.loom.com/share/61e86eaa1be34c7c97df6b7adf456f63" %}
Loom Video showing how to propagate metadata.
{% endembed %}
