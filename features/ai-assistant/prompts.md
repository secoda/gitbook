---
description: See below for prompt examples to use in your workspace.
---

# Prompts

### Data Analyst:&#x20;

1. How can I query {insert table name}?
2. What is downstream of {insert table name}?
3. What is downstream of {insert column name}?
4. What are the primary data sources used in the {insert specific topic} dataset?
5. Analyze the data lineage of the {insert table name} table.
6. What table is used to for the {insert KPI}?
7. Identify any query optimizations or best practices for the "{insert specific topic, e.g., sales performance}" dataset.
8. Search for all queries related to {insert specific metric or subject, e.g., customer churn rate}.
9. Find all resources related to debugging or troubleshooting common query errors in the "{insert data source, e.g., BigQuery}" platform.
10. Look for a sample query to calculate the "{insert specific business objective, e.g., month-over-month growth}" metric.
11. What does {insert query} do?
12. What does {insert LookML code} do?
13. What does {Insert Python} do?
14. Analyze the metadata of the {insert table name} table to identify the most frequently accessed columns.
15. Determine the average size of tables in the database based on their metadata.
16. Investigate the metadata to find tables with missing or incomplete documentation.
17. Analyze the metadata to find tables with high cardinality columns that may impact query performance.
18. Write detailed descriptions for each column in the {insert table name}, including data type, meaning, and allowed values.
19. Develop a comprehensive metadata glossary that defines common terms, acronyms, and abbreviations used in the organization.
20. Document the metadata lineage for a specific data pipeline, showcasing the flow of data from source systems to the final output.

### Data Engineer:

1. Show the schema and column details for a particular table
2. What does {insert column name} mean?
3. Where does {insert column name} exist?
4. What is {insert column name} related to?
5. Show the primary key and foreign key relationships for a particular table.
6. Write a dbt model for {insert table name}
7. Write a SQL query for {insert KPI} analysis
8. Write me LookML code based on my {insert KPI}
9. Write me Python code based on my {insert table} to calculate {insert KPI}
10. Fix this query: {insert query}
11. View details on the {insert ETL platform, e.g., Apache Airflow} job "{insert job name}."
12. Who created this query: {insert query}
13. Write .yml documentation for my dbt model
14. Write .md documentation for my dbt model using docs block format
15. Write documentation for the {insert specific topic, e.g., sales performance} dataset, including its structure, data sources, and usage guidelines.
16. Create a user guide for querying the {insert table name}, providing step-by-step instructions and examples.
17. Document the data dictionary for the {insert specific topic} dataset, including definitions and descriptions of each column.
18. Prepare a documentation template for documenting dashboards, including their purpose, audience, and data sources.
19. Write documentation on troubleshooting common query errors in the {insert data source, e.g., BigQuery} platform, including error messages and potential solutions.

### Data Governance:

1. Which tables contain PII?
2. Which dashboards contain PII?
3. Which columns contain PII?
4. Which table is stale?
5. Which table hasn’t been queried in over 3 months?
6. What table is not documented / has no description?
7. What dashboard is not documented?
8. What does {insert employee name} own?
9. What PII lineage exists downstream of {insert table name}?
10. How can I ensure data consistency and integrity if I need to make changes to the {insert column name} or its structure?
11. What are the potential risks and consequences of removing the {insert column name} column from the customers table?
12. Are there any workarounds to drop the {insert column name} column without impacting reporting and data analysis?
13. How is {insert column name} used as a foreign key in the database?
14. Can you provide examples of tables that rely on the {insert column name} column?
15. Can you explain the importance of {insert column name} in terms of data lineage?
16. Identify the most utilized database indexes based on metadata analysis.
17. Write a comprehensive data dictionary for the {insert specific topic} dataset, covering all relevant tables and their metadata.
18. Create documentation for the metadata catalog, including its purpose, structure, and usage guidelines.
19. Develop a data lineage diagram documenting the flow of data from its source to the destination tables.
20. Document the metadata standards and conventions followed in the organization.

### Data Leadership:

1. Recommend the most suitable dashboard to monitor {insert KPI}.
2. Suggest the relevant stakeholders to discuss {insert KPI} analysis with.
3. Find resources related to revenue forecasting within the organization.
4. Show the description of the {insert dictionary term} in the data glossary.
5. Identify the data sources used to calculate the {insert KPI}.
6. Analyze the data quality issues impacting revenue reporting.
7. Find examples of data visualizations for presenting {insert KPI} insights.
8. Provide guidelines for documenting a dbt model in YAML format.
9. Explain the purpose and usage of a particular dbt model in Markdown format.
10. Describe the impact of {insert dictionary term} on data governance and compliance
11. Identify the data sources that contribute to the customer acquisition funnel.
12. Show the trend of customer retention over the past six months.
13. Who is responsible for data privacy and compliance within the organization?
14. Find resources on data strategy and roadmap development.
15. What are the current data quality issues affecting our decision-making process?
16. Provide insights on the impact of data analytics in improving operational efficiency.
17. Identify the data sources and methodologies used for forecasting sales revenue.
18. Show the correlation between marketing spend and customer acquisition metrics.
19. What data-driven initiatives can be implemented to improve customer experience?
20. Search for the metadata catalog that contains details about {insert specific topic, e.g., data quality rules}.

### The prompts are endless! Let us know which ones you've found useful.
