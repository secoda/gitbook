---
description: Explore common use cases for Secoda's Automations features.
---

# Automations Use Cases

## Introduction

Secoda’s Automations feature allows you to streamline and automate repetitive data management tasks, enhancing efficiency and consistency across your workspace. This document outlines several practical use cases where Automations can significantly improve data governance and operational workflows.

## Verify documented resources

* **Objective:** Ensure that fully documented resources are automatically marked as Verified.
* **Setup:** This automation identifies resources that have both a complete description and an assigned owner. Once these criteria are met, the resources are automatically tagged as Verified.
* **Benefits:** Indicates to end users that the resources are verified and ready to use.

**Note:** The criteria for "fully documented" might vary across organizations! Configure the filters to align with your organization's standards.

<figure><img src="../../.gitbook/assets/Screenshot 2024-05-23 at 11.31.44 AM.png" alt=""><figcaption><p>Verify documented Tableau assets</p></figcaption></figure>

## Automate PII tagging

* **Objective:** Automatically tag columns containing personal identifiable information (PII) for privacy compliance.
* **Setup:** Identify columns with the title 'name' (or other keywords) and tag them as PII.
* **Benefits:** Enhances data protection measures, ensuring compliance with privacy regulations and improving data security.

<figure><img src="../../.gitbook/assets/Screenshot 2024-05-23 at 11.33.30 AM.png" alt=""><figcaption><p>Tag columns as PII</p></figcaption></figure>

## Propagate metadata to child resources

* **Objective:** Automatically propagate essential metadata, like ownership and tags, from parent resources to their child resources.
* **Setup:** Configure automations to apply metadata updates from table resources to associated child (column) resources, ensuring consistent metadata across related datasets.
* **Benefits:** Reduces redundant documentation tasks for similar resources.

<figure><img src="../../.gitbook/assets/Screenshot 2024-05-21 at 4.49.34 PM.png" alt=""><figcaption><p>Propagate metadata to children</p></figcaption></figure>

## Propagate descriptions to same named resources

* **Objective:** Standardize descriptions across all columns sharing the same name, ensuring consistency in metadata.&#x20;
* **Setup:** The automation scans for columns named identically across different tables, using a populated description from one column to update others. It targets columns, identifies matching titles, and applies the selected metadata—descriptions in this case.&#x20;
* **Benefits:** Streamlines the updating process, ensuring all similar resources have accurate and consistent descriptions without manual editing.

<figure><img src="../../.gitbook/assets/Screenshot 2024-05-23 at 11.14.25 AM.png" alt=""><figcaption><p>Propagate descriptions to same-name resources</p></figcaption></figure>

## Notify users of undocumented resources

* **Objective:** Ensure that users are promptly informed about resources lacking proper documentation.
* **Setup:** Set up notifications about resources that are identified as undocumented based on specific criteria. Notifications can be directed to specific users or broadcasted through your connected Slack channel.
* **Benefits:** Promotes timely documentation and increases data reliability and trustworthiness.

<figure><img src="../../.gitbook/assets/Screenshot 2024-05-21 at 4.45.42 PM.png" alt=""><figcaption><p>Send announcements about undocumented assets</p></figcaption></figure>

## Alert users of schema changes

* **Objective:** Notify stakeholders when changes occur in core schemas to keep them updated in real-time.
* **Setup:** Set the trigger to detect schema changes, then send an announcement/Slack notification/email to designated users detailing the changes.
* **Benefits:** Ensures timely updates to all relevant parties, automating these change notifications.&#x20;

<figure><img src="../../.gitbook/assets/Screenshot 2024-05-29 at 1.07.58 PM.png" alt=""><figcaption><p>Alert about schema changes</p></figcaption></figure>

## Tag resources for deprecation

* **Objective:** Automate the identification of outdated or irrelevant resources.&#x20;
* **Setup:** Flag resources that haven't been accessed or updated within a predefined period, tagging them as "Candidates for deprecation".&#x20;
* **Benefits:** Keeps the data ecosystem clean and focused, reducing clutter and focusing efforts on relevant, up-to-date resources.

<figure><img src="../../.gitbook/assets/Screenshot 2024-05-24 at 2.28.05 PM.png" alt=""><figcaption><p>Identify resources for deprecation</p></figcaption></figure>

## Publish documented tables

* **Objective:** Automatically publish tables that meet documentation standards.
* **Setup:** Configure automations to change the status of tables from 'Draft' to 'Published' once they meet predefined documentation criteria.
* **Benefits:** Ensures only fully documented tables are visible to Viewers, maintaining data quality and accessibility.

<figure><img src="../../.gitbook/assets/Screenshot 2024-05-23 at 11.37.03 AM.png" alt=""><figcaption><p>Publish documented resources</p></figcaption></figure>

## Apply descriptions to similarly named resources

* **Objective:** Standardize descriptions across resources that share similar names or characteristics to maintain consistency in metadata.
* **Setup:** The automation scans for resources with similar naming conventions (e.g., columns named "order" across different databases) and automatically applies a predefined description to these resources.
* **Benefits:** This automation ensures that all similar resources carry the same descriptive information, reducing confusion and enhancing the usability of the data.&#x20;

<figure><img src="../../.gitbook/assets/Screenshot 2024-05-23 at 11.40.00 AM.png" alt=""><figcaption><p>Apply descriptions to similarly named resources</p></figcaption></figure>

## Assign owners to Questions

* **Objective:** Automatically assign ownership to unresolved questions in Secoda.
* **Setup:** Identify questions using specific filters and automatically assign them to the appropriate team member.
* **Benefits:** Streamlines the process of question resolution, ensuring timely and effective answers to critical data queries.

<figure><img src="../../.gitbook/assets/Screenshot 2024-05-23 at 11.42.05 AM.png" alt=""><figcaption><p>Assign owners to Questions</p></figcaption></figure>

## Add resources to their relevant Team

* **Objective:** Automatically classify and add relevant tables to the relevant team for easier access.
* **Setup:** Filter tables by integration and schema, and assign them to the relevant team.
* **Benefits:** Optimizes resource management and improves team-specific data accessibility.

<figure><img src="../../.gitbook/assets/Screenshot 2024-05-23 at 11.43.46 AM.png" alt=""><figcaption><p>Add Stripe assets to Sales Team</p></figcaption></figure>

## Popular tables Collection

* **Objective:** Identify and collect frequently accessed Snowflake tables into a designated Collection.
* **Setup:** Set filters to identify Snowflake tables with external usage over a certain amount of queries.
* **Benefits:** Facilitates easier access and management of popular tables, enhancing data visibility and user productivity.

<div data-full-width="true">

<figure><img src="../../.gitbook/assets/Screenshot 2024-05-23 at 11.46.25 AM.png" alt=""><figcaption><p>Create Popular Snowflake tables Collection</p></figcaption></figure>

</div>

