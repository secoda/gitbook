---
description: This page walks through connecting your data sources via a direct SSH tunnel
---

# Connecting via SSH Tunnel

## **Getting Started with SSH Tunnels** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

Tunnels require you to run an SSH server process ([SSHD](https://www.ssh.com/academy/ssh/sshd)) on a **Bastion Host** accessible from the public internet. Bastion hosts can be set up in nearly all cloud providers, though instructions for set up may differ slightly.&#x20;

{% hint style="info" %}
For more information on setting up a Bastion host in your environment, check out the AWS documentation [here](https://aws-ia.github.io/cfn-ps-linux-bastion/#\_overview), or the Azure documentation [here](https://learn.microsoft.com/en-us/azure/bastion/).
{% endhint %}

The Secoda app will open an SSH connection to your Bastion, then open a port forwarding connection to the private service that you specify. Ensure your Bastion host has whitelisted our NAT Gateway address: `35.175.75.15`

#### Setup <a href="#h_7ee5f8a430" id="h_7ee5f8a430"></a>

Open up the `authorized_keys`(or equivalent) file in your Bastion host. Example below:

```
nano ~/.ssh/authorized_keys
```

Add the **public key** provided by Secoda to this file. You can find the public key from the application by navigating to [https://app.secoda.co/tunnels/new](https://app.secoda.co/tunnels/new). Example below:&#x20;

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDMRSB7sRm7HwEUC/TbvBtKKWLYgt1P8K+Xs5CyPqHVKqGbHThhx9HCqxqoVagGBIcdlImfJIBy0PuRKj9/H994o5Vxc5irQ/fpw1jx71sdSGA4Bgn38/qQaRyU7YS0PUZ7JC4otjKHP2k7vgC3/pYcR/A2g0fg/31lORjWqLjMsxrwQGbI6Mw56fwfqMXrAm/BZaK6nHUHRTZkdNgozENZQTYyptjv/vkpGgZoTAOeeY+UK0A30nOVB4Gv+3f0P/50K+CHQJO1t8SXJIJNs2h6qWPwiHLN9+2soWCu7ojH/a9keOSj+i/SDpu8calZl0qxaoFQwYbcXyH1X7Xr5MY2GTJyuzc4UatvNVJrSsAv/Wm+9jQLWNuGtdtoUUi6uTCukMxD10uvgNvGqoPfAWdUFVKbvRywWaPXd0FuaqeEt/I/sYEy2lP53Pf4DtAouCphmwHDVMaK4GEJwHwRAdJ34dR8oB4KDrz1mxjeopD/HN97hUa/O6fMy3oGY/XIZPVwivyGP3P7mIbmryIjGT15xVFr08cSY2h90P+/tWWAkkCVxcdn5vX3X7sqUFBDiPYQRPj5rpKgOgxoNTEzWWV8hkyXqSsO9mQmlkCMV0XndOwY64IoxBm8k+GKVI29ZzMrmpNLZi2L3SYA0oSgssORMghuyk8kfW9ZnUB5ptm+MQ== [ssh@secoda.co](<mailto:ssh@secoda.co>)
```

#### Troubleshooting <a href="#h_4e44bc0849" id="h_4e44bc0849"></a>

If you're having trouble establishing a connection with a standard tunnel, check the following:

* Check that the Secoda IP `35.175.75.15` is whitelisted on your Bastion host.
* Check that the public key _**we provide you**_ on tunnel creation is in the `~/.ssh/authorized_keys` file.
* Check permissions on the SSH files.
  * `~/.ssh` directory should be `0700`
  * `~/.ssh/authorized_keys` file should be `0644`
* Check that the Bastion host can network to your data source.
  * `nc -z $data_source_host $data_source_port`
*   Check that you can use the bastion host from your personal machine. You will need to use _your own_ private and public keys, not the public key from the above step. Replace the values where appropriate.

    ```
    ssh -L localhost:1111:<POSTGRES_URL_OR_IP>:5432 -i <PRIVATE_KEY_NAME>.pem <BASTION_USER>@<BASTION_IP> psql -h localhost -P 1111 -U secodapostgres
    ```
