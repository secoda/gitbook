# Snowflake Native App Monitoring Commands

While you can manage monitors using the Streamlit GUI, you can also create and manage monitors directly from a Snowflake worksheet using SQL commands. This guide provides a comprehensive overview of monitoring functionality available through SQL.

## Prerequisites

Before using the monitoring commands, ensure you've:

1. Successfully installed the Secoda Native Snowflake App
2. Connected to your Secoda instance 
3. Granted the necessary permissions to the application

{% hint style="warning" %}
The Secoda app needs appropriate permissions to monitor your data objects. Make sure to grant the required permissions before creating monitors.
{% endhint %}

## Granting Required Permissions

For each database, schema, and table you want to monitor:

```sql
-- Replace with your actual database, schema, and table names
GRANT USAGE ON DATABASE <your_database> TO APPLICATION secoda_app;
GRANT USAGE ON SCHEMA <your_database>.<your_schema> TO APPLICATION secoda_app;
GRANT SELECT ON TABLE <your_database>.<your_schema>.<your_table> TO APPLICATION secoda_app;
```

## Creating Monitors

The Secoda Native App supports several different monitor types, each tracking specific aspects of your data.

### Basic Monitor Creation

The simplest form of monitor creation requires only a few parameters:

```sql
CALL SECODA_APP.MONITORING.CREATE_MONITOR(
    MONITOR_KEY => 'users_row_count',     -- Unique identifier
    NAME => 'Users Table Row Count',      -- Display name
    METRIC_TYPE => 'row_count',           -- Type of metric to monitor
    TABLE_CATALOG => 'your_database',     -- Database name
    TABLE_SCHEMA => 'your_schema',        -- Schema name
    TABLE_NAME => 'your_table'            -- Table name
);
```

### Monitor Types

The Secoda Native App supports the following monitor types:

1. **Row Count**: Monitors the total number of rows in a table
   ```sql
   CALL SECODA_APP.MONITORING.CREATE_MONITOR(
       MONITOR_KEY => 'users_row_count',
       NAME => 'Users Table Row Count',
       METRIC_TYPE => 'row_count',
       TABLE_CATALOG => 'your_database',
       TABLE_SCHEMA => 'your_schema',
       TABLE_NAME => 'users'
   );
   ```

2. **Maximum Value**: Monitors the maximum value in a specified column
   ```sql
   CALL SECODA_APP.MONITORING.CREATE_MONITOR(
       MONITOR_KEY => 'users_max_age',
       NAME => 'Users Maximum Age',
       METRIC_TYPE => 'max',
       TABLE_CATALOG => 'your_database',
       TABLE_SCHEMA => 'your_schema',
       TABLE_NAME => 'users',
       COLUMN_NAME => 'age',
       THRESHOLDS_METHOD => 'manual',   -- Optional: 'auto' or 'manual'
       THRESHOLDS_MAX => 40,            -- Only used with 'manual'
       THRESHOLDS_MIN => 20             -- Only used with 'manual'
   );
   ```

3. **Minimum Value**: Monitors the minimum value in a specified column
   ```sql
   CALL SECODA_APP.MONITORING.CREATE_MONITOR(
       MONITOR_KEY => 'users_min_age',
       NAME => 'Users Minimum Age',
       METRIC_TYPE => 'min',
       TABLE_CATALOG => 'your_database',
       TABLE_SCHEMA => 'your_schema',
       TABLE_NAME => 'users',
       COLUMN_NAME => 'age'
   );
   ```

4. **Mean Value**: Monitors the average value in a specified column
   ```sql
   CALL SECODA_APP.MONITORING.CREATE_MONITOR(
       MONITOR_KEY => 'users_avg_age',
       NAME => 'Users Average Age',
       METRIC_TYPE => 'mean',
       TABLE_CATALOG => 'your_database',
       TABLE_SCHEMA => 'your_schema',
       TABLE_NAME => 'users',
       COLUMN_NAME => 'age'
   );
   ```

5. **Null Percentage**: Monitors the percentage of NULL values in a column
   ```sql
   CALL SECODA_APP.MONITORING.CREATE_MONITOR(
       MONITOR_KEY => 'users_null_percentage',
       NAME => 'Users with Null Account Balance',
       METRIC_TYPE => 'null_percentage',
       TABLE_CATALOG => 'your_database',
       TABLE_SCHEMA => 'your_schema',
       TABLE_NAME => 'users',
       COLUMN_NAME => 'account_balance',
       THRESHOLDS_METHOD => 'manual',
       THRESHOLDS_MAX => 10,            -- Alert if more than 10% nulls
       THRESHOLDS_MIN => 0
   );
   ```

6. **Cardinality**: Monitors the number of distinct values in a column
   ```sql
   CALL SECODA_APP.MONITORING.CREATE_MONITOR(
       MONITOR_KEY => 'users_distinct_ages',
       NAME => 'Distinct User Ages',
       METRIC_TYPE => 'cardinality',
       TABLE_CATALOG => 'your_database',
       TABLE_SCHEMA => 'your_schema',
       TABLE_NAME => 'users',
       COLUMN_NAME => 'age'
   );
   ```

7. **Unique Percentage**: Monitors the percentage of unique values in a column
   ```sql
   CALL SECODA_APP.MONITORING.CREATE_MONITOR(
       MONITOR_KEY => 'users_unique_usernames',
       NAME => 'Unique Username Percentage',
       METRIC_TYPE => 'unique_percentage',
       TABLE_CATALOG => 'your_database',
       TABLE_SCHEMA => 'your_schema',
       TABLE_NAME => 'users',
       COLUMN_NAME => 'username'
   );
   ```

8. **Custom SQL**: Monitors using a custom SQL query that returns a single numeric value
   ```sql
   CALL SECODA_APP.MONITORING.CREATE_MONITOR(
       MONITOR_KEY => 'users_active_count',
       NAME => 'Count of Active Users',
       METRIC_TYPE => 'custom_sql',
       TABLE_CATALOG => 'your_database',
       TABLE_SCHEMA => 'your_schema',
       TABLE_NAME => 'users',
       QUERY => 'SELECT COUNT(*) FROM your_database.your_schema.users WHERE is_active = TRUE'
   );
   ```

9. **Freshness**: Monitors how recent the data is based on a date/timestamp column
   ```sql
   CALL SECODA_APP.MONITORING.CREATE_MONITOR(
       MONITOR_KEY => 'users_data_freshness',
       NAME => 'Users Data Freshness',
       METRIC_TYPE => 'freshness',
       TABLE_CATALOG => 'your_database',
       TABLE_SCHEMA => 'your_schema',
       TABLE_NAME => 'users',
       COLUMN_NAME => 'signup_date'
   );
   ```

### Configuring Thresholds

You can set up thresholds in two ways:

1. **Automatic Thresholds**: The system automatically determines thresholds based on historical data
   ```sql
   THRESHOLDS_METHOD => 'auto'  -- This is the default if not specified
   ```

2. **Manual Thresholds**: You specify exact threshold values
   ```sql
   THRESHOLDS_METHOD => 'manual',
   THRESHOLDS_MAX => 1000,      -- Maximum acceptable value
   THRESHOLDS_MIN => 0          -- Minimum acceptable value
   ```

### Scheduling Monitors

You can configure when monitors should run:

```sql
CALL SECODA_APP.MONITORING.CREATE_MONITOR(
    -- Basic monitor parameters...
    SCHEDULE_CADENCE => 'daily',        -- 'hourly', 'daily', 'weekly', 'monthly'
    SCHEDULE_HOUR => 6,                 -- Hour of day to run (UTC)
    SCHEDULE_FREQUENCY => 1             -- Run every X periods (e.g., every 1 day)
);
```

## Managing Monitors

### Running Monitors

To manually run a monitor:

```sql
CALL SECODA_APP.MONITORING.RUN_MONITOR('monitor_key');
```

### Listing Monitors

To view all configured monitors:

```sql
SELECT * FROM SECODA_APP.MONITORING.LIST_MONITORS();
```

### Pausing and Resuming Monitors

To temporarily pause a monitor:

```sql
CALL SECODA_APP.MONITORING.PAUSE_MONITOR('monitor_key');
```

To resume a paused monitor:

```sql
CALL SECODA_APP.MONITORING.RESUME_MONITOR('monitor_key');
```

### Updating Monitors

To update an existing monitor (for example, changing thresholds):

```sql
CALL SECODA_APP.MONITORING.UPDATE_MONITOR(
    MONITOR_KEY => 'users_null_percentage',
    THRESHOLDS_METHOD => 'manual',
    THRESHOLDS_MAX => 20        -- Updated threshold
);
```

### Deleting Monitors

To delete a specific monitor:

```sql
CALL SECODA_APP.MONITORING.DELETE_MONITOR('monitor_key');
```

To remove all monitors:

```sql
CALL SECODA_APP.MONITORING.CLEAR_MONITORS();
```

## Complete Example

Here's a complete example that creates a test database and several monitors:

```sql
-- Create sample database and table
CREATE DATABASE IF NOT EXISTS tmp_demo_db;
USE DATABASE tmp_demo_db;
CREATE SCHEMA IF NOT EXISTS demo;
USE SCHEMA demo;

-- Create a sample users table
CREATE TABLE IF NOT EXISTS users (
    user_id NUMBER,
    username VARCHAR(255),
    age NUMBER,
    signup_date DATE,
    last_login TIMESTAMP,
    account_balance FLOAT,
    is_active BOOLEAN
);

-- Insert sample data
INSERT INTO users VALUES
    (1, 'john_doe', 25, '2024-01-15', CURRENT_TIMESTAMP(), 1250.75, TRUE),
    (2, 'jane_smith', 32, '2024-02-01', CURRENT_TIMESTAMP(), 3420.50, TRUE);

-- Grant necessary permissions
GRANT USAGE ON DATABASE tmp_demo_db TO APPLICATION secoda_app;
GRANT USAGE ON SCHEMA tmp_demo_db.demo TO APPLICATION secoda_app;
GRANT SELECT ON TABLE tmp_demo_db.demo.users TO APPLICATION secoda_app;

-- Create a row count monitor
CALL SECODA_APP.MONITORING.CREATE_MONITOR(
    MONITOR_KEY => 'demo_row_count',
    NAME => 'Demo Users Row Count',
    METRIC_TYPE => 'row_count',
    TABLE_CATALOG => 'tmp_demo_db',
    TABLE_SCHEMA => 'demo',
    TABLE_NAME => 'users'
);

-- Run the monitor
CALL SECODA_APP.MONITORING.RUN_MONITOR('demo_row_count');

-- View the result
SELECT * FROM SECODA_APP.MONITORING.LIST_MONITORS();
```

{% hint style="info" %}
Monitor results are synchronized with Secoda and processed by a scheduled job that runs every 5 minutes. There may be a short delay before new measurements appear or updated values are reflected in the Secoda UI.
{% endhint %}
