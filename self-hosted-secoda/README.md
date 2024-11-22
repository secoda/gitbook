---
description: Self-hosted or on-premise
---

# Self-Hosted

### **Installing Secoda On-Premises**

Secoda offers multiple on-premises installation options, ranging from a Docker Compose setup to fully automated Kubernetes deployments in AWS EKS or GCP GKE. All Secoda services are distributed as container images, designed to run on any Docker-compatible container engine.

### **Recommended Installation for AWS**

For a balance of production-readiness, ease of installation, and manageability, we recommend using the **AWS ECS Terraform module**.&#x20;

[Secoda Terraform Module](https://github.com/secoda/terraform-aws-secoda)

### **Kubernetes Installation Options**

For greater flexibility but also higher complexity, we offer three Kubernetes deployment methods.

[Fully Automated EKS (AWS EKS Deployment)](https://github.com/secoda/aws-eks-self-hosted)

[Fully Automated GKE (GCP GKE Deployment)](https://github.com/secoda/gcp-gke-self-hosted)

[Generic Secoda Helm Chart](https://github.com/secoda/secoda-helm-generic)

The fully automated options install Secoda along with all necessary network and service dependencies. However, enterprise customers with specific security or operational requirements often prefer the **Generic Helm Chart**, which focuses solely on installing Secoda services. This option allows customers to customize their networking, Kubernetes engine, and service dependencies.

### **Trial or Testing Setup**

For quick trials or non-production environments, Secoda provides a lightweight **Docker Compose setup.**

[Docker-Compose](https://github.com/secoda/docker-compose)

### **Resource Requirements**

For detailed information on the resources required to run Secoda in a production environment — or to understand the setup handled by automated installation packages — refer to the README file in the [Generic Secoda Helm repository](https://github.com/secoda/secoda-helm-generic).

### **SAML**

[okta-saml.md](../saml/okta-saml.md "mention")

[microsoft-azure-ad-saml.md](../saml/microsoft-azure-ad-saml.md "mention")



{% hint style="info" %}
Not using Secoda to manage your data documentation yet? Sign up for free [here](http://app.secoda.co/) 👈
{% endhint %}
