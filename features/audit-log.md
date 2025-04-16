# Audit Log

The Audit Log provides a comprehensive timeline of all activities and changes made within your Secoda workspace. This feature helps you track user actions, monitor changes, and maintain accountability across your data documentation.

### Overview

The Audit Log captures various types of activities including: resource updates, permission changes, documentation updates, role assignments, among other activities.

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

### Accessing the Audit Log

1. Navigate to Settings in your Secoda workspace
2. Select "Audit log" from the left sidebar
3. View the chronological timeline of all workspace activities
4. Filter entries by user, date, log type, and resource

### Understanding Log Entries

Each log entry contains:

* Timestamp of the action
* User who performed the action
* Type of action performed
* Affected resource

### API Access

You can programmatically access the Audit Log through our REST API. Please refer to [secoda-api.md](../secoda-api.md "mention") for detailed documentation on using the API.

#### Get Workspace Audit Log

```http
GET /api/v1/notification/workspace/
```

Query Parameters:

* `days`: Number of days of history to retrieve (default: 90)
* `page`: Page number for pagination
* `page_size`: Number of items per page

Example Response:

```json
{
  "count": 100,
  "next": "https://api.secoda.co/api/v1/notification/workspace/?page=2",
  "previous": null,
  "results": [
    {
      "id": "123e4567-e89b-12d3-a456-426614174000",
      "created_at": "2024-03-14T12:00:00Z",
      "event": "resource_created",
      "resource_id": "789e4567-e89b-12d3-a456-426614174000",
      "resource_type": "document",
      "performer": {
        "id": "456e4567-e89b-12d3-a456-426614174000",
        "name": "John Doe"
      }
    }
  ]
}
```

### Best Practices

1. **Regular Auditing**: Review the Audit Log periodically to monitor workspace changes
2. **Change Management**: Use the log to track and verify planned changes
3. **Compliance**: Maintain records of sensitive data access and modifications
4. **Troubleshooting**: Reference the log when investigating unexpected changes

### Permissions

Only workspace administrators and users with appropriate permissions can access the Audit Log. This ensures security and maintains the integrity of audit records.

### Limitations

* Logs are retained for 90 days
* Bulk actions are logged as single entries
* System-generated changes are marked with "system" as the actor

For more information about Secoda's security features, visit our [Security Documentation](https://docs.secoda.co/security).
