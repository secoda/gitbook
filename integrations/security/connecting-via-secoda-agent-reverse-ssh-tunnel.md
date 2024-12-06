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
      - SSH_PORT=
      - SSH_HOST=
      - SSH_LISTEN_PORT=
      - SSH_KEY_BASE64=
```

To retrieve the docker compose environment for your tunnel, go to [https://app.secoda.co/tunnels](https://app.secoda.co/tunnels) and create a new reverse tunnel.&#x20;

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/e6807591-f663-464a-837c-cca19a138e17.png" alt="" width="375"><figcaption></figcaption></figure>

Copy the details to your clipboard, and replace the contents of your docker compose file with this configuration.

### **Running the agent**

Once you have inputted the values, you can restart the Secoda Agent with:

```bash
docker-compose down
docker-compose up -d
```

### Using the reverse tunnel

On an integration credentials page, fill in the integration connection details. DNS names are resolved on the agent, so you may use local hostnames.

Select the reverse tunnel you would like to use. Test connection.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/d634e6ca-a785-4ca4-87f9-211cf4958137.png" alt="" width="375"><figcaption></figcaption></figure>

### Troubleshooting

Upon running the agent, if the agent becomes stuck on the version number during the startup process, similar to:

```bash
agent  | OpenSSH_9.3p2, OpenSSL 3.1.3 19 Sep 2023
```

This typically means that the outbound connection is blocked. Please check your firewall settings. Secoda can adjust the outbound port to a whitelisted one if necessary.
