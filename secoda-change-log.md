---
description: The highlights of the releases for Secoda’s product can be found here.
---

# Secoda Change log

**The highlights of the releases for Secoda’s product can be found here.**

### June 8, 2023 (Release 7.2.2)

* Added Slack proactive response in data request channel
* Added AI search command in Slack with `secoda-ai`
* Added Slack to onboarding checklist
* Added AI assistant for viewers
* Added automatically turn on Databricks cluster on extraction
* Added custom integration not in catalog tree
* Fixed incorrect icons on home page
* Replace private notepad widget with text block & white background on home page
* Fixed asked by and assigned to fields empty on question
* Added preference to disable staling logic on all integrations
* Fixed Snowflake extraction accessing deleted DB
* Fixed original home page background not migrated
* Added delete option in resource menu
* Removed scheduled extractions from custom integrations
* Fixed columns disappear when sorting on "Type"
* Fixed subscribers being notified of table schema changes
* Fixed Teams selector not saving in questions
* Fixed columns showing up in main lineage graph
* Fixed not being able to click on resource in inbox
* Fixed Inbox content width is inconsistent
* Fixed negative inbox count
* Fixed mention notification not sending
* Fixed being unable to click related resource in questions
* Fixed Slack notification showing wrong approver for change request
* Fixed relative links in AI assistant
* Fixed custom property not showing all content
* Fixed Retool integration cookie parsing when cookie contains space
* Fixed related resource not clickable
* Fixed failing test in lineage causes blank screen
* Fixed collections drop down list showing deleted collections

### June 1, 2023 (Release 7.2.0)

**Features & Improvement**

* New inbox
* New home page
* Schema change notifications
* Change parents of collections with "move to"
* Auto-suggest similar questions
* Hide support for viewers

**Fixes**

* Query blocks export
* Collections flash on load
* Scroll on query blocks
* Set default team if empty teams
* Auto-relate questions to resource
* Reduce SVG sizes
* MSSQL extraction failures fixed
* Lowercase all emails (including service accounts)
* Cleanup unused postgres indexes
* Support for Russian and German characters in signup flow
* Team not set in invitation links
* Column stats for viewers
* CSV export/import fixes

### May 23, 2023 (Release 7.1.5)

* Added "Move To" functionality for collections, documents, and dictionary terms
* Fixed new teams not showing up right away in permissions after update
* Added pagination for columns in the catalog
* Fixed Snowflake failing on schema attribute
* Fixed collections page crashing due to undefined reference in metadata sidebar
* Fixed CSV import not uploading in catalog due to None in cel
* Fixed search not persisting results when navigating back
* Improved BigQuery column lineage coverage
* Fixed BigQuery query errors
* Set default team for resource when team is not specified
* Fixed BigQuery failure due to no objects to concatenate
* Fixed invite teammate in settings crashing page
* Added ability to filter by multiple column types
* Improve MS SQL lineage coverage
* Improved Google Drive embed regex matching
* Fixed Tableau integration failing due to projects bad reference
* Fixed Great Expectations failing if latest run not found
* Fixed question templates not working
* Fixed Lineage tooltip being blank
* Organize list of owners alphabetically

### May 18, 2023 (Release 7.1.4)

* Added Databricks lineage
* Added 32k context for Open AI GPT 4 API calls
* Added Custom integration option
* Condensed resource metadata properties
* Added "Move To" functionality on documents, dictionary terms, and collections
* Improved performance of catalog table and catalog tabs
* Fixed extraction jobs running multiple times in a row
* Fixed deleted documents not being removed from search
* Fixed great\_expectations integration page crash
* Fixed settings page crash
* Fixed search crashing when trying to add a schema filter
* Fixed Looker views importing columns from the wrong schema
* Fixed Salesforce integration pulling deleted reports
* Fixed Tableau hierarchy not showing up properly
* Fixed MS SQL Preview failing
* Fixed default form not working on questions
* Updated design of nested page in documentation editor
* Rename discussions to questions on table page
* Fixed email notifications missing name

### May 16, 2023 (Release 7.1.3)

* Added Teams feature
* Added Stitch Integration
* Improved speed of BigQuery integration by 4x
* Fixed slow scroll behaviour on catalog and column list
* Fixed filters for types in columns list not working
* Fixed related resource in questions not being clickable
* Fixed Tableau groups not paginating
* Fixed source not being automatically selected on query block
* Fixed Git integration password not being masked in UI
* Added mandatory title on resource creation modal
* Fixed typo on BigQuery Integrations permissions section
* Fixed docs link on Great Expectations integration page
* Fixed icon selector modal not closing on collection
* Fixed dbt casing in AI page
* Fixed UI not showing if SSH Tunnel is being used
* Fixed customization menu unable to close menu by clicking outside
* Fixed clicking on profile reloading the whole page

### May 9, 2023 (Release 7.1.2)

* Fixed integration extractions being queued for long periods
* Fixed service account users not receiving announcements
* Fixed tags not being available on search
* Fixed Redshift integration unable to load schemas
* Fixed having archived and stale resources in search
* Fixed Tableau extraction failure
* Added incremental difference logic for integration extractions
* Fixed column lineage not working for Snowflake views
* Fixed Slack search not working
* Added Glue integration query popularity
* Added resource link on announcement
* Added PowerBI internal Lineage
* Removed schedule from Google Data Studio
* Added column descriptions in search

### April 30, 2023 (Release 7.1.1)

* Fixed lineage graph not rendering consistently after expansion
* Added BigQuery record fields support
* Fixed sort not working on columns tab in Catalog
* Fixed columns tab on Catalog not loading
* Fixed Search results missing
* Added metadata propagation on table columns
* Modify Postgres query to increase lineage coverage
* Fixed duplicate Slack notifications sent
* Fixed Fivetran extraction failure
* Fixed 500 error when connected Slack for on-premise

### April 26, 2023 (Release 7.1.0)

* Secoda AI
* Added Collection templates
* Fixed for query block footer render issues
* Fixed integration source name cut off
* Added new feature modal
* Fixed Fivetran integration failing
* Fixed column search results not showing database, schema, and table
* Fixed Sigma integration failing
* Fixed Dictionary Term Chart in Home Page not showing relevant info
* Fixed "Access Denied" error when looking at nested documents while editing a template

### April 20, 2023 (Release 7.0.3)

* Added BigQuery stored procedure lineage parsing
* Added optional Glue workgroup and encryption parameters
* Added resource link on announcement
* Fixed small percentage of docs not saving
* Fixed [API reference](http://docs.api.secoda.co/) not loading
* Fixed "Add content" button on Home page
* Fixed not being able to create a second workspace
* Fixed popularity sort issue during extractions
* Fixed page popular resources widget on Home page
* Fixed Redshift integration failure
* Fixed PowerBI OAuth refresh creating new integration

### April 17, 2023 (Release 7.0.2)

* Added resource subscriptions
* Added created at property on resource side bar
* Fixed search queries not matching
* Fixed column profiler returning errors for MS SQL
* Fixed Mode integration failing with "invalid attribute columns\_dataframe" error
* Fixed filter menu switch does not toggling
* Fixed column Profiler crashing
* Fixed BigQuery cross project lineage not populating
* Fixed user being able to add collection to itself

### April 11, 2023 (Release 7.0.1)

* New login page design
* New profile and workspace design
* Fixed search timing out
* Fixed table component filters crashing app
* Improved cross database column level lineage inaccuracy
* Fixed sort menu item missing for dropdown
* Fixed @ search not matching
* Added button to refresh OAuth for Power BI

### April 4, 2023 (Release 7.0.0)

* Added semantic search algorithm using AI
* Lineage UI/UX bugs and improvements
* Fixed Google Data Studio reports not loading in search
* Fixed lineage not showing for custom sql query in Tableau
* Fixed column profile distributions not showing
* Fixed no pagination missing on table level columns
* Added preference to filter personal folders in Looker
* Fixed manual Lineage freezing
* Added metadata propagation on table columns
* Added inbox pagination and unread indicator
* Added Power BI support for measures
* Fixed not always showing lineage tab
* Fixed column profiler not working on timestamp columns in Redshift

### March 30, 2023 (Release 6.3.1)

* Added Weekly and Monthly active users analytics widget
* Fixed analytics page goes blank on on-premise instances
* Fixed search page not loading on filter loading failure
* Fixed collections hierarchy not displaying in side bar
* Fixed BigQuery lineage being backwards
* Fixed search bar un-focusing
* Fixed chart not displaying time scale properly
* Added optional parent element in form
* FixedCustom text property not saving edited value
* Added form select user input for options
* Fixed user first and last name not set after invitation
* Fixed git integration sync failing
* Fixed analytics page settings is not up-to-date when leave and go back
* Fixed blank screen after opening resource side sheet via lineage
* Fixed line chart minimum based on dataset
* Fixed users without names on the Analytics page shown as blank fields
* Fixed number of searches and resource views being inaccurate
* Added filters on related resource selector
* Added groups in user selector for form
* Added auto-populating resource owner with form user
* Added default support for form templates
* Added invite option on user select menu

### March 28, 2023 (Release 6.3.0)

* Released new iteration of the Analytics page

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/88956064-ba86-4dac-a937-70da03c62d45/Untitled.png)

* Fixed incorrect Snowflake view lineage
* Fixed collapsable rows for the collections list
* Fixed Metadata integration exception

### March 23rd, 2023 (Release 6.2.6)

*   Added form templates

    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c12f3011-85f8-471d-ad30-767fbf048886/Untitled.png)
* Added collapsable rows on table component
* Updated AI Assistant to use GPT 4
* Fix for metadata propagation performance issues
* Fix for search results not showing
* Fix for Snowflake views query error
* Fix for slow search performance
* Fix for metadata propagation modal not loading
* Improved owner list in creation modal
* Fixed asking questions from Slack
* Fixed question notification sent on signup
* Fixed Inbox going blank
* Fixed notification sent on all archived resources
* Fixed Power BI datasets not imported
* Fixed collection documentation being overwritten
* Fixed Databricks dbt mapping
* Fixed Tableau project visibility toggle not working
* Fixed lineage node overflow
* Added button to re-calculate column level lineage on lineage graph
* Fixed dbt lineage not created on dbt core
* Switch CTA to "Done" after resource update on metadata propagation
* Fixed Looker integration bad variable access error
* Fixed opening AI assistant causing blank screen

### March 17th, 2023 (Release 6.2.5)

* Added manual lineage builder
* Added propagating metadata
* Added User, Tag, Resource and Checkbox type to custom properties
* Added support for properties in templates
* Fix for source filter unscrollable
* Fix for alignment issues in catalog table
* Fix for lineage Inference for select \*
* Fix for Slack app on isolated instance
* Fix for Fivetran and Hightouch runs not showing
* Fix for integration filter uses type instead of name
* Fix for dbt cloud integrations
* Fix for bi-directional relation not showing
* Fix for column filter not showing any results
* Fix for table and column filters not showing
* Fix for slack channel filter not lazy loaded

### March 10th, 2023 (Release 6.2.3)

* Search page UI update with better filtering, sorting, and customization
* Fixed search page throwing server error
* Fixed making workspace selector visible at all times
* Fixed removing Postgres schema in settings does not remove it from the workspace
* Performance optimizations for metadata extraction

### March 7th, 2023 (Release 6.2.2)

* Added Dictionary Term nesting
* Fix import not working
* Fix catalog side bar list not filtering by permissions
* Fix Slack question body not included in notification
* Fix column exporter performance issues
* Fix tests are not being displayed on Glue views
* Added document custom property inheritance
* Added document share setting inheritance

### February 27th, 2023 (Release 6.2.0)

* Added Retool integration
* Updated design for accessibility
* Fixed dbt creation query missing
* Improved profiler to analyze all rows in table
* Fixed dragging down collections on catalog not persisting
* Added column profiler null improvements
* Added column profiler strings support
* Fixed schemas not loading on integrations page
* Added support for all data types in column profiler
* Fixed Oracle lineage not working
* Added Slack notification mentions for sender of notification
* Fixed announcement Slack notification format

### February 23rd, 2023 (Release 6.1.9)

* Fix for link icon redirect
* Resource discussions refresh on creation
* Fixed Glue -> Great Expectations mapping not working
* Added notification preferences for resource requests
* Added deleted resource notification preference
* Fixed BigQuery view definition lineage
* Fixed dangling extraction jobs
* Fixed great expectations mapping tab now showing
* Fixed Tableau failing
* Fixed Great Expectations with AWS role arn not working
* Allow multiple discussions on a resource
* Fixed filter by blank description on columns broken
* Fixed mention notifications sent to connected Slack channel
* Fixed scrolling on onboarding drawer

### February 16th, 2023 (Release 6.1.6)

* Add Resource button on related tab
* Glue view lineage
* Column level lineage accuracy with Open AI
* Google data studios connection error
* Confluence document import with embeds not updating
* Fix the recursive sql generation prompt
* Bulk export invalid type
* Workspaces on free trial are set to free instead of enterprise
* Support query salesforce data using query blocks
* Publishing not working when Send Announcement is selected
* Salesforce integration preview support
* Display properly cased of resource
* AI assist endpoints with background job for long running queries
* Additional parameters in search algorithm
* Column lineage edge behaviour
* Cannot add many-to-many fields via the API
* Tableau Schema Selector extend functionality to data sources

### February 9th, 2023 (Release 6.1.4)

* Nested documents
* Fix for Loom (and all) embeds
* Integration performance improvements
* great expectations test linking improvements
* dbt jobs sync for URLs and test runs
* Fix for being able to update scheduled extractions
* BigQuery -> Tableau lineage not working
* Published workflow does not show user name
* [Salesforce integration](https://docs.secoda.co/integrations/salesforce-integration)
* Filter option for tags not working
* Metabase integration broken
* Export format does not match import format
* Looker column lineage
* Integration not extracting all selected schemas
* dbt creation query not importing
* Return definition for tables on API
* PII table shows null for column names
* User first name and last name missing
* Export screen crashing
* Incorrect custom property deleted
* Search icon render issue
* Announcement modal counting Frequent Users incorrectly
* Preference to disable Personal collections from Metabase extracts
* Displaying Tags Column on AgGrid for Dictionary and Documents
* Cross account role for Great Expectations
* Export resource page
* Search for tag icons
* Unable to navigate list of users on Assign to Question
* Extraction history not loading

### January 30, 2023 (Release 6.1.0)

#### Bug Fixes and Improvement

* Added tags column on Collections page
* Added announcement body in Slack notification
* Fixed Slack question submission form
* Fixed Snowflake not showing popularity
* Fixed Table tabs order to always have columns first
* Fixed resource drawer breaking when clicking on draft resource in the lineage graph
* Added dictionary term query block preference
* Fixed published content showing \[object Object]
* Fixed announcement recipient options not showing
* Fixed lineage tab not loading
* Fixed change request notifications not sending to all users
* Fixed Glue External ID parameter updating on integration change
* Fixed viewers not being able to create questions
* Fixed removing Slack hooks creating published event
* Fixed table page crashing
* Fixed resource announcements only sending to resource owner
* Fixed sorting catalog items by title
* Fixed upstream lineage for BigQuery tables not showing
* Fixed dbt job schedule displaying incorrectly
* Fixed blank dbt test names
* Fixed preview tab having horizontal scrollbar
* Fixed BigQuery table queries incorrect
* Fixed Safari login redirect loop
* Added multiple workspace support
* Fixed home page card changes not persisting
* Fixed PII column not masked in preview
* Fixed removing table of contents from Confluence import
* Added BigQuery view lineage
* Fixed Confluence import dead links
* Fixed PII suggestions table not shown
* Fixed updating collections changing the reply count of questions
* Fixed Tableau failing due to NoneType reference
* Fixed viewers being able to edit related and custom properties
* Fixed sidebar showing data tree when collapsed
* Fixed published collections not being visible to viewers
* Fixed Great Expectations tests not linking with table
* Added scrolling to “@” search
* Fixed table filter by blank description on columns
* Fixed collections hierarchy not sorted by alphabetical order
* Fixed emoji keyboard blocked by sidebar
* Fixed frequent users being inconsistent
* Fixed Slack search permissions to reflect user that’s searching
* Fixed API csv upload endpoint timing out
* Added tab support for the resource page
* Fixed multiple table creation queries shown on tables
* Fixed Airflow DAGs not imported correctly
* Fixed queries in query blocks not running on schedule
* Fixed question notification question asker name being incorrect
* Fixed being unable to remove parent collection from a child collection page
* Fixed catalog column schema filters not working
* Fixed Mode external URL does not work
* Fixed scrolling in creation modal collection list
* Added tooltip on home page integration icons
* Fixed priority filter option not working on questions page
* Fixed axis labels on dictionary chart not displaying
* Fixed inbox notifications not being filtered for viewers
* Fixed graphs not refreshing after query run
* Fixed not being able to edit above a query block
* Fixed Tableau chart preview not showing
* Fixed terminated extraction stage spinner
* Fixed Incorrect extraction time after termination
* Fixed Inherited workspace permissions not showing in share modal
* Fixed invitation link not redirecting to registration page
* Fixed markdown styles not rendering in inbox
* Fixed markdown styles not rendering in resource drawer
* Fixed error not showing when search request fails
* Fixed new tab opening when clicking on a link in Secoda
* Fixed settings tab highlighting for editors
* Fixed clicking on search result not opening page
* Fixed being unable to select group when creating invitation link

### January 3, 2023 (Release 5.6.2)

#### Features and Improvements

*   Support for real time, multiplayer editing

    ![Group 915 (3).png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0885dfde-b31e-4961-bcec-40b0ad81cb87/Group\_915\_\(3\).png)

### December 19, 2022 (Release 5.6.1)

#### Features and Improvements

* Related resource tab
* Added support for importing dbt tags
* Released Desktop app
* Modified resource notifications to only send to owners

#### Bug Fixes

* Fixed Glue integration permissions
* Fixed Slack search issue
* Fixed Airflow lineage bug
* Fixed collapsed lineage bugs
* Fixed Slack channels not refresh

### December 19, 2022 (Release 5.6.1)

#### Features and Improvements

* Related resource tab
* Added support for importing dbt tags
* Released Desktop app
* Modified resource notifications to only send to owners

#### Bug Fixes

* Fixed Glue integration permissions
* Fixed Slack search issue
* Fixed Airflow lineage bug
* Fixed collapsed lineage bugs
* Fixed Slack channels not refresh

### December 13, 2022 (Release 5.6)

#### Features and Improvements

* Improved lineage graph by collapsing least popular resources into a single node
* Added support for importing Confluence, Microsoft Word, and Google docs
* Added Mode and Looker dashboard previews
* Added SSL certificate support on database integrations
* Relational database lineage improvements
* Added Slack bot notification DMs
* Copy paste from Notion to Secoda docs
* Added support for AWS Glue (Athena) as a query block source
* Added dbt logo icon to decorated tables
* Added support for Databricks schema selection
* Improved Slack notification message structure
* Added preview and query permission settings for integrations

#### Bug Fixes

* Fixed integration form crashing
* Fixed table and dashboard page crashing because of documentation markdown
* Fixed Slack notifications being sent
* Fixed integration description preference for columns
* Fixed dbt job schedules not displaying correctly
* Fixed integration failure notification not sending
* Fixed duplicate queries being shown on Dashboards
* Fixed certain notifications not being sent via email
* Fixed user profile page crashing
* Fixed custom invite link not assigning users to groups
* Fixed dbt descriptions not being imported
* Fixed search filters showing non-visible schemas
* Fixed guest user search permissions being incorrect
* Fixed using label instead of name for dbt metrics
* Fixed activity log not updating when navigating between resources
* Fixed mentions not sending notifications
* Fixed change requests not showing for viewers
* Fixed not being able to resize the sidebar when the catalog is expanded
* Fixed integrations not showing on the home page
* Fixed `dbt_cloud_pr` schemas showing
* Fixed back button on dictionary terms
* Fixed Tableau dashboard owners not being imported
* Fixed query blocks not working on the creation modal
* Fixed inability to discard staged changes

### November 28, 2022 (Release 5.5)

#### Features & Improvements

* BigQuery view lineage based on the view SQL definition
* BigQuery cross project lineage
* Support for mapping great\_expectations to connected data source
* Full column name including schema and table on “@” search
* Support for Databricks SQL warehouse
* Description import preferences on all integrations
* Tableau workbooks now show related queries from upstream sheets
* Popularity now shows on the resource page
* Governance information, i.e, PII now shows on resource page
* dbt creation query now shows on resource page
* Integrations now embed documentation directly in the form
* Improved integration error message UX
* Improved query block UX on the documentation editor
* Mode dashboard queries are now extracted
* Updated PII tag behaviour to redact table and column data on previews and profiling
* Added resource deletion notification
* Add text search and order alphabetically to schema selection

#### Bug Fixes

* Fixed image upload functionality
* Fixed embed resizing on documentation editor
* Data tree links now apply filters correctly on catalog page
* Fixed source filters on catalog page
* Related charts and tables show correctly for dashboards
* Fixed BigQuery table query count
* Fixed Tableau workbook view count
* Fixed Google Data Studio dashboard links
* Fixed new question button not opening modal
* Fixed integration filters on search page
* Fixed LookML extraction failing when url is https instead of git
* Fixed filter icons being inconsistent, i.e, schema icon
* Fixed MS SQL table previews
* Fixed question properties not rendering correctly on questions page
* Fixed question reply count always showing 0
* Fixed creation model adding description to documentation for dictionary terms
* Fixed external last updated column not being able to be turned off
* Fixed deletion state being shared between different pages on table components
* Fixed adding a tag overwriting existing tags on dictionary page
* Fixed circular lineage on some resources

### November 2, 2022 (Release 5.4)

#### Features & Improvements

* Increased search speed by 5x
* Improved search algorithm accuracy
* Prompt with similar questions when user asks a question
* Snowflake view → view lineage
* Improved Postgres view lineage
* AWS Glue column profiling
* Discussions are supported on dictionary terms
* Markdown support in custom properties
* Creation modal UI for questions, collections, terms and docs
* Groups are now supported on the catalog owner column
* Support for GCS on dbt core integration
* Support for GCS on self-hosted private cloud storage
* Support for Slack integration on self-hosted instances
* Blank filters on the catalog page are now support
* New UI for the user profile page for easier navigation
* New UI for collections page for easier navigation
* Downstream connected Slack channels option on resource announcement

#### Bug Fixes

* Tableau view count corrected
* Tableau dashboard previews now show
* Query blocks support `LIKE %text%`
* Sidebar data catalog tree now expands without showing blanks
* Catalog filters show all options for collections, owners, and tags
* Question priority is included aggregate list
* Event properties now show properly on event page
* Snowflake previews load only on preview tab click
* Search filter “x” button now works
* Looker dashboard names are updated on latest extraction
* Creator of terms and docs are automatically added as owner
* Export functionality fixed for number of columns being exported
* Tableau custom SQL queries not duplicated
* Notification text formatting improvements
* Announcement home page widget displays correctly
* Description tooltips show the full multiline description
* Invited users do not show blank names
* Weekly digest now sends

### August 23, 2022 (Release 5.3)

#### Features & Improvements

*   Popularity in search

    Search is now sorted by popularity across assets with queries / usage. This was removed briefly from the product because of the impact on search speed but now it’s back and much more efficient.
*   Data Inbox

    The data inbox is a new tab that gives users a central place to see all the changes that are relevant to them in the workspace. Support teams have a shared view of all tasks / conversations with customers through tools like Intercom and now, data teams can collaborate on their data assets and conversions in the same way!
*   Viewers can submit changes on any resource

    When viewers see something that seems a little off or that they would like to change, they can submit a change for review by the admins or editors. Admins get this change in their inbox and can approve or deny the change.
*   Lineage API

    Push lineage to Secoda and add your own custom information about relationships between assets.
*   Push data to Secoda

    We’ve introduced a new way to integrate data with Secoda, which allows data sensitive customers to push data to Secoda cloud hosted solution with an agent
*   Announcements

    As an admin or editor, you can now send announcements to your workspace when new in Secoda occurs. This can be done just to viewers, editors or to your entire workspace.
*   DBT tags import

    You can now import tags, jobs and metadata associated to tags and metadata when connecting dbt to Secoda.
*   Charting in dictionary terms

    We’ve added the ability to add live charts to your metric definitions in you data dictionary. This can give viewers a little bit more context over a term when they are first jumping into Secoda.
*   Looker improvements

    We’ve significantly improved the Looker integration, which now added LookML Explore fields populated in Secoda

### August 3, 2022

#### Features & Improvements

*   Scheduling queries in Secoda

    **You can now schedule queries in Secoda!** By going to the “schedule” tab on the query block, you can choose to run a query on a certain time period within Secoda. This way, you can make sure that viewers have accurate information when browsing Secoda

    ![62eaa4b006ceec835d2a84a8\_Screen Shot 2022-08-03 at 9.15.47 AM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/65f584fd-a3b2-4368-a6f8-ff9bab96b8ab/62eaa4b006ceec835d2a84a8\_Screen\_Shot\_2022-08-03\_at\_9.15.47\_AM.png)
*   Databricks Integration

    We're excited to announce our new integration with Databricks. You can now connect one of the best data warehouses and data lakes in Secoda to handle all your data, analytics metadata management.

    ![62eaa5097e8c6db8529ed0f5\_Group 821 (3).png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c1df8e31-ec89-4daf-a0cf-73a2189252c1/62eaa5097e8c6db8529ed0f5\_Group\_821\_\(3\).png)
*   Lineage Improvements

    We're also excited to introduce a new lineage UI / UX which allows you to explore lineage easier, see column level lineage in the same view as table lineage, and see your lineage in fullscreen!

    ![62eaa6e857283e4263774ed4\_Screen Recording 2022-08-03 at 12.47.08 PM.gif](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/354498ec-aae6-45f8-8b58-70d109f08d1e/62eaa6e857283e4263774ed4\_Screen\_Recording\_2022-08-03\_at\_12.47.08\_PM.gif)
*   Catalog Improvements

    In addition to these big changes, we've also added some additional functionality to bring in the dbt tests into your the catalog from the dbt integration, some of the other changes are highlighted below:

    * Markdown preview in the catalog
    * Additional performance improvements to catalog & app
    * Additional bugs resolved and performance improvements

### July 26, 2022

#### Today, we’re excited to announce one of the bigger changes to Secoda we've created over the last year.

The problem with existing data catalogs and discovery tools is that they don't focus on publishing, approving, reproducing, and iterating on data knowledge across the company. Company data knowledge is vast and needs to service many stakeholders and use cases.

Even if a company adopts a data catalog, employees have to search through four separate locations when trying to find any data-related information: the data catalogue, a data dictionary, BI tools or Google Slides for analysis, and a Slack channel of common questions. With so much separation around search, most data knowledge continues to disappear into obscurity.Instead, **we are excited to announce Secoda's new "Data Portal", which allows every data team to create a home page for anyone search for data.**

Today, teams can collaborate in Secoda to document their data catalog, create the data dictionary, build analysis and answer common questions from one place. With this new change, teams can submit changes for review and publish a company wide "Data Portal" that contains all associated information about your data. One single plane to search for tables, analysis, queries, terms, common charts, events, syncs, ETL, and common questions.

### July 13, 2022

#### Features & Improvements

* Snowflake roles are used on table data preview
* Added Internal popularity
* Added a query block last run timestamp
* Last updated property added on resources
* Consolidate lineage tabs
* Highlight on matched search terms
* Caching between viewer/editor mode
* Added Looker Looks metadata
* Added Looker dialects
* Added frequent users metadata
* Improved default sort order on source
*
  * 50 additional bugs and improvements

### June 23, 2022

#### Features & Improvements

*   Improved search / load speed by 6x

    We've refactored some of our search queries to index metadata and content in Secoda much faster.
*   Editable table component across the entire app

    You can now bulk edit components in collections, columns, dictionary terms, questions and docs using the data table that many of you have enjoyed using. In addition, this allows editors to bulk delete, edit and customize their views to show viewers only what they need to see when looking through Secoda. We hope this change significantly speeds up your editing workflows in Secoda.
*   Data profiling V2

    We have launched a new version of our columns profiling, which now includes: Count, Max, Mean, Median, Min, Percent Filled, Unique counts as well as a detailed graph viewable in the column.
*   Markdown documentation in table descriptions

    Our column and table descriptions now render markdown. In order to write your documentation in markdown, you can double click on a description and toggle between the markdown editor and the preview of the markdown.
*   Questions tagging

    You can now tag resources in questions to see any related discussions to a resource. This can give business users a clear view of the types of questions others have asked about a resource and allows them to easily find what they are looking for in Secoda.
*   Lineage / schema change notifications

    Owners of resources now get notified when columns change or are added to a table that they are responsible for. In addition, Secoda will notify owners of downstream effected resources to make sure dashboards and terms stay up to date when there's changes associated to schema.
*   Link tables with Slack channels

    Each resource in Secoda can now connect to a unique slack channel. By connecting a resource to a Slack channel, data teams can monitor changes on a resource through Slack and can see a history of changes in specific channels.

### June 22, 2022

We're excited to announce our new Fivetran Integration. With this new integration, teams will be able to understand where the data in their warehouse is coming from and where is it going afterwards. The building blocks of data organization are sources that are driving data into the warehouse. Without visibility into how a Fivetran connector flows into a data source, a business user could have a more tough time navigating the data across their data warehouse.

To read more about how to configure this integration, you can visit [our docs](https://docs.secoda.co/integrations/fivetran-integration?q=fivetran).

### June 14, 2022

This week, we’ve launched a bunch of new features that will help with organization, documentation and activity tracking in Secoda.

#### Features & Improvements

*   Side sheets

    You can now preview a table in a side sheet view before navigating to it. This is also available for columns and accessible through lineage. We found that it was difficult to know if you were clicking on the right resource, with the new side sheet, you should be more confident if you’re going to a new resource.
*   Query documentation

    You can now document queries by clicking on queries in Secoda, you can add documentation to them and share them with others. This is a big feature that a lot of you have been asking about for a long time! We’re excited to introduce it.
*   Teams

    You can now see which group each member of your team belongs to and see what resources that team owns. You can use your groups to assign resource to multiple people and the navigate to see what different groups are able to use in Secoda.
*   Version history

    You can now see an activity log of changes to each resource by clicking on the clock icon on the top right hand corner of the resource. This can show you what different users have worked on in Secoda and helps to track down changes over time.

In addition, we've fixed many bugs, added some UI improvements to dictionary terms and made the search much faster.

### February 28, 2022

#### Features

* Column level lineage for Snowflake
* Query blocks on questions, dictionary terms, and resource documentation

#### Bug Fixes and Improvements

* Added API endpoints for adding, updating, and removing documentation on resources
* Fixed duplicate resources in collection list
* Fixed dbt core integration for `manifest.json` upload
* Improved efficiency of Snowflake lineage extractor
* Fixed updating profile name
* Fixed lineage graph and upstream/downstream showing duplicate tables
* Fixed related resources not being added to dictionary terms
* Fixed Airflow integration not extracting job runs
* Fixed Redash integration not working for v10

### February 14, 2022

#### Features

* ERD diagrams are available for database integrations (Postgres, MySQL, MS SQL, and Oracle)
* UI Update on the questions feature
* Oracle is now a supported integration.

#### Bug Fixes and Improvements

* Updated the demo data for new users on Secoda
* Added “Documents” sidebar option for viewers
* Fixed failing Postgres and Redshift extractions
* The Snowflake integration has been updated to make the integration setup easier
* Fixed pagination issues and updated pagination UI
* Fixed issue with installing the PowerBI integration

### January 31, 2022

#### Features

* SAML is now supported on the cloud version of Secoda

#### Bug Fixes and Improvements

* Primary and foreign keys are now pulled for Postgres and MySQL databases

### January 24, 2022

#### Features

* “All” resources can now be search for on the search page

#### Bug Fixes and Improvements

* Notifications have been updated to allow for notification preferences
* The matches in a search result are now highlighted
* Custom metadata properties can be added to dictionary terms

### January 17, 2022

#### Features

* A visual lineage graph has been released that enables users to have a graphical representation of their lineage

#### Bug Fixes and Improvements

* The scheduled extractions that were not running have been fixed to run properly
* The Looker integration has been updated to fix lineage issues.

### January 10, 2022

#### Features

* The metadata API is not publicly available which enables users to programatically access and update the resources in Secoda.
* The documentation editor has been improved to have backslash commands and is much faster compared to the previous version.
* An integration with Hightouch has been released to bring in syncs.
* An integration with dbt metrics enables users to bring their metric definitions into Secoda.

#### Bug Fixes and Improvements

### December 20, 2021

#### Features

* A git integration has been released that allows a user to sync their Secoda data to git
* Secoda now supports Aptible as a deployment method for on-premise customers

### December 13, 2021

#### Features

*   The table page UI has been extended to other resources in Secoda including dashboards, jobs, and collection

    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ec26d3b2-d991-4e72-a08d-ff209c5e5351/Untitled.png)

### December 6, 2021

#### Features

* The table page has a new UI that makes a better use of space on the page.

#### Bug Fixes and Improvements

* Column profiling has been improved to see additional metrics around min, max, and number of nulls

### November 29, 2021

#### Features

* Admins can now simulate how viewers see the workspace via the viewer toggle.

#### Bug Fixes and Improvements

* An onboarding checklist has been introduced to help new users onboard to Secoda
* Extractions now show the individual stages that have succeeded or failed along with the execution time for that stage
* Users can assign owners to a column
* Columns can be manually removed

### November 22, 2021

#### Features

* Admins now have an analytics dashboard to showcase how their Secoda workspace is being used.
* Admins also receive a weekly email that highlights the metrics in the analytics dashboard.

#### Bug Fixes and Improvements

* The dbt integration now pulls in the creation query for a particular model.

### November 15, 2021

#### Features

* A “magic wand” feature has been added which allows users to copy descriptions to similarly named columns.
* Templates for questions have been added which allow an admin to set a standard body for a question.
* Columns can now be profiled to show the distribution of values.

### November 8, 2021

#### Features

* Secoda now has a “Published” and “Draft” state for all resources. This helps you organize what viewers can see in the product. A viewer can only see resources when they are in a “Published” state.
* Snowflake, BigQuery, and Redshift now have “Common Queries” to see what queries are most frequently run against a particular table.

#### Bug Fixes and Improvements

* The Tableau integration now extracts popularity based on the number of views for a dashboard
* Service account users can now be removed from the popularity count for tables
* Fixed bug where search indices were not updating properly

### November 1, 2021 - 🔍 New Search UI

#### Features

* Secoda now has a new search UI to make it easier to browse all of your resources and get context directly from the search page

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ca1fe78f-6b20-4eed-81d4-68446afa9f5b/Untitled.png)

#### Bug Fixes and Improvements

* Slack app `/secoda` command has been fixed
* Added sorting capabilities on the questions table
* Added option to set a workspace level background image
* Fixed dbt core integration button to upload `manifest.json`
* Updated Slack integration to send notifications for question updates
* Added email notification for extraction status
* Added image block to the documents

### October 25, 2021 - Dashboard Integration Updates

#### Bug Fixes and Improvement

* Improved the Looker integration to extract views and explores
* Added asset ratings on tables
* Sorted upstream and downstream by depth level
* The Metabase integration now extracts question metadata
* The Tableau integration now extracts sheets
* All emails now must be verified on signup
* Search indexes are properly updated when a user is added or removed from a workspace

### October 18, 2021 - ↕️ Sorting and Extractor Improvements

#### Bug Fixes and Improvements

* Added a delete button on resources page
* Added relationships extractor for Microsoft SQL Server integration
* Added primary key extractor for Microsoft SQL Server integration
* Added "Submit a data request" button in navigation bar for viewers
* Added sorting options on dictionary, questions and browse page
* Added filter for view vs. table on the browse page
* Added ability to limit dbt integration by schema
* Added extractor for dashboard tags extractor from Tableau
* Added group option to invitation modal
* Added copy button for column names
* Fixed image upload not working on self-hosted Secoda
* Fixed Metabase dashboard links being broken
* Fixed Tableau dashboard links being broken
* Fixed analysis documents being archived instead of deleted
* Fixed Viewers being able to view workspace settings
* Fixed dictionary terms not be updated on browse page after an update
* Fixed view not updating when navigating between browse and catalog page
* Fixed dictionary term giving "Something went wrong" on creation
* Fixed adding owner to table not working
* Fixed Looker scheduled extractor not working

### October 4, 2021 - 🐞 Bug Fixes and Improvements Continued

#### Bug Fixes and Improvements

* Added popularity information for Snowflake integration
* Added ability to resize images on the documentation editor
* Added ability to send bulk invitations using a comma separated list of emails
* Added ability to edit the dictionary term owner
* Added searching by the documentation content
* Fixed admins not being able to view all resources in search page
* Fixed question replies not having the correct content after submission
* Fixed multiple dictionary terms showing up when using `@` functionality
* Fixed documentation editor breaking when clicking on a result that shows up using `@`
* Fixed documentation editor breaking when submitting a question response
* Fixed column description formatting issues
* Fixed underline formatting not working in documentation editor
* Fixed frequent users not showing up in Snowflake integration
* Fixed resource count not being accurate
* Fixed tables disappearing from the catalog randomly

### September 27, 2021 - 🐞 Bug Fixes and Improvements

#### Features

* We've updated our pricing model to be focused on a per editor pricing. All current customers will be unaffected. You can view the pricing update at [https://secoda.co/pricing](https://secoda.co/pricing)
* We've added [Collections](https://help.secoda.co/en/articles/5589453-collections) to help organize your resources for different teams in Secoda

#### Bug Fixes and Improvements

* Fixed Metabase extractor that broke for "Our Analytics" dashboards
* Fixed custom invitation links not working
* Fixed question updates not being indexed properly in search
* Fixed adding collections to table columns causing error
* Fixed collections not being instantly updated on search indexes
* Fixed Cancel button not working on New Question page
* Fixed users having multiple workspaces which lead to unexpected behaviour, i.e. logos being uploaded didn't save properly
* Fixed not allowing viewers to add tags to questions
* Fixed questions being duplicated when adding a second answer
* Fixed resource being hidden after assigning a group that an admin is not part of
* Added dictionary terms demo data
* Added ability to upload images to Readme documents

### September 13, 2021 - 🏗️ Infrastructure Update

#### Features

* Secoda had its largest infrastructure update to date last week which will help improve the speed, reliability, and scaling of the cloud application
* You can now limit the dashboards that are imported based on group **Integrations > **_**your integration**_** > Groups** and select which groups you'd like to import into Secoda

#### Bug Fixes and Improvements

* Fixed the scheduled extractions not running
* Fixed the paywall popup for users within the free trial limits
* Fixed demo data not being deleted after adding first integration

### September 6, 2021 - 🔍 Universal Search

#### Features

* The search in Secoda has been updated to index all of your resources. That includes Dictionary Terms, Analysis Documents, Questions, Tables, Dashboards, Users, Jobs and Tags. The main search bar will help you find all of these different items quickly.
* You can now limit the schemas that are imported into Secoda by going the **Integrations > **_**your integration**_** > Schema** and select which schemas you'd like to import into Secoda

#### Bug Fixes and Improvements

* Images can be uploaded in the documentation editor automatically
* Separated resources in "related resources" section
* Fixed documentation editor not being cleared for new questions form
* Fixed content not being cleared after posting a question reply
* Fixed image pasting multiple times in documentation editor after uploading an image
* Fixed tags not showing up in aggregate tag list after creating a new tag

### August 23, 2021 - Looker Integration

#### Features

* The Looker integration will extract your dashboards, LookML models and views from the platform and any associated metadata

#### Bug Fixes and Improvements

* Ask a question directly from Slack using the Slack integration
* Fixed sharing Analysis documents with everyone in the workspace
* Fixed BigQuery lineage extraction error

### August 16, 2021 - ✋ Data Questions

#### Features

* The data questions feature allows anyone to ask questions and have a collaborative conversation in Secoda.

#### Bug Fixes and Improvements

* Admins can remove members from a workspace
* Fixed sharing for Analysis documents

### August 9, 2021 - Metabase Integration

#### Features

* The Metabase integration will import all of the metadata associated with your Dashboards, Questions and Queries from the platform.

#### Bug Fixes and Improvements

* Added workspace setting to hide sensitive parameters
* Fixed code blocks behaviour where a code block was treated as inline code
* Fixed Tableau integration failing
* Fixed UI error where integration params where being overwritten after updating the params

### August 2 - 🙌 Improved Sharing

#### Features

* All resources now have a Share button in the top right corner that allows users to decide which groups and users can view a particular resource.

#### Bug Fixes and Improvements

* Admins can set the default share settings for their workspace
* Improved Snowflake documentation for determining what an "account" is
* Fixed removing all demo data when an integration connects
* Fixed showing analysis document query error

### July 26 - 🏘 Groups

#### Features

* You can now create groups is Secoda to organize the various people in your organization

#### Bug Fixes and Improvements

* Admins can specify which domains can join their workspace
* Fixed deleting cells in an analysis block

### July 19 - User and Schema Entities

#### Features

* You can now search for users in the catalog, and there is a page for database schemas where you can view all of the associated tables

#### Bug Fixes and Improvements

* Fixed special characters being encoded in database connection URLs
* Fixed improper app state after inviting a user

### July 12 - 📊 Analysis Documents

#### Features

* The Analysis Documents are a new feature in Secoda that enables users to query databases and associate queries with charts in a notebook format

#### Bug Fixes and Improvements

* Tableau integration extracts the CustomSQL Tables
* Fixed profile name update being shown around the app without refresh

### July 5 - Views Extraction for Data Warehouses

#### Features

* Postgres and Microsoft SQL Server now extract the views

#### Bug Fixes and Improvements

* Fixed free trial modal popping up when workspace is within free trial limits

### June 28 - Power BI Integration

#### Features

* The Power BI integration will extract your dashboards and data models from the platform and any metadata associated with them

#### Bug Fixes and Improvements

* Limit integration creation to only admins
* Added multi-line code blocks to the README documents
* Increased description character limit
* Added hover for long column names
* Fixed PII widget overflow in settings
* Fixed showing more than 4 popular resources on the home page
* Fixed creating tags for data dictionary

### June 21 - 📔 Data Dictionary

#### Features

* A new data dictionary section of Secoda to help define consistent metrics across your organization
* Tag entity which gives you an overview of all the resources that are associated with a tag

#### Bug Fixes and Improvements

* Fixed tags not being instantly updated
* Fixed related resources not being populated on Dictionary Term
* Fixed mentions not adding correct word
* Fixed owner changing on a dictionary term

### June 14 - 🔎 Search UI Update

#### Features

* The search page has been updated with more friendly filters and exploration of the different resources across your data ecosystem

#### Bug Fixes and Improvements

* Added optional role parameter in Snowflake
* Added user list on owner select
* Fixed Slack API Oauth flow
* Fixed copying an invitation link
* Fixed fuzzy search for tags
* Fixed last tag being removed

### June 7 - Airflow Integration

#### Features

* Airflow integration that extracts your Airflow DAGs, associated tasks and metadata

#### Bug Fixes and Improvements

* Invitation links now point to `https://app.secoda.co`
* Integration resources are deleted when the integration is deleted
* Integration extraction failures now show errors
* Billing shows correct plan a company is on
* Fixed dismissing background photo widget
* Fixed removing quick start when all tasks are completed

### May 31 - dbt Cloud Integration

#### Features

* dbt Cloud integration that will extract dbt jobs, models, and status updates from dbt's metadata API

#### Bug Fixes and Improvements

* Access tokens will be automatically renewed → This was leading to silent errors
* Fixed Redash dashboard link
* Set README to be in view mode as default
* Admin cannot change themselves to role "Viewer"
* User photos are consistent around the app

### May 24 - 🏠 New Homepage

#### Features

* Our homepage has been simplified to have a similar UX look and feel to Google
* Badges to mark resources as verified or PII data

#### Bug Fixes and Improvements

* Can edit dashboard owner
* Can edit description of dashboard
* Bug reports can now be sent from Secoda
* Improved spacing on Column descriptions

### May 17 - ☁️ Secoda On Prem & Table Lineage

#### Features

* Table lineage for upstream & downstream tables with support on BigQuery, Redshift and Snowflake
* Self hosted version is available to be used inside of a company's cloud infrastructure. All metadata is contained within the machine's on the company's cloud and not sent to our cloud databases
* Homepage UI/UX update
* Upload custom profile, workspace, and background images

#### Bug Fixes and Improvements

* Tags redirecting to search page are now faster
* Column level tagging
* Linking dashboards to tables in the resource details pages
* Fixed demo data images being broken
* Fixed popular tables not loading on first load

### May 3 - 📋 Data Debt Backlog

#### Features

* Popularity of Snowflake resources
* Table ↔ Dashboard relationships on the dashboard and table details page
* Data debt backlog to show unused, stale, and undocumented data resources
* Microsoft SQL Server integration
* Rich text editor for documentation on resources
* Slack application that can help you search for resources and be notified about resource updates

#### Bug Fixes and Improvements

* Enforced email address on resource owner input
* New UI for resource owner editor
* Changed documentation to not be default on
* Removed schema updates for demo tables
* Added ability to edit integration parameters
* Fixed demo dashboards not being removed
* Fixed markdown not being rendered in descriptions of resources
* Fixed emails pointing to localhost

### April 11 - 🔔 Staying Notified

#### Features

* In app notifications log for updates on metadata including descriptions, tags and owners
* Schema change notifications
* User roles for each workspace member including **admin, editor, and viewer**
* Microsoft SSO
* Popularity for Redshift and BigQuery tables

#### Bug Fixes & Improvements

* Helper documentation on integration connection page
* Change user name
* Removing stale data when deleted from a data source
* Removal of demo data

### March 28 - 🔃 Switching from Amundsen

#### Features

* Import & export descriptions from Amundsen into Secoda
* Add & remove demo data from the Workspace Settings page
* Change your extraction schedule from the **Integrations > Integration > Schedule** page

#### Bug Fixes

* Snowflake extraction connections not closing (this was causing issues for other extractions on the platform)
* Integrations name not being correctly displayed on the Integration page
* Added extraction schedule for all workspaces

### March 22 - 📊 Demo Data and Data Previews

#### Features

* For any new workspace that is created, we add a set of demo data to highlight the main features of Secoda
* Redshift and Postgres have a 50 row preview of data with the "Preview" button the the table details page
* There is a **Quick Start** guide in the bottom left corner of the app to get you setup on Secoda
* Automated metadata extractions happen every 24 hours for your connected integrations
* Intercom product tour to give you an overview of Secoda → Any feedback on what could be improved is helpful

#### Bug Fixes

* The Search page now defaults to show all of your data resources
* You can change your workspace name in your workspace settings
* Bookmarking on the search page now works
* Forgot password email now sends a reset email
* Postgres and Redshift integrations now extract metadata for any version of the platforms

### March 15 - 🔌 Self Service & Dashboard Integrations

#### Features

* Secoda is now self service, anyone can signup without being on a waitlist
* Integration support for Redash, Mode, and Tableau
* Intercom support - if you have any questions you can now ask directly from the platform
* Secoda community - [Join](https://join.slack.com/t/secodacommunity/shared\_invite/zt-mhnu278g-FktKZmZ51SDQtlu3NRAxqg) our community of Secoda users

#### Bug Fixes

* Invitation and resource update emails now send
* Adding tags to tables
* Big Query integration not running scheduled extractions
* Show team members in Settings
* Show integration extraction history
* Descriptions added in Secoda are no longer overwritten
* Resource count is not updated when integration is connected

### March 1 - ⚙️ Settings & Pricing Plans

#### Features

* Now you can manage your workspace settings, team members, and view pricing plans for Secoda.
* We've added a "**Resource count**" to indicate how many resources your workspace is using and if it's approaching your pricing tiers limit
* **Google authentication** has been added

#### Bug Fixes

* The scheduler for the metadata extraction process was rewritten to fix some issues we were having in production
* Table descriptions, column descriptions, table owners and bookmarks automatically update in the table details view
