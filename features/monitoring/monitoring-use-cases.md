---
description: >-
  Discover how Secoda users implement Monitoring use cases to boost data
  integrity and streamline processes at their organizations.
---

# Monitoring Use Cases

There are numerous ways to utilize Monitors within the Secoda UI to enhance operational efficiency and data quality. The following use cases demonstrate how various monitoring types can be applied effectively across diverse industries and business functions.

1. **Row Count Monitor**
   * **Use Case: Daily Transaction Records**
     * **Scenario:** An e-commerce platform expects to process hundreds of transactions daily. Any significant deviation from this expected volume could indicate problems with the transaction processing system or data logging mechanisms.
     * **Implementation:** Configure a row count monitor on the `transactions` table to alert if the number of records per day does not match the expected count (e.g., less than 200 transactions per day). The threshold for alerts can be set based on historical data and expected variations.
     * **Outcome:** Helps quickly identify disruptions in transaction processing or data capture, allowing for swift troubleshooting and resolution to maintain business continuity.
2. **Freshness Monitor**
   * **Use Case: Inventory Management**
     * **Scenario:** A retail company needs to ensure that inventory data is updated regularly to accurately reflect stock levels.
     * **Implementation:** Set a freshness monitor on the inventory table to alert if the last update timestamp exceeds 24 hours, indicating potential issues in stock update processes.
     * **Outcome:** Guarantees that inventory data is current and reliable, helping to prevent stock-outs or overstock situations.
3. **Cardinality Monitor**
   * **Use Case: Inventory SKU Accuracy**
     * **Scenario:** In retail, each product is assigned a unique Stock Keeping Unit (SKU) to accurately track inventory across various locations. Effective management of this SKU data is critical to prevent inventory discrepancies that negatively affect sales and customer satisfaction.
     * **Implementation:** Implement a cardinality monitor within the inventory database to ensure the number of unique SKUs matches expected levels. This monitor alerts to any significant changes, such as unexpected increases that may indicate duplicate entries or decreases that could point to data losses or entry mistakes.
     * **Outcome:** Ensures inventory levels are correct, enhancing order fulfillment accuracy and facilitating effective strategic planning.
4. **Maximum/Minimum Monitor**
   * **Use Case: Financial Transactions**
     * **Scenario:** A financial institution needs to track unusually high or low transaction values that could indicate errors or fraudulent activity.
     * **Implementation:** Set maximum and minimum monitors on the transaction value column to alert if transactions exceed or drop below predefined thresholds.
     * **Outcome:** Helps quickly identify and investigate outliers in transaction data for potential errors or fraud.
5. **Mean Monitor**
   * **Use Case: Call Center Performance**
     * **Scenario:** A call center tracks the average call duration as a measure of customer service efficiency.
     * **Implementation:** Use a mean monitor on the call duration column to alert if the average time significantly deviates from the norm, which could indicate issues with call handling or system problems.
     * **Outcome:** Ensures consistent customer service and helps identify areas for process improvement.
6. **Unique Percentage Monitor**
   * **Use Case:** **SaaS User Management**
     * **Scenario:** In a SaaS platform, each user account ID should be unique to ensure individual access and prevent unauthorized multiple account usage.
     * **Implementation:** Implement a unique percentage monitor on the user ID column to ensure that nearly 100% of the entries are unique.
     * **Outcome:** Maintains the integrity of the user management system by preventing duplicate account creations, enhancing security and user experience.
7. **Nullness Monitor**
   * **Use Case: Customer Contact Information**
     * **Scenario:** In a customer relationship management (CRM) system, contact details such as phone numbers and email addresses are critical for communications. These fields should never be null.
     * **Implementation:** Set a nullness monitor on the phone number and email columns of the customer table. Configure the monitor to alert if any null values are detected, indicating issues in data collection or integration processes that need immediate rectification.
     * **Outcome:** Ensures that all customer records are complete, supporting effective communication and customer service operations.
8. **Custom SQL Monitor**
   * **Use Case: Compliance Checks**
     * **Scenario:** A company needs to comply with industry regulations requiring specific checks against database entries.
     * **Implementation:** Create a custom SQL monitor that runs a query to verify compliance with these regulations. The query might check for the presence of necessary data fields or validate relationships between data entries.
     * **Outcome:** Ensures continuous compliance with regulations and helps avoid potential legal or financial penalties.
