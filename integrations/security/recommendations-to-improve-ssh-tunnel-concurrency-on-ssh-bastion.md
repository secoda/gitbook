# Improve Concurrency on your SSH Bastion

### 1. **Increase `MaxSessions` on SSH Bastion**

* **Purpose**: The `MaxSessions` parameter limits the number of concurrent sessions (logical channels) allowed over a single SSH connection. Increasing this value allows more port forwarding sessions to run simultaneously without opening multiple SSH connections.
* **Action**:
  *   Edit the SSH server configuration on the bastion host (`/etc/ssh/sshd_config`):

      ```plaintext
      MaxSessions 50  # Increase as necessary
      ```
  *   Restart the SSH server:

      ```bash
      sudo systemctl restart sshd
      ```

### 2. **Increase `MaxStartups` on SSH Bastion**

* **Purpose**: The `MaxStartups` parameter controls the number of simultaneous unauthenticated SSH connections allowed. Increasing this value prevents new connections from being rejected when a large number of SSH sessions are established.
* **Action**:
  *   Edit the SSH server configuration on the bastion host (`/etc/ssh/sshd_config`):

      ```plaintext
      MaxStartups 50:30:200  # Adjust for higher concurrency
      ```
  *   Restart the SSH server:

      ```bash
      sudo systemctl restart sshd
      ```

### 3. **Increase System Resource Limits**

* **Purpose**: System limits on file descriptors and processes can impact the number of concurrent SSH connections or tunnels. Increasing these limits can help support more concurrent sessions.
* **Action**:
  *   Check and increase the file descriptor limit (`ulimit -n`):

      ```bash
      ulimit -n 65535
      ```
  *   Edit `/etc/security/limits.conf` to increase the limit for your user:

      ```plaintext
      your-username soft nofile 65535
      your-username hard nofile 65535
      ```
  *   Adjust systemd limits if needed (for example, `/etc/systemd/system/ssh.service`):

      ```plaintext
      [Service]
      LimitNOFILE=65535
      LimitNPROC=65535
      ```
  *   Reload systemd and restart SSH:

      ```bash
      sudo systemctl daemon-reexec
      sudo systemctl restart sshd
      ```
