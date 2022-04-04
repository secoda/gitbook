# Airflow

### **Getting Started** <a href="#h_d780d3703b" id="h_d780d3703b"></a>

There are three steps to get started using Airflow with Secoda:

1. Enable the Airflow REST API
2. Connect Airflow to Secoda
3. Whitelist Secoda IP Address

#### **Enable the Airflow REST API** <a href="#h_5679925c3a" id="h_5679925c3a"></a>

Secoda uses the Airflow stable REST API, which is only available on Airflow v2.0+. For Secoda to retrieve metadata from Airflow, you need to enable your Airflow's REST API. To do this, edit your `airflow.cfg` file and change the line below to `airflow.api.auth.backend.basic_auth`\


```
[api] auth_backend = airflow.api.auth.backend.deny_all
```

After changing this is what the line should look like:

```
[api] auth_backend = airflow.api.auth.backend.basic_auth
```

#### **Connect Airflow to Secoda** <a href="#h_2cd5acf282" id="h_2cd5acf282"></a>

After enabling the Airflow REST API, the next step is to connect Secoda:

1. In the Secoda App, select ‘Add Integration’ on the Integrations tab
2. Search for and select ‘Airflow’
3. Enter your Airflow user and password. This information is kept encrypted.
4. Click 'Connect'

### **Security** <a href="#h_4e3c0bcf41" id="h_4e3c0bcf41"></a>

VPCs keep servers inaccessible to traffic from the internet. With VPC, you’re able to designate specific web servers access to your servers. In this case, you will be whitelisting the Secoda IPs to read from your Airflow instance.

Allow Secoda to access your Airflow API from the IP address `35.175.75.15/32`
