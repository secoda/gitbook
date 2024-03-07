---
description: Best practices for how to use Search within Secoda
---

# Search

Search is super important to Secoda users and we are constantly improving the functionality to provide the best experience.

You can search for any data resource using Secoda's search, including tables, columns, collections, dictionary terms, documents, metrics and questions. You can search for terms in plain language, or by the table name and data source if you already know what you're looking for.

## How to Search

When you first click into Search, it'll show your workspace's Popular resources as well as your personal Recent searches.

{% hint style="info" %}
Popular resources in Secoda are calculated by summing the number of views in Secoda over the last 90 days, with the number of views/queries extracted from the source 24 hours from the extraction. Learn more about [Popularity](popularity.md).
{% endhint %}

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/904494a7-2d27-46b1-b403-1218e763ec72.gif" alt=""><figcaption></figcaption></figure>

You can also search directly from the Home page, [within the Catalog](search.md#search-within-the-catalog), or by typing `/` from any screen.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/a261d8b4-6b8e-464f-bebb-32ceb6eb9bc2.png" alt=""><figcaption></figcaption></figure>

## How Search works

The search strategy ranks results based on how closely they match your search term in different fields, using a priority system:

1. **Exact Title Match**: Finds resources where the title exactly matches your search term. This is highly prioritized, making it more important than other matches.
2. **Title Prefix Match**: Looks for resources where the title starts with your search term. It's slightly less important than an exact match but still prioritized.
3. **Phrase Match in Title**: Identifies resources where the title contains your search term as a phrase. This has a lower priority compared to exact and prefix matches.
4. **Phrase Match in Description**: Searches for your term as an exact phrase within the resources' description. It's less important than finding the phrase in the title.
5. **Phrase Match in Documentation**: Finds your term as an exact phrase within the resources' definition, having the lowest priority among phrase matches.
6. **Wildcard Match in Full Title**: Highly prioritizes resources where the full title contains your search term anywhere. This is given the highest importance of all, significantly more than any other match type.

In essence, resources that exactly match your term in the title are most preferred, followed by those where the term starts the title or appears as a phrase in the title, description, or definition. Documents with your search term anywhere in the full title are deemed most relevant.

## Search views

You are able to save search filters so that you can easily go back to common searches. These can be either personal to you, or at the Team level.

1. Click into Search and click the filters icon next to Relevance
2. Click + Create new view
3. Title the filter view, add which filters you'd like, and set the Team visibility
   * Note: If you leave the "Team visibility" section blank, these will only be saved to your personal space

Check out the video below for a step by step walkthrough!

{% embed url="https://www.loom.com/share/9dec6cfc5dae489884567c54596c7665?sid=55903669-0d5e-438d-ac3b-9b00a9eca52d" %}

## Search within the Catalog

Searching and filtering within the Catalog can be helpful when identifying resources that have not been documented. To filter for undocumented resources:

1. Click into Catalog
2. Click into the metadata that you'd like to filter for, for example Description
3. Check off "Blank" to show resources with no description filled out

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/46a60d90-5cc3-4840-84dd-ac03cb1d59df.gif" alt=""><figcaption><p>Filter for no Description</p></figcaption></figure>

In this same view, you can order your results by any metadata including Title, Database, Last Updated Date etc. Simply click the arrows next to the metadata you'd like to order by.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/e0647d4a-9d6e-4d7d-a58d-5433878f6208.gif" alt=""><figcaption><p>Order Catalog results</p></figcaption></figure>

## Search from the sidebar

Searching can be daunting if you’re not sure exactly what you’re looking for. We’ve tried to make it as seamless as possible by adding features to help filter down your search.

### Ask AI

The [Secoda AI](https://www.secoda.co/blog/transforming-data-discovery-using-secoda-ai)[ Assistant](ai-assistant/) improves user experience when searching for resources. Once you’ve enabled it, you can find the AI Assistant on the lefthand panel under Search. You can also Ask AI right from the main Search. This feature will be helpful for business users who might not know where to begin when looking at data. Read more about it [here](https://docs.secoda.co/features/ai-assistant).

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/877412ec-091c-458a-bf63-c5ea7b1c5c5d.gif" alt=""><figcaption></figcaption></figure>

### Sort

You’re able to sort by Relevance, Popularity, Last modified and Date created.

* Relevance is measured by your personal usage (tables, dashboards, docs that you’ve worked on and are relevant to you)
* Popularity is measured by how often a resource is clicked into in your workspace as well as how often it’s queried outside of the workspace (Read more about this [popularity.md](popularity.md "mention"))
* Last modified will show you the most recently _updated_ resources
* Date created will show you the most recently _created_ resources

<div align="center">

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/1cc2981a-a1a2-4a67-abf5-8df85caa5039.png" alt=""><figcaption></figcaption></figure>

</div>

### All filters

If you know what kind of resource you are searching for, you can filter down to that type in the All filter dropdown. There you will see every type of resources from Apps to Questions.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/Screenshot%202023-05-02%20at%205.00.40%20PM.png" alt=""><figcaption></figcaption></figure>

### Add filter

You can get even more granular with filters in the Add filter section. For example, if you are looking for all resources containing PII tags, this feature allows you to filter down your results.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/c8f1519a-12f7-4856-98a8-4dc11b8dc745.png" alt=""><figcaption></figcaption></figure>

### View

The view filter allows you to toggle on/off the different kinds of information related to the results from your search.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/759e542f-10a8-49b1-b048-77ee43965c8a.png" alt=""><figcaption></figcaption></figure>
