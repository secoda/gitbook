---
description: >-
  Secoda provides high level insight into the columns of your datasets with
  Column Profiling.
---

# Column Profiling

Column profiling is a process of analyzing the characteristics and patterns of data within a specific column or field in a data set. Column profiling can be used to identify data quality issues and help organizations improve the quality of their data.

There are several benefits to column profiling for data quality:

1. Improved data accuracy: Column profiling can help identify data errors or inconsistencies within a specific column, allowing organizations to correct these issues and improve the overall accuracy of their data.
2. Enhanced data integrity: By identifying data quality issues within a specific column, organizations can take steps to ensure that data is being entered and stored correctly, improving data integrity.
3. Improved data governance: Column profiling can help organizations identify and address data quality issues, improving data governance and reducing the risk of errors or misunderstandings.
4. Enhanced data trustworthiness: By identifying and correcting data quality issues, organizations can improve the trustworthiness of their data, making it more useful and reliable for decision-making and analysis.

## How it works

Column profiling runs a `SELECT` query directly on the database/data warehouse, processing the data to quickly determine the distribution of your data including any null values, Minimum, Maximum, the column count, and number of unique columns.

The processed data will **not** be saved. As soon as the calculations are complete, we save the metadata results, but the data itself that the calculation is done on is not persisted anywhere in our database.

Profilers exclude PII data.&#x20;

The overall goal is to gain a feel for the quality of the dataset, and from here you can determine if you'd like to set monitors on certain tables/columns to further track data quality issues. Read more about our Monitoring capabilities here: [monitoring.md](monitoring.md "mention")

## **How to run column profiling** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

1.  Click Run profiler from any table (double check that we support column profiling for the integration in the nested[ metadata extracted docs](../integrations/)) \


    <figure><img src="../.gitbook/assets/image (2) (1) (1).png" alt=""><figcaption></figcaption></figure>
2.  See the distribution visualization and hover over for frequency info\


    <figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
3. Double click into the visualization too see additional details like min, max, mode, unique values etc.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/68ee1db9-dec8-4c1d-920a-32c857906923.gif" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Not using Secoda to manage your data documentation yet? Sign up for free [here](http://app.secoda.co/) 👈
{% endhint %}
