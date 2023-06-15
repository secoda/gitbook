---
description: This guide is only for Docker-Compose.
---

# Configure TLS (Docker-Compose)

## Prerequisites:

* Ensure that a certificate has been created for the domain name that will be used to access the Secoda platform. Ensure that it is a valid, signed certificate.

Setup: Add the following to the docker-compose directory:

* `on-premise.crt` - the X509 certificate file in PEM format
* `on-premise.key` - the private key file in PEM format

Then uncomment the following lines in the `docker-compose.yml` file:
