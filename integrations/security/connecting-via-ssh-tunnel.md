---
description: This page walks through connecting your data sources via a direct SSH tunnel
---

# Connecting via SSH Tunnel

## **Getting Started with SSH Tunnels** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

Tunnels require you to run an SSH server process ([SSHD](https://www.ssh.com/academy/ssh/sshd)) on a host accessible from the public internet. These hosts are often referred to as jump hosts or Bastion hosts and can be set up in nearly all cloud providers. The sole purpose of these host is to provide access to resources in a private network from an external network like the internet.

### Set Up

There are three main steps to set up a tunnel:

1. Configure a host in your environment that is accessible from the public internet. Make sure the [Secoda IP address](../../faq.md#what-are-the-ip-addresses-for-secoda) is whitelisted.
2. [Create a Tunnel in Secoda](https://app.secoda.co/tunnels/) and add in the configuration details from the host (`SSH Username`, `SSH Hostname`, `Port`). Once you submit these details, a Public Key will be shown.
3. Add the Public Key to the `authorized_keys` file in your host.

#### AWS

* Create an EC2 instance from the AWS Management Console in a public subnet in the same VPC as the resource that you'd like to integrate with Secoda.
* Add the SSH key from Secoda.
* Create a Security Group for this instance, and add an inbound rule for the Secoda IPs.
* Make sure the EC2 instance has access to the resource that you'd like to integrate with Secoda. This might mean adding an inbound rule for the IP of the EC2 instance to the database or source that you're integrating with Secoda.

#### Azure Cloud

* Create a Virtual Network from the Azure console, that has access to the database or datasource that you'd like to integrate with Secoda. Make sure the Azure firewall is enabled for this network.
* Create a Virtual Machine. This machine is acting as the jump server. This VM does not need an public access, but must have access to the database or datastore that is meant to integrate with Secoda.
* Go to your firewall rules, and add a NAT rule.
  * Protocol should be set to TCP
  * Source IP address should be set to the [Secoda IP Address](../../faq.md#what-are-the-ip-addresses-for-secoda)
  * Destination IP address should be the IP address of your Firewall
  * Default Port is 22
  * Translated IP address should be the IP address of the Virtual Machine
* From within your instance, you'll need to create a user and set up the SSH key provided by Secoda. The follow commands are recommended to do this:

```xml
# Create a new non-admin user for Secoda
$ sudo useradd -m secoda 

# Switch to the new user
$ sudo su - secoda 

# Create an SSH folder if one doesn't already exist
$ mkdir -p ~/.ssh 

# Set restrictive permissions on the .ssh folder
$ chmod 0700 ~/.ssh 

# Navigate into the .ssh folder
$ cd ~/.ssh 

# Create or open the authorized_keys file, add a Public Key to this file, and save it
$ vi authorized_keys 

# Set restrictive permissions on the authorized_keys file
$ chmod 0600 authorized_keys

# Exit the 'secoda' user session
$ exit

# Restart the SSH service (systemd-based systems)
$ sudo systemctl restart ssh 

# Restart the SSH service (SysVinit-based systems, if applicable)
$ sudo service ssh restart
```

### Connecting your Integration using a Tunnel

Once your tunnel has been made, navigate to the source that you're integrating with. On the connect page, add the credentials for the datasource.

At the bottom of the connect page, you'll see the option to add a tunnel. Click on the arrow to see a drop down menu with your recently created Tunnel. Select this tunnel, and click Test Connection to complete your integration setup!

![](https://secoda-public-media-assets.s3.amazonaws.com/6fec8c62-f468-4411-8ade-6dca075dda43.png)

## Troubleshooting

If you're having trouble establishing a connection with a standard tunnel, check the following:

1. **Whitelist the Secoda IP**\
   Ensure that the Secoda IP is whitelisted on your Bastion host.
2. **Verify the Public Key**\
   Confirm that the public key provided during tunnel creation is correctly added to the `~/.ssh/authorized_keys` file of the user on the Bastion host.
3.  **Check Permissions on SSH Files**\
    Ensure that the permissions on SSH-related files and directories are set correctly:

    * `~/.ssh` directory: `0700`
    * `~/.ssh/authorized_keys` file: `0600`

    **Note:** The permissions for `authorized_keys` should be `0600` (not `0644`) to maintain strict security compliance.
4.  **Concurrency**

    To improve the number of concurrent connections using a single SSH tunnel please refer to [recommendations-to-improve-ssh-tunnel-concurrency-on-ssh-bastion.md](recommendations-to-improve-ssh-tunnel-concurrency-on-ssh-bastion.md "mention")
5.  **Test Network Connectivity**\
    Verify that the Bastion host can connect to your data source. Replace `$data_source_host` and `$data_source_port` with the actual hostname and port of your data source.

    ```
    Copy code
    ```

    ```bash
    nc -z $data_source_host $data_source_port
    ```

*   Check that you can use the bastion host from your personal machine. You will need to use _your own_ private and public keys, not the public key from the above step. Replace the values where appropriate.

    ```
    ssh -L localhost:1111:<POSTGRES_URL_OR_IP>:5432 -i <PRIVATE_KEY_NAME>.pem <BASTION_USER>@<BASTION_IP> psql -h localhost -P 1111 -U secodapostgres
    ```
