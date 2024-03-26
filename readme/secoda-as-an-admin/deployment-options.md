---
description: Check out the deployment options for setting up Secoda.
---

# Deployment options

Secoda offers three main deployment options depending on your organization's needs.

## **Multi-Tenant Cloud**

You can select from the following regions for hosting our multi-tenant Cloud version of the app:

1. US (us-east-1)
2. EU (eu-central-1)
3. APAC (ap-southeast-1)

With our multi-tenant setup (and most software SaaS), organization's application data is stored on a shared database. All application data is stored within a private VPC and is separated at the software-level using row-level security, global checks, and automated tests to ensure data is securely separated.

## **Single-Tenant Cloud**&#x20;

A single-tenant Cloud set up is an isolated version of the app in it's own VPC  in the region of your choice. The following holds true for this option:

* All of your organization's application data exists in it's own database that is not shared with any other Secoda customers.&#x20;
* The Secoda team manages all application upgrades and infrastructure changes.&#x20;
* You can select your own custom URL, i.e, https://test.secoda.co.

This provides stronger security guarantees, dedicated resources, and can offer lower latency by configuration in a nearby AWS region.

## [**Self-Hosted**](../../self-hosted-secoda/) (On-Premise)

There are three options for self-hosting Secoda:

1. [AWS ECS](https://github.com/secoda/terraform-aws-secoda)  (recommended)
2. [Docker Compose](https://github.com/secoda/docker-compose)
3. [Kubernetes](https://github.com/secoda/helm)

{% hint style="info" %}
The self-hosted options require DevOps support from the customer and Secoda which can result in higher costs.
{% endhint %}

