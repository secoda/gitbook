---
description: >-
  Enhance your data quality with Secoda's DQS: A systematic tool to measure,
  track, and improve data quality.
---

# Data Quality Score

{% hint style="info" %}
**The Data Quality Score feature is currently under development.** Sign up for [beta access here](https://tally.so/r/nG1aRL) to be among the first to explore its capabilities!
{% endhint %}

## Overview

The Data Quality Score (DQS) in Secoda offers a comprehensive scoring system that evaluates your data's quality. Focused initially on tables, DQS not only helps teams understand their data quality but also provides actionable steps to improve their scores over time. It aggregates scores across several categories to deliver a comprehensive total out of 100 points.

## Benefits of DQS

* **Data Producers**: Offers actionable steps and clear metrics to measure data quality, helping to address and reduce technical debt.
* **Data Consumers**: Improves data discoverability and trustworthiness with transparent quality indicators.
* **Governance**: Supplies a measurable metric to guide data governance investments, promoting a high standard of data quality.

Access to DQS motivates both data producers and consumers to uphold high data quality standards, fostering a culture of continuous improvement and accountability within your organization.

## Enabling DQS

By default, DQS is enabled in all workspaces. Admins can disable it in the Quality Score settings.

Consider adjusting the **Resource filter rules** to selectively include or exclude specific resources from the DQS calculations. For instance, you might exclude resources from your 'dev' database, which are often incomplete and could skew the overall quality score.

<figure><img src="../.gitbook/assets/Screenshot 2024-06-27 at 2.26.29 PM.png" alt=""><figcaption><p>DQS Settings</p></figcaption></figure>

## Accessing and Using DQS

### **Table-Level Scores**

1. **Navigate to a Table**: Go to the resource page of any table in your workspace.
2. **Open the Quality Tab**: Find the 'Quality' tab where the DQS is displayed.
3. **View Score Details**: Check the overall score and explore detailed breakdowns for each category.
4. **Improve Scores**: Click on specific categories to see actionable steps to enhance scores.

<figure><img src="../.gitbook/assets/Kapture 2024-06-18 at 17.03.45.gif" alt=""><figcaption><p>Table DQS</p></figcaption></figure>

### **Tracking Changes with Analytics Reports**

1. **Open the Analytics Dashboard**: Head to the Analytics section of Secoda.
2. **Create a Quality Score Report**: Use the "Add report" button to set up a new report focused on DQS.
3. **Customize Your View**: Apply filters, such as by Team, to pinpoint areas needing data quality improvements.

<figure><img src="../.gitbook/assets/Kapture 2024-06-18 at 17.06.08.gif" alt=""><figcaption><p>DQS in Analytics</p></figcaption></figure>

### **Search and Catalog Filters**

In the Search and Catalog views, you can [filter](filters.md) resources based on their Data Quality Score. The available quality filters are:

* **Is not set:** No score has been assigned.
* **Good:** Represents a high-quality score.
* **Moderate:** Indicates average quality.
* **Poor:** Shows a low-quality score.

These filters help you quickly identify and prioritize areas for improvement directly from your search results or catalog listings.

<figure><img src="../.gitbook/assets/Kapture 2024-06-18 at 17.29.14.gif" alt=""><figcaption><p>Filtering on Quality</p></figcaption></figure>

### **Automations for DQS**

Create an Automation to automatically apply actions based on the DQS of each table. For instance, when a table achieves a "Good" quality score, the system can automatically mark it as "Published" and "Verified." This helps users quickly identify which tables are confirmed as reliable and ready for business use.

<figure><img src="../.gitbook/assets/Screenshot 2024-06-27 at 3.03.13 PM.png" alt="" width="502"><figcaption><p>DQS Automation</p></figcaption></figure>

### **Adding a DQS Homepage Widget**

1. **Customize Your Homepage**: Navigate to your personal or team-level homepage settings.
2. **Add the DQS Widget**: Select the DQS widget to add it to your homepage.
3. **Access DQS Instantly**: Enjoy quick and easy access to your data quality scores directly from the homepage.

<figure><img src="../.gitbook/assets/Kapture 2024-06-18 at 17.09.02.gif" alt=""><figcaption><p>DQS on the Homepage</p></figcaption></figure>

## Scoring Categories

DQS consists of four main dimensions, each reflecting essential aspects of data quality:

**1. Stewardship (25 Points)**

* **Ownership (10 Points)**: Full points if the table has an owner; otherwise, it scores 0.
* **Tagged (10 Points)**: Full points if the table has been tagged (e.g., PII, Verified); no tags scores 0.
* **Questions & Answers (5 Points)**: Points awarded based on the percentage of Questions on the table with answers. If no questions have been asked, full points are awarded.

**2. Usability (25 Points)**

* **Resource Description (10 Points)**: Full points if the table has a description; no description scores 0.
* **Column Descriptions (10 Points)**: Points awarded based on the percentage of columns with descriptions.
* **Schema Description (5 Points)**: Full points if the table schema has a description; no description scores 0.

**3. Reliability (15 Points)**

* **Freshness Set (5 Points)**: Full points awarded if a freshness monitor or SLA is defined; otherwise, it scores 0.
* **Freshness Achieved (10 Points)**: Full points if the data freshness is within the expected period; otherwise, it scores 0.

**4. Accuracy (35 Points)**

The Accuracy score integrates results from dbt tests or Secoda Monitors, with future plans to include tools like Monte Carlo and Great Expectations.

* **Nullness (10 Points)**:&#x20;
  * 5 points awarded if a nullness test is configured for the table; otherwise, it scores 0.
  * Points awarded based on the percentage of passing nullness tests.
* **Uniqueness (10 Points)**:&#x20;
  * 5 points awarded if a uniqueness test is configured for the table; otherwise, it scores 0.
  * Points awarded based on the percentage of passing uniqueness tests.
* **Cardinality (10 Points)**:&#x20;
  * 5 points awarded if a cardinality test is configured for the table; otherwise, it scores 0.
  * Points awarded based on the percentage of passing cardinality tests.
* **Other Tests (5 Points)**: Additional points based on the percentage of other tests passing.

## Feedback

We welcome your suggestions for enhancing DQS. Please contribute your ideas on our [feedback board](https://www.feedback.secoda.co) to help us evolve this tool to better meet your needs.
