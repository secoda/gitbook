---
description: This page walks through connecting your data sources via the Secoda Agent
---

# Connecting via Secoda Agent (Reverse SSH Tunnel)

## **Getting Started**

**The Secoda Agent**  implements a Reverse SSH Tunnel to securely connect local data sources without opening ports, while encrypting data in-transit.

### **Setup**

On your own EC2/VM, you will run the Secoda Agent as a docker image. You can use docker-compose, like so:

```yml
version: "3"
services:
  agent:
    image: "secoda/agent:latest"
    environment:
      - SSH_USER=
      - SSH_HOST=
      - SSH_LISTEN_PORT=
      - SSH_KEY_BASE64=
      - WAREHOUSE_HOST=
      - WAREHOUSE_PORT=
```

Secoda Agent is an enterprise preview feature. Your enterprise contact at Secoda will provide you with the values for the environment variables.

### **Running**

Once you have inputted the values, you can run the Secoda Agent with:

```bash
docker-compose up -d
```
