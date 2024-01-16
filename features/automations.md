---
description: >-
  Automate repetitive tasks by defining rules that bulk edit your metadata at
  scale
---

# Automations

{% hint style="warning" %}
This feature is currently in beta testing. If you'd like early access to testing out these features, and help inform our improvements to it, you can sign up at [this link](https://www.secoda.co/blog/early-access-secoda-automations).
{% endhint %}

Automate documentation and keep it up to date by defining repetitive tasks with our Automations feature. Users can create rule-based automations at scale and update metadata in bulk. This Zapier-like feature will save your team an invaluable amount of time!

You can update the following resource metadata using Automations:

* Tags
* Owners

Note: we plan on expanding this list to make metadata documentation as automated as possible across your workspace!

## Creating an Automation

#### Step 1: Create a new Automation in Secoda

1. Find and click into Automations in the left side bar under Monitors.
2.  Click Add Automation, which will open a new automation template for you to fill out.&#x20;

    <figure><img src="../.gitbook/assets/Screenshot 2024-01-12 at 2.55.54 PM.png" alt=""><figcaption></figcaption></figure>
3. The default title will be "New Automation". Enter a new title describing the task to be accomplished, for example "Update tags".

#### Step 2: Set up rules as filters

1. Select **Add Filter** and add attributes you'd like to filter on. Right now these options are for Tag and Owner.&#x20;
2. Choose between contains, does not contain, et.c depending on what values you'd like to include.
3. Select the relevant values that you'd like to filter on.
4. (Optional) To add additional filters, click **Add filter** and follow the same steps above.
5. To set a matching condition for the filters, click the blue **all** button to choose either **all** or **any**. **All** will logically `AND` the criteria, while **any** will logically `OR` the criteria.

#### Step 3: Select the actions to be performed based on the rules above

1. Select Add Property and add which properties you'd like to be updated with the automation.
2. To set a matching condition for the filters, click the blue **self** button to select which resources you'd like to be edited with the automation. These can be the same resources defined in the previous steps (self), their children resources (child) or their parent resources (parent).
3. Choose whether or not you'd like to Override existing metadata with these actions, using the check box :ballot\_box\_with\_check:.

#### Step 4: Run the Automation

1. Under the **Actions** drop down, you can click Turn on or Delete.
2. Configure the scheduling so that this Automation runs on a set cadence which can be hourly, daily or weekly depending on your needs.

## Example Automation

In the example below, I've create an Automation that automatically updates the children of resources that are tagged with a "Warning" tag, with that same tag. This will be super time-saving with tables and columns, for example. If I bring in tables that already have a set tag, but the columns within do not yet, this automation will identify those columns and automatically tag them for me.

<figure><img src="../.gitbook/assets/Screenshot 2024-01-12 at 1.57.01 PM.png" alt=""><figcaption></figcaption></figure>
