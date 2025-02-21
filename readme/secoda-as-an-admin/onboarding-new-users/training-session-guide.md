---
description: A guide of what you might want to cover in your onboarding sessions
---

# Training session guide

### Introduction

* Introduce yourself and your roles with the project
* Introduce Secoda high-level - AI-powered data search, cataloging, lineage and documentation platform for data teams
  * Explain your main use cases for the product, what issues and pain points it will help address
  * Explain which data is currently integrated and documented
  * Encourage users to browse and search our docs.secoda.co site for documentation

### **Demo**

Share your screen showing your Secoda workspace.

#### Homepage

* Homepage is the first thing you'll see in the product. This is your own personal customizable homepage where you can:
  * Edit the cover image
  * Add widgets to pin certain resources that you come back to often
  * Add a private notepad for your personal notes
  * Filter the widgets for most popular to see what your teammates are searching for
* While you're here, you can also explain the different roles (Viewers, Editors, Admins) and what access the group should expect based on their roles

{% embed url="https://www.loom.com/share/ea6c9de6fffe4edc93378a6be7a20a43?sid=1204d0e6-62c0-41fb-a517-0a89585fe480" %}

#### Teams

* Click into Teams and explain how you've designed them; point out which Team the group you're presenting to will be added to
*   Demo how to join and leave a Team and how it appears in the left sidebar once you join

    <figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/3f55a9a4-9d15-4f37-839a-cc46b9d97729.gif" alt=""><figcaption></figcaption></figure>
* Click into a Team to explain the different sections within a Team
  * The Team Homepage functions similarly to the Main homepage, but it is configured by the Admins and is specific to that Team - pin resources that the whole Team will benefit from having easy access to
  * The Catalog hosts all of your data sources - show the different integrations
  * Metrics is where you can define key metrics your team uses, and visualize them by writing the SQL query used to calculate them
  * The Dictionary is a space for glossary terms and metrics - show what you've built out so far and how you plan to use that feature
  * Talk about your current use cases for Documents - what type of documentation have you built out
  * Questions is where FAQs live, and also can be used for data requests - explain if/how you plan to incorporate these into workflows
  * Collections are essentially folders that allow you to group a subset of each of these resources - you might consider having separate Collections for different projects within a team
  * Note that Admins can remove any of these sections to simplify the user's experience if they don't need access to certain features

#### Search

* Choose a resource that is particularly enriched (maybe one that is important/relevant to the group that you're presenting to) and Search for it
  * Click into the resource and show off all of the metadata that you've added like descriptions, owners, tags, verification etc.
  * Explain how you are defining ownership and verification at the moment, if applicable
  * Navigate to the Lineage tab to show that feature, if applicable
*   Click into Search and show off all of the search filters that will help users narrow down their search, more details here [#search](training-session-guide.md#search "mention")

    <figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/f89bc6c1-9ddf-4518-ab4d-f652e45d65f7.gif" alt=""><figcaption></figcaption></figure>

#### AI Assistant

* If users don't know exactly what they want to search for, show them that they can use the AI Assistant to search in plain language
* Show a few examples of asking the AI some questions about your data: examples [prompts.md](../../../features/ai-assistant/prompts.md "mention")
  * If your team is interested in documenting PII, you could ask it to find you all of the tables with potential PII data

{% embed url="https://www.loom.com/share/6a802f20155d4a83bc2fa758f613d33a?sid=17bd2f81-83c4-49d5-b9e6-262d7f1a65d1" %}

#### Slack Integration

* Open up Slack to demo how to use the Slack integration to ask the AI questions about your data directly in Slack [slack-user-guide.md](../../../extensions/slack-connection/slack-user-guide.md "mention")

{% embed url="https://www.loom.com/share/ebc7267824734f0c92ed1c74d0a42ac3?sid=0fa8cb84-fd7c-4b1e-b93b-e8311c2f84f5" %}

#### Additional Features Demo

You may want to highlight additional features depending on who you are providing training for. Consider the persona that you are working with, and which features might be useful for improving their current workflows.&#x20;

For example, a data analyst might benefit from seeing how the [queries](../../../features/queries/ "mention") feature works in Documents. A data owner would benefit from hearing about the different ways to [#automate-documentation](../../../best-practices/best-practices-for-setting-up-your-workspace.md#automate-documentation "mention"), like using Automations & the Propagate metadata feature. A data owner might also want to know about [monitoring.md](../../../features/monitoring.md "mention") and how they can set up data quality alerting for their core tables.

### Next steps

* Invite the users to Secoda and add them to their respective Teams
* Ask users to review the resources that they/their team owns - update descriptions and other metadata if necessary
* Ask users to test out the AI Assistant and provide feedback
* Share any relevant documentation with users, including[secoda-as-a-viewer](../../../getting-started/secoda-as-a-viewer/ "mention") [secoda-as-an-editor.md](../../../getting-started/secoda-as-an-editor.md "mention")
