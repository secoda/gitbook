---
description: An overview of the ServiceNow extension with Secoda
---

# ServiceNow

## Getting Started with ServiceNow

ServiceNow is an extension that allows you to sync all access request status between Secoda and ServiceNow. There are three steps to getting started using ServiceNow with Secoda

{% hint style="info" %}
Please note: Secoda relies heavily on email ids of the creator and reviewer of Access Requests. Thus, Secoda emails and ServiceNow emails must align.
{% endhint %}

### Connect ServiceNow to Secoda

To connect your ServiceNow instance to Secoda:

1. In the Secoda app, navigate to **Settings > Extensions**.
2. Click Connect Extension and search for and select ServiceNow.
3. Choose your preferred authentication method:
   * **Credentials** (username + password), or
   * **OAuth** – [follow this guide](https://www.servicenow.com/community/developer-blog/up-your-oauth2-0-game-inbound-client-credentials-with-washington/ba-p/2816891) to retrieve your `client_id` and `client_secret`.
4. Fill in the Host field with your ServiceNow instance URL (e.g., `https://devXXXXXX.service-now.com`).
5. Provide the Form Table:
   * In ServiceNow, navigate to **System Definition > Tables**.
   * Use the Name of the form table you wish to use.
   * We recommend using a table that extends Request Task (check the Extends Table column).
6. Optionally fill in the **Field Map** to customize field mappings between Secoda and ServiceNow (see next section).
7. Optionally, you can use REST API for communication. Follow the steps below to set this up - fill out the **Api Path** with the Resource Path you get from ServiceNow (`/api/#####/api_id`).&#x20;
8. Click Submit to save the integration.

### Optional: Using REST Communication

If you prefer to implement custom behaviour, you can do so via REST with JSON as data exchange format. The steps are as follows:&#x20;

1. In ServiceNow, navigate to **System Web Services > Scripted Web Services > Scripted REST APIs**
2. Create New, give your API a name, which will automatically create an API ID for you, then click submit.&#x20;
3. Now, using the search bar filtering on Name, look for the API you just created and click on it.&#x20;
4. Scroll down until you see Resources. We will create two new resources: a POST method and a PATCH method.&#x20;

#### POST Method

* Name: Any descriptive name
* HTTP Method: POST
* Relative Path: `/`
* Take note of the Resource Path: this is what you will enter when creating the Secoda extension, under Api Path.&#x20;
* Use Case: Triggered when a new Data Access Request is submitted in Secoda.
* Script: the most important part of using REST APIs. You will get the data from Secoda through `request.body.data`.  Your script must have the following return signature:

```
(function process(/*RESTAPIRequest*/ request, /*RESTAPIResponse*/ response) {
    // your code

    response.setStatus(201);
    response.setBody({
        sys_id: '---fill here---',  // Unique ID of the created record in ServiceNow
        record_url: '---fill here---',  // URL to open the ServiceNow record in Secoda
    });
})(request, response);
```

#### PATCH Method

* Name: Any descriptive name
* HTTP Method: PATCH
* Relative Path: `/`
* Use Case: Secoda calls this to update the status of an existing request
* Script: Does not need to return `sys_id` or `record_url` in the response

#### Payload

This is the payload that will be given to you as a JSON dict from Secoda.&#x20;

```
payload = {
    "method": "create" or "update",
    "secoda_request_id": store this, it's what you will send back in the webhook,
    "state": one of "Open", "Closed Complete", "Closed Skipped",
    "status": one of "requested", "approved", "rejected",

    "requested_text": request reason,
    "expires_at": request expiry date,
    "created_by": email of user who created the request
    "created_at": ,
    "requested_expires_at": request expiry date,
    "requested_resources": json dump of all requested_resources,
    "assigned_to_group": first group that is an owner of requested resources,
    "assigned_to_user": first user that is an owner of requested resources,

    "approved_at": ,
    "approved_by": email of aprover
    "approved_text": ,
    "cancelled_at": ,
    "cancelled_by": email of the user that cancelled the request
    "cancelled_text": ,
    "rejected_at": ,
    "rejected_by": email of the user that rejected the request,
    "rejected_text": ,

    "sys_id": this is the sys id that you send through POST, that you will need in PATCH
}
```

### Optional: Creating your Field Map

{% hint style="info" %}
Note: This is not needed if you are using REST API for communication
{% endhint %}

The default Field Map is the following:&#x20;

```
default_field_map = {
  "short_description": "short_description",  // displays the data request ID
  "description": "description",
  "secoda_request_id": "secoda_request_id",
  "status": "approval",
  "state": "state",
  "expires_at": "secoda_expires_at",
  "created_by": "opened_by",
  "assigned_to_group": "assignment_group",
  "assigned_to_user": "assigned_to",
  "created_at": "opened_at",
  "approved_at": "closed_at",
  "approved_by": "assigned_to",
  "rejected_at": "closed_at",
  "rejected_by": "assigned_to",
  "cancelled_at": "closed_at",
  "cancelled_by": "assigned_to",
  "approved_text": "work_notes",
  "rejected_text": "work_notes",
  "cancelled_text": "work_notes",
  "requested_text": "description",
  "approved_expires_at": "due_date",
  "requested_resources": "work_notes",
  "requested_expires_at": "due_date",
}
```

The left hand side values all represent Secoda fields, and the right hand side values represent the mapping to ServiceNow fields (must use the element name, not the label).&#x20;

You can use the Field Map input when connecting the extension to modify this default field map. For example, if you want to store your status in a field called 'servicenow\_status' instead, you can pass in the following to Field Map:&#x20;

```
{'status': 'servicenow_status'}
```

{% hint style="info" %}
We recommend configuring your ServiceNow form to use status values that match Secoda: "Requested", "Approved", and "Rejected".
{% endhint %}

Once the integration is connected, creating a new access request in Secoda will create a corresponding record in ServiceNow, and status changes in Secoda will reflect in ServiceNow automatically.

### Creating a Webhook from ServiceNow

To send approval updates back to Secoda, we need to create a Webhook in ServiceNow.&#x20;

1. In ServiceNow, navigate to **System Definitions > Business Rules**.&#x20;
2. Click New to create a new record.&#x20;
3. Fill in:
   * Name: A meaningful name (e.g., `Secoda Access Update`)
   * Table: Use the same table name you provided in the Form Table when connection the extension.
   * Check Advanced.
4. Under When to run:
   * Set When to `async`
   * Enable the Update checkbox
   * Set Filter Condition:
     * `Approval is Approved` **OR**
     * `Approval is Rejected`
5. Under Advanced, add the following script. Then you can enable the webhook by clicking Submit. Any updates on ServiceNow will also sync in Secoda!

```
(function executeRule(current, previous /*null when async*/) {
    var r = new sn_ws.RESTMessageV2();
    r.setEndpoint("https://app.secoda.co/integration/servicenow/webhook/");
    r.setHttpMethod("post");

    // Set headers
    r.setRequestHeader("Content-Type", "application/json");

    // Payload with just the sys_id
    var payload = {
        secoda_request_id: current.sys_id.toString(),
		reviewer_email: gs.getUser().getEmail(),
		status: current.approval.toString()
    };

    r.setRequestBody(JSON.stringify(payload));

    try {
        var response = r.execute();
        gs.info("Secoda webhook sent. Status: " + response.getStatusCode());
    } catch (ex) {
        gs.error("Failed to send Secoda webhook: " + ex.message);
    }
```

