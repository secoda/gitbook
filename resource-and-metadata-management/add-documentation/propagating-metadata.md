---
description: This section will go over how to propagate properties between resources.
---

# Propagation

## Introduction

Secoda offers a robust feature that allows you to copy properties from one resource to related resources within your workspace. This can streamline the management of properties across related resources.

If you'd like to Automate this process even further, check out [automations-use-cases.md](../../features/automations/automations-use-cases.md "mention") for some examples.

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

{% embed url="https://www.loom.com/share/ff571a8bb859466f8571fec8d041dcf4" %}
