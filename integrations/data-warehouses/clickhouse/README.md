# ClickHouse

ClickHouse is an open-source column-oriented database management system that allows generating analytical data reports in real-time. The ClickHouse integration in Secoda allows you to connect your ClickHouse instance to catalog and document your data.

### Getting Started with ClickHouse <a href="#getting-started-with-redshift" id="getting-started-with-redshift"></a>

Create a user with the following permissions

* `SELECT` access on system tables (`system.tables`, `system.columns`)
* `SELECT` access on the databases and tables you want to catalog
* Access to query history information
* If using metadata push capabilities, the user needs `ALTER` permissions on tables

Gather the additional information:

* Host name of your ClickHouse instance, e.g., `wo3evzjkve.us-east-1.aws.clickhouse.cloud`
* Port number, e.g., 8443
* Username with access to ClickHouse
* Password for authentication

### Setup

1. In Secoda, navigate to the Integrations page
2. Click "Add Integration"
3. Select "ClickHouse" from the list of available integrations
4. Fill in the following credentials:

```yaml
Host: your-clickhouse-host
Port: 8443
User: your-username
Password: your-password
```

5. Click "Test Connection"
6. Select databases and schemas&#x20;
7. Click "Continue" to trigger the initial sync

See [clickhouse-metadata-extracted.md](clickhouse-metadata-extracted.md "mention")for the full list of information sycned from ClickHouse.

### Monitoring Capabilities

The ClickHouse integration supports various monitoring features:

* Table row counts
* Table freshness
* Column-level statistics, e.g., null % and unique %.

### Troubleshooting

Common issues and solutions:

1. **Connection Failed**
   * Verify the host and port are correct
   * Ensure the user has proper permissions
   * Check if the ClickHouse server is accessible from your network
2. **Missing Tables**
   * Verify the user has SELECT permissions on the schemas
   * Check if tables are in system or information\_schema databases (these are excluded)
3. **Query History Not Showing**
   * Ensure the user has access to system tables
   * Verify query history retention settings in ClickHouse

### Limitations

* External tables may have limited metadata support
* Some system tables are excluded from extraction
* Query history retention depends on ClickHouse settings
* Metadata push is not supported for external tables

### FAQ

**Q: Can I connect to multiple ClickHouse instances?** A: Yes, you can create multiple ClickHouse integrations in Secoda, each pointing to a different instance.

**Q: Does the integration support SSL connections?** A: Yes, ClickHouse connections are secured using standard SSL/TLS protocols.

**Q: How often does the integration sync?** A: By default, the integration syncs once per week, but this can be configured in the integration settings.

**Q: Can I preview data in Secoda?** A: Yes, the integration supports data preview capabilities for tables and query results.
