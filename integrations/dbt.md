---
description: This page walks through the Secoda and dbt integration that Secoda supports
---

# dbt

### **Getting Started** <a href="#h_0703b4d233" id="h_0703b4d233"></a>

There are three steps to get started using dbt with Secoda:

1. Enable your dbt Cloud REST API
2. Retrieve your dbt Cloud API key and Account ID
3. Connect dbt to Secoda

#### **Enable the dbt REST API** <a href="#h_89d08409d1" id="h_89d08409d1"></a>

Secoda uses the dbt Cloud REST API, which is only available paying dbt Cloud customers. For Secoda to retrieve metadata from dbt, you need to enable your dbt's REST API. To do this, go to **Account Settings > Metadata API** and enable the API.

![](https://downloads.intercomcdn.com/i/o/345516478/e4c72562e6b3c14d3d20629b/image.png)

#### **Retrieve your dbt Cloud API key and Account ID** <a href="#h_a2cb9baed8" id="h_a2cb9baed8"></a>

You can determine your account ID by going to the Home page of dbt Cloud. In the URL, for example in the URL below, the account ID is `12345 https://cloud.getdbt.com/#/accounts/12345/projects/28649/dashboard`

Your API key can be found in **Profile > API Access** and then click show to see your API key.

![](https://downloads.intercomcdn.com/i/o/345516125/f29da89403c954783f78de48/Screen+Shot+2021-06-03+at+10.30.16+AM.png)

#### **Connect dbt to Secoda** <a href="#h_d49e98be3a" id="h_d49e98be3a"></a>

After enabling the dbt REST API, the next step is to connect Secoda:

1. In the Secoda App, select ‘Add Integration’ on the Integrations tab
2. Search for and select ‘dbt’
3. Enter your dbt account ID and API key. This information is kept encrypted.
4. Click 'Connect'
