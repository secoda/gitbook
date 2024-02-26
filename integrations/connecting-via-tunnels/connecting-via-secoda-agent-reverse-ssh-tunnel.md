---
description: This page walks through connecting your data sources via a Reverse SSH Tunnel
---

# Connecting via Reverse SSH Tunnel

## **Getting Started**

The Reverse SSH Tunnel is used securely connect local data sources without opening ports, while encrypting data in-transit.

### **Setup**

On your own EC2/VM, you will run the `secoda/agent` docker image. You can use docker-compose, like so:

```yml
version: "3"
services:
  agent:
    restart: always
    image: "secoda/agent:latest"
    environment:
      - SSH_USER=
      - SSH_HOST=
      - SSH_LISTEN_PORT=
      - SSH_KEY_BASE64=
      - WAREHOUSE_HOST=
      - WAREHOUSE_PORT=
```

Secoda Agent is an Enterprise feature. Your enterprise contact at Secoda will provide you with the values for the environment variables.

### **Running**

Once you have inputted the values, you can run the Secoda Agent with:

```bash
docker-compose up -d
```

### Troubleshooting

Upon running the agent, if the agent becomes stuck on the version number during the startup process, similar to:

```bash
agent  | OpenSSH_9.3p2, OpenSSL 3.1.3 19 Sep 2023
```

This typically means that the outbound connection is blocked. Please check your firewall settings. Secoda can adjust the outbound port to a whitelisted one if necessary.
