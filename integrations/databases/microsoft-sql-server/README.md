---
description: Microsoft SQL Server Integration with Secoda
---

# Microsoft SQL Server

{% content-ref url="metadata-extracted.md" %}
[metadata-extracted.md](metadata-extracted.md)
{% endcontent-ref %}

### Getting Started with Microsoft SQL Server

There are three high-level steps to start using Microsoft SQL Server with Secoda:

1. Create a database user
2. Whitelist the Secoda IP address
3. Integrate Microsoft SQL Server in Secoda

#### Create a Database User

The username and password you originally set up for your cluster is your admin account. Keep this account for your own use. For Secoda (or any other third-party tool), create a separate, limited-scope user.

```sql
-- Create a user named "secoda" that Secoda will use when connecting to your Microsoft SQL Server database.
CREATE USER secoda PASSWORD = '<enter-strong-password-here>';

-- Grant read-only access on each database you would like Secoda to extract from.
GRANT SELECT ON DATABASE <yourdbname> TO secoda;
```

Use these credentials (not your admin account) when configuring the integration in Secoda.

#### Connect Microsoft SQL Server to Secoda

1. In the **Integrations** tab of the Secoda app, click **Add Integration**.
2. Select **Microsoft SQL Server**.
3. Enter your connection details.
4. Choose an authentication method (explained below).
5. Click **Connect**.

{% hint style="info" %}
You can connect to an entire server and integrate its databases through a single integration. This enhancement simplifies integration, which previously required separate integrations for each database.
{% endhint %}

**Connection Methods**

| Method                      | How it Authenticates           | Typical Use Case                                                                                                                         |
| --------------------------- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Direct (SQL Authentication) | SQL Server username & password | Quick setup for any environment.                                                                                                         |
| Azure AD                    | Azure Active Directory account | Cloud or hybrid environments using centralized identity management.                                                                      |
| Windows AD (NTLMv2)         | Domain credentials via NTLMv2  | On-premise or hybrid domains. Strongly recommended to pair with reverse/forward SSH tunnels to provide a layer of end-to-end encryption. |

#### Security

If your SQL Server is inside a VPC or behind a firewall, whitelist Secoda’s outbound IP addresses so our workers can reach the host. Alternatively, use a reverse **SSH Tunnel**.

Once an SSH tunnel is configured (if you are using one), choose **SSH Tunnel** in the connection form and provide the tunnel details.\
\
See the full list here: [What are the IP addresses for Secoda?](https://your-secoda-docs-link-here/)

### Troubleshooting

| Issue                         | Possible Cause                         | Resolution                                                                                                    |
| ----------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Timeout or “host unreachable” | The server is on a private network.    | Whitelist the Secoda IPs or use a reverse SSH tunnel                                                          |
| Authentication failures       | Wrong auth type selected.              | Verify you picked the correct method (SQL Login, Azure AD, or Windows AD) and that the credentials are valid. |
| Permission errors             | The `secoda` user lacks SELECT rights. | Re-run the `GRANT SELECT` statement for each required database.                                               |
