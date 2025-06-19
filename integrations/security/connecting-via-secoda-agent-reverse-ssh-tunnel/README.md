---
description: This page walks through connecting your data sources via a Reverse SSH Tunnel
---

# Connecting via Reverse SSH Tunnel

## **Getting Started**

The Reverse SSH Tunnel is used securely connect local data sources without opening ports, while encrypting data in-transit. By default, this option supports multiple concurrent integration syncs.&#x20;

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

To retrieve the docker compose environment for your tunnel, go to [https://app.secoda.co/tunnels](https://app.secoda.co/tunnels) and create a new reverse tunnel.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/e6807591-f663-464a-837c-cca19a138e17.png" alt="" width="375"><figcaption></figcaption></figure>

Copy the details to your clipboard, and replace the contents of your docker compose file with this configuration.



## Running

### **docker-compose (recommended)**

Once you have inputted the values in **Setup**, you can restart the Reverse SSH agent with:

```bash
docker-compose down
docker-compose up -d
```

### Custom

```bash
#!/bin/sh

SSH_USER=tunnel
SSH_HOST=...
SSH_HOST_PORT=...
SSH_LISTEN_PORT=...
SSH_KEY_BASE64=...

mkdir -p /root/.ssh
chmod 600 /root/.ssh

if [ ! -z "$SSH_KEY_BASE64" ]; then
    echo "Creating ssh key"
	echo $SSH_KEY_BASE64 | base64 -d | tee /root/.ssh/id_rsa > /dev/null
	chmod 600 \
		/root/.ssh/id_rsa
fi

# A predefined host key in SSH is used to verify the identity of a remote server,
# ensuring a secure connection by preventing man-in-the-middle attacks.
echo "Adding the predefined host key for $SSH_HOST"
TEMPFILE=$(mktemp)
echo "[$SSH_HOST]:$SSH_HOST_PORT ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBo2+mYwlNTvJXrNCETYHrrHyUGMnWdQO5vEhFVU833o" > $TEMPFILE
 
echo "Attempting tunnel with $SSH_USER to $SSH_HOST:${SSH_HOST_PORT:-22}"

autossh -N -M0 -vvv \
    -o "ExitOnForwardFailure yes" \
    -o "ServerAliveInterval 15" \
    -o "ServerAliveCountMax 4" \
    -o "ControlPath none" \
    -o "UserKnownHostsFile=$TEMPFILE" \
    -o StrictHostKeyChecking=yes \
    -R 0.0.0.0:$SSH_LISTEN_PORT \
    $SSH_USER@$SSH_HOST -p $SSH_HOST_PORT
```

### Using the reverse tunnel

On an integration credentials page, fill in the integration connection details. DNS names are resolved on the agent, so you may use local hostnames.

Select the reverse tunnel you would like to use then click "Test connection".

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/d634e6ca-a785-4ca4-87f9-211cf4958137.png" alt="" width="375"><figcaption></figcaption></figure>

### Troubleshooting

**Issue: Agent Stuck on Version Number During Startup**

**Symptom:** The agent displays its version (e.g., `agent | OpenSSH_9.3p2, OpenSSL 3.1.3 19 Sep 2023`) and does not proceed with the startup process.

**Likely Cause:** Outbound network connection is blocked.

**Troubleshooting Steps:**

1. **Check Firewall Settings:** Verify your firewall rules to ensure outbound connections are not being blocked for the agent.
2. **Contact Support (if necessary):** If firewall adjustments are not feasible or don't resolve the issue, contact Secoda support. We can assist in configuring the agent to use a whitelisted outbound port.



#### **Issue: DNS Resolution Error During Integration**

**Symptom: Integration fails with the error: `"Error: Unable to find the DNS query names for <DNS_NAME>. Please check the spelling and try again."`**

**Likely Cause:** The reverse tunnel instance cannot resolve the hostname of the target database server.

**Troubleshooting Steps (on the reverse tunnel instance):**

1. **Verify DNS Resolution:**
   *   Execute the following command to check DNS resolution for the database server's hostname:

       ```
       dig <DATABASE_HOSTNAME>.<DOMAIN_SUFFIX>.<TLD>
       ```

       _(Replace `<DATABASE_HOSTNAME>.<DOMAIN_SUFFIX>.<TLD>` with the fully qualified domain name of your database server, e.g., `yourdb.yourcompany.com` or `yourdb.local`)._
   * **Expected Output:** A successful `dig` command should return the IP address of the database server.
2. **Check Port Connectivity:**
   *   Use `telnet` to verify connectivity to the database server on its standard SQL port (default 1433):

       ```
       telnet <DATABASE_HOSTNAME>.<DOMAIN_SUFFIX>.<TLD> 1433
       ```
   * **Expected Output:** A successful connection will display a blank screen or a "Connected to..." message. Press `Ctrl + ]` then type `quit` to exit.
3. **Inspect Docker Container (if applicable):**
   * If the reverse tunnel agent is in a Docker container, check DNS resolution _from within_ the container:
     *   **a. Find Container ID:**

         ```
         docker ps
         ```

         (Note the `CONTAINER_ID` of the reverse tunnel agent.)
     *   **b. Access Container Shell:**

         ```
         docker exec -it <CONTAINER_ID> /bin/bash
         ```
     *   **c. Perform In-Container DNS Check:**

         ```
         apt-get update && apt-get install dnsutils -y # Install if not present
         dig <DATABASE_HOSTNAME>.<DOMAIN_SUFFIX>.<TLD>
         ```
     * **Expected Output (in-container):** A successful `dig` command from within the container should return the IP address of the database server.
