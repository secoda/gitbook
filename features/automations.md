---
description: >-
  Automate repetitive tasks by defining rules that bulk edit your metadata at
  scale
---

# Automations

Users can create rule-based automations at scale and update metadata and documentation in bulk. This Zapier-like feature will save your team an invaluable amount of time!

You can update the following resource metadata using Automations:

* Tags
* Owners
* Descriptions
* Verification
* Teams
* Collections
* Subscribers

{% hint style="info" %}
This list will expand over time, to eventually automate all the editable metadata that is included as part of your resource documentation.
{% endhint %}

## Creating an Automation

#### Step 1: Create a new Automation in Secoda

1. Find and click into Automations in the left side bar under Monitors.
2.  Click Add Automation, which will give you the option to start from scratch or choose from our list of templates.

    <figure><img src="../.gitbook/assets/Screenshot 2024-02-08 at 4.30.19 PM.png" alt=""><figcaption></figcaption></figure>
3.  Choosing a template will set up the filters and settings for you, while starting from scratch will open a new automation template for you to fill out.

    <figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/cd99248e-078a-4168-b32b-afb6839768c9.png" alt=""><figcaption></figcaption></figure>
4. Enter a title and description of the task to be accomplished, for example "Update tags".

#### Step 2: Set up rules as filters

1. For each filter you'd like to add, select **Add Filter** and add the metadata you'd like to filter for.&#x20;
2. Next, you must define how you'd like to filter on this metadata. Should it be an exact match, contain a term, etc.
3. If you have more than one filter, click the blue **all** button to choose either **all** or **any**. **All** will implement `AND` logic among the filters, while **any** will logically `OR` the criteria.

#### Step 3: Select the actions to be performed based on the rules above

1. Select Add Property and add which properties you'd like to be updated with the automation.&#x20;
2. To set a matching condition for the filters, click the blue **self** button to select which resources you'd like to be edited with the automation. These can be the same resources defined in the previous steps (self), their children resources (child) or their parent resources (parent).
3. Choose whether or not you'd like to Override existing metadata with these actions, using the check box :ballot\_box\_with\_check:.

{% hint style="info" %}
The "Override existing metadata" button is **additive** for the list properties like Owners, Tags, and Collections but it will completely replace the properties like Description, PII, and Verified.

For example, if you have an Owner set on a table that was previously brought over from the source (or added manually in Secoda) and then you create an Automation that tags the same resource with a different Owner, both Owner's names will persist.
{% endhint %}

#### Step 4: Run the Automation

1. Under the **Actions** drop down, you can click Turn on or Delete.
2. Configure the scheduling so that this Automation runs on a set cadence. Automations can run hourly, daily or weekly.

## Example Automations

<div data-full-width="true">

<figure><img src="../.gitbook/assets/Screenshot 2024-03-15 at 11.15.58 AM (1).png" alt=""><figcaption><p>Create Popular Snowflake tables Collection</p></figcaption></figure>

 

<figure><img src="../.gitbook/assets/Screenshot 2024-03-15 at 1.52.31 PM.png" alt=""><figcaption><p>Assign owners to Questions</p></figcaption></figure>

 

<figure><img src="../.gitbook/assets/Screenshot 2024-03-15 at 11.16.55 AM (1).png" alt=""><figcaption><p>Apply descriptions to similarly named resources</p></figcaption></figure>

</div>

<div data-full-width="true">

<figure><img src="../.gitbook/assets/Screenshot 2024-03-15 at 11.14.42 AM (1).png" alt=""><figcaption><p>Verify documented Tableau assets</p></figcaption></figure>

 

<figure><img src="../.gitbook/assets/Screenshot 2024-03-15 at 11.15.04 AM (1).png" alt=""><figcaption><p>Add Stripe assets to Sales Team</p></figcaption></figure>

 

<figure><img src="../.gitbook/assets/Screenshot 2024-03-15 at 11.15.38 AM (1).png" alt=""><figcaption><p>Tag columns as PII</p></figcaption></figure>

</div>

#### Adding Tags to Children

In the example below, you'll see an Automation that automatically updates the children of resources that are tagged with a "Warning" tag, with that same tag. This will be super time-saving with tables and columns, for example. If I bring in tables that already have a set tag, but the columns within do not yet, this automation will identify those columns and automatically tag them for me.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/34033212-a6cf-446d-8530-11053f328ad5.png" alt=""><figcaption></figcaption></figure>
