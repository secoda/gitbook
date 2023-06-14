# Maintain your Resources

Now that your data is in Secoda, you can edit your metadata and add documentation in a few different ways.

{% hint style="info" %}
Secoda creates a unique ID for each resource using the Integration name, Database name, and Resource title.&#x20;

E.g. a column named <mark style="background-color:blue;">orders</mark>, in the <mark style="background-color:blue;">sales</mark> database of a <mark style="background-color:blue;">Snowflake</mark> integration would have an ID of <mark style="background-color:blue;">snowflake.sales.orders</mark>.

To ensure changes in your CSV are reflected as updates in Secoda, instead of net new resources, the **three fields must not change.**&#x20;

Any changes to these three fields will result in a new ID, and create a new resource.&#x20;
{% endhint %}

### Maintain a Master CSV

If you are maintaining all your resources in a CSV, and have not disabled auto staling, any changes in the CSV will reflect in Secoda when you upload the CSV next time around. This means that missing resources in the CSV, will stale the resource in Secoda (so it will no longer show up in the UI).

If you'd like to the descriptions to always come from the CSV, make sure you toggle the Descriptions toggle on.

### Edit in Secoda

You can use Secoda's UI to make edits to the resources. All the ways to do this can be found in the [Resource and Metadata Management](../../resource-and-metadata-management/) and [Features](../../features/).

You can delete resources extracted from Custom Integrations in the UI by clicking on the three dots in the top right corner, and then clicking Delete.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/Screenshot%202023-06-09%20at%203.25.13%20PM.png" alt="" width="308"><figcaption></figcaption></figure>

### Edit in CSV Export

If you'd like to use a new CSV to edit metadata, you can export your resources using the [Import and Export](../../resource-and-metadata-management/import-and-export-data.md) feature in Secoda and edit metadata there. **This is not the same as a CSV upload for an integration extraction, and is only meant to metadata editing.**

Metadata edited in this CSV will take precedence over what is in the UI.
