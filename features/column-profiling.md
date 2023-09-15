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

## **How to run column profiling** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

You're able to view the distribution of your data, the column count, and how many unique columns you have. And, if you hover over the distribution visualization, you can see the distribution percentage and what the column name is.

Wondering how up to date the column profile is? Secoda shows this on top of the table in the right hand corner.

![](https://secoda-public-media-assets.s3.amazonaws.com/Group%20824%20\(1\).png)

![Results of the column profiler](https://secoda-public-media-assets.s3.amazonaws.com/Screen%20Shot%202022-08-10%20at%2010.38.38%20AM.png)

![Double click on the results of the column profiler for more information](https://secoda-public-media-assets.s3.amazonaws.com/Screen%20Shot%202022-08-10%20at%2010.38.45%20AM.png)

## How it works

Column profiling runs a `SELECT` query directly on the database/data warehouse, processing the data to determine the Minimum, Maximum, Range, etc of the columns. The processed data will **not** be saved. As soon as the calculations are complete, we save the metadata results, but the data itself that the calculation is done on is not persisted anywhere in our database.

{% hint style="info" %}
Not using Secoda to manage your data documentation yet? Sign up for free [here](http://app.secoda.co/) 👈
{% endhint %}
