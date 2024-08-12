---
description: An overview of the Hex integration with Secoda
---

# Hex

{% content-ref url="hex-metadata-extracted.md" %}
[hex-metadata-extracted.md](hex-metadata-extracted.md)
{% endcontent-ref %}

## Getting started with Hex

There are two steps to connect Hex with Secoda

1. Create a Personal or Workspace access token within Hex
2. Connect Hex to Secoda

### **Create a Personal Access or Workspace Token**

1. Navigate to `Settings` > `API Keys`
2.  Create either a Personal access or Workspace token.&#x20;

    **Note:** If using a Personal access token, the token will mirror the user's permissions in the workspace and will expire by the chosen date. Only workspace admins can create a Workspace token and this token has the option to never expire. For more information on tokens see ([https://learn.hex.tech/docs/explore-data/notebook-view/hex-api/hex-api-overview#token-creation](https://learn.hex.tech/docs/explore-data/notebook-view/hex-api/hex-api-overview#token-creation))

### **Connect Hex to Secoda**

After creating an access token, the next step is to connect Hex to Secoda

1. In the Secoda App, navigate to the 'Integrations' tab
2. Click on 'Connect Integration'
3. Search for and select 'Hex'
4. Add the access token
5. Test the Connection - if successful, you'll be prompted to run your initial sync
