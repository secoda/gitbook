---
description: >-
  Automate repetitive tasks by defining rules that bulk edit your metadata at
  scale
---

# Automations

## Introduction

Automations in Secoda enable admins to set up rule-based operations that automate routine data management tasks, much like Zapier. This feature significantly saves time by automating updates to metadata and documentation, allowing teams to concentrate on more strategic activities and enhance productivity and accuracy in data management.

To see these in action, check out our document on example use cases here.

## Capabilities of Automations

Automations allow users to **update** a wide range of resource metadata, including:

* Tags (Custom, Verification, & Governance)
* Owners
* Documentation
* Descriptions
* Subscribers
* Status (Published, Draft)

Additionally, Automations can help **organize** workspace resources by moving them to:

* Teams
* Collections

**Communication** with users is also streamlined through Automations, enabling:

* Inbox notifications and announcements
* Email dispatches
* Slack messages

## Creating an Automation

**Step 1: Initiate an Automation**

1. Navigate to Automations in the left sidebar.
2. Click 'Create Automation' to start from scratch or select from a list of predefined templates.
   * **Using a Template:** Templates come with pre-configured filters and settings, which can be further customized.
   * **Starting from Scratch:** Allows for complete customization from the ground up.
     * Enter a title for the Automation, for example, "Update tags."
     * (Optional) Add a description and choose an icon for the Automation to help identify it easily in the future.

<figure><img src="../../.gitbook/assets/Screenshot 2024-02-08 at 4.30.19 PM.png" alt=""><figcaption><p>Creating a new Automation</p></figcaption></figure>

**Step 2: Set trigger**

* **Scheduled:** Set Automations to trigger on a specific schedule (hourly, daily, weekly) on a particular day and time.
*   **Schema Changes:** Automations trigger when changes are made to the specified schemas in the source (ex. a column has been added to a table).

    <figure><img src="../../.gitbook/assets/Kapture 2024-05-21 at 09.53.21 (1).gif" alt=""><figcaption><p>Setting the trigger</p></figcaption></figure>

**Step 3: Configure Rules as Filters**

1. Click '+Add Action' and select 'Filter resources' to begin adding filters.
2. Select filters and define the filtering logic (exact match, contains, is set, etc.).
3. To add more filters, click 'Add Filter' and select 'all' or 'any' to apply AND or OR logic across filters.
4.  (Optional) Add a Filter Group by selecting '+Add Action' and choosing between AND or OR logic.

    <figure><img src="../../.gitbook/assets/Kapture 2024-05-21 at 15.03.40.gif" alt=""><figcaption><p>Setting up rules and filter groups</p></figcaption></figure>

**Step 4: Define Actions**

1. Select '+Add Action' to select the actions or metadata properties to update. Choose from the following actions:
   * **Edit resources:**
     * Use the 'Resources' button to specify the scope of resources affected (resources, parent, children).
     * Click '+Add Property' to choose which metadata properties to update.
   * **Send announcement:**&#x20;
     * Select recipients and craft the messaging for an [Inbox](../data-inbox.md) announcement.
   * **Send email:**
     * Select recipients and craft the messaging for an email.
   * **Send Slack message:**&#x20;
     * Select Slack channels and compose the message to be sent.
   * **Propagate metadata:**
     * Specify the scope of resources to propagate metadata to relative to the filtered resources set earlier (Child resources, Parent resources, Resources with the same name).&#x20;
     * Specify the level of which you'd like to propagate metadata to: 1-4.
2. For Editing & Propagating Metadata: Choose whether or not you'd like to Override existing metadata with these actions, using the toggle.

{% hint style="info" %}
The "Override existing metadata" button is **additive** for the list properties like Owners, Tags, and Collections but it will completely replace the properties like Description, PII, and Verified.

For example, if you have an Owner set on a table that was previously brought over from the source (or added manually in Secoda) and then you create an Automation that tags the same resource with a different Owner, both Owner's names will persist.
{% endhint %}

<figure><img src="../../.gitbook/assets/Kapture 2024-05-21 at 15.09.04.gif" alt=""><figcaption><p>Propagating descriptions to children resources</p></figcaption></figure>

**Step 5: Run the Automation**

1. In the top right, choose 'Turn on automation' to activate.
2. (Optional) Use the three dot menu to 'Delete' the Automation.

<figure><img src="../../.gitbook/assets/Kapture 2024-05-21 at 15.11.07.gif" alt=""><figcaption><p>Delete, turn on, run Automation</p></figcaption></figure>
