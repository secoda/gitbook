---
description: List of all the metadata that Secoda pulls from Omni
---

# Omni Metadata Extracted

The Omni integration extracts the following metadata:

#### Folders

* Name
* Description
* Path
* Owner information
* Created and updated timestamps

#### Dashboards/Documents

* Name
* Description
* URL to view in Omni
* Owners
* Labels as tags
* Parent folder
* Created and updated timestamps
* External usage (view count)&#x20;

#### Models&#x20;

* Name
* Description&#x20;
* Owner
* Labels&#x20;
* Created and updated timestamps&#x20;

#### Views&#x20;

* Name&#x20;
* Description&#x20;
* Parent model&#x20;
* Dimensions
  * Name&#x20;
  * Description
* Measures&#x20;
  * Name
  * Description

#### Lineage

The integration automatically creates lineage connections between:

* External table ->  View -> Chart -> Dashboard
* External column -> Dimension/Measure -> Chart&#x20;

### Dashboard Previews

Secoda supports embedded previews of Omni dashboards directly within the platform. When viewing an Omni dashboard in Secoda, you can see a live preview without leaving Secoda.
