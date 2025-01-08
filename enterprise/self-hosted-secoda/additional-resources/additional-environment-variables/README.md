# Additional Environment Variables

### Getting started

The following variables can be added to the `api` and `worker` (if worker exists) containers to unlock additional functionality. They are all optional.

```
  api:
    ...
    environment:
      - OPENAI_API_KEY=sk-abc12345EXAMPLExyz67890
      ...
    healthcheck:
      ...
```

### Modules

**AI Assistant&#x20;**_**(recommended)**_

```
OPENAI_API_KEY=

# Example
OPENAI_API_KEY=sk-abc12345EXAMPLExyz67890
```

{% content-ref url="openai-api-key-creation-on-premise.md" %}
[openai-api-key-creation-on-premise.md](openai-api-key-creation-on-premise.md)
{% endcontent-ref %}

**Bucket Uploads**

If this is not configured, Secoda defaults to storing file uploads in Postgres.

```
PRIVATE_BUCKET=
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=

# Example
PRIVATE_BUCKET=organization-manifest-bucket
# These are not necessary if the container can assume an AWS role
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```

{% content-ref url="aws-bucket-with-access-keys-on-premise.md" %}
[aws-bucket-with-access-keys-on-premise.md](aws-bucket-with-access-keys-on-premise.md)
{% endcontent-ref %}

### Integrations

**BigQuery (OAuth) Integration**

```
BIGQUERY_SECRETS=

# Example
BIGQUERY_SECRETS='{"web":{"client_id":"1234567890-abcdefghijklmnopqrstuvwxyz.apps.googleusercontent.com","project_id":"your-project-id","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":"your-client-secret","redirect_uris":["https://your-redirect-uri.com/callback","http://localhost:8080/callback"],"javascript_origins":["https://your-domain.com","http://localhost:8080"]}}'
```

{% content-ref url="google-oauth-application-on-premise.md" %}
[google-oauth-application-on-premise.md](google-oauth-application-on-premise.md)
{% endcontent-ref %}

**Looker Studio (OAuth) Integration**

```
GOOGLE_DATA_STUDIO_CLIENT_ID=
GOOGLE_DATA_STUDIO_CLIENT_SECRET=

# Example
GOOGLE_DATA_STUDIO_CLIENT_ID=1234567890-abcdefghijklmnopqrstuvwxyz.apps.googleusercontent.com
GOOGLE_DATA_STUDIO_CLIENT_SECRET=GOCSPX-abcdefghijABCDEFGHIJ12345678
```

{% content-ref url="google-oauth-application-on-premise.md" %}
[google-oauth-application-on-premise.md](google-oauth-application-on-premise.md)
{% endcontent-ref %}

**PowerBI (OAuth) Integration**

```
POWERBI_CLIENT_ID=
POWERBI_CLIENT_SECRET=

# Example
POWERBI_CLIENT_ID=12345678-abcd-1234-efgh-56789abcdef0
POWERBI_CLIENT_SECRET=abcDEF123456!@#XYZ789
```

{% content-ref url="powerbi-oauth-application-on-premise.md" %}
[powerbi-oauth-application-on-premise.md](powerbi-oauth-application-on-premise.md)
{% endcontent-ref %}

**Github Integration**

```
GITHUB_APP_ID=
GITHUB_SIGNING_SECRET=
GITHUB_APP_PRIVATE_KEY=

# Example
GITHUB_APP_ID=123456
GITHUB_SIGNING_SECRET=abc123XYZ456!@#example
# RSA, base-64 encoded private key
GITHUB_APP_PRIVATE_KEY=LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQoMQUlFQW9NKlRoU
```

{% content-ref url="github-application-on-premise.md" %}
[github-application-on-premise.md](github-application-on-premise.md)
{% endcontent-ref %}
