---
description: >-
  This page walks through the Secoda and Connecting via VPC Peering that Secoda
  supports
---

# Connecting via VPC Peering

## **Getting Started with VPC Peering** <a href="#h_3a4bfd6458" id="h_3a4bfd6458"></a>

First, create a Secoda a VPC Peering request following the instructions below&#x20;

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).
2. In the navigation pane, choose **Peering Connections**, **Create Peering Connection**.
3.  Configure the information as follows, and choose **Create Peering Connection** when you are done:

    * **Peering connection name tag**: You can optionally name your VPC peering connection. Doing so creates a tag with a key of `Name` and a value that you specify. This tag is only visible to you; the owner of the peer VPC can create their own tags for the VPC peering connection.
    * **VPC (Requester)**: Select the VPC in your account with which to create the VPC peering connection.
    * **Account**: Choose **Another account**.
    * **Account ID**: Enter 482836992928.
    * **Region**: Choose **Another region**, if you're VPC is not in **us-east-1**.
    * **VPC (Accepter)**: Enter the VPC id. See table below for VPC ids.

    <table><thead><tr><th width="121">Region</th><th width="602">VPC (Accepter)</th></tr></thead><tbody><tr><td>US</td><td>vpc-0d8e3f390c5aee744</td></tr><tr><td>EU</td><td>vpc-01a0b77b5b5616d60</td></tr><tr><td>APAC</td><td>vpc-0c7421c54b3efbc07</td></tr><tr><td>Managed</td><td>Contact us</td></tr></tbody></table>
4. In the confirmation dialog box, choose **OK**.

After sending the VPC Peering request you will need to accept incoming connections on the  appropriate ports and machines from these two security groups (prefixed with Secoda' account id) where our integrations connect from:

<table><thead><tr><th width="120">Region</th><th width="361">Worker (security group)</th><th>Service (security group)</th></tr></thead><tbody><tr><td>US</td><td><code>482836992928/sg-096e49e8ee5ebd1b6</code></td><td><code>482836992928/sg-0c2d21417310fd28f</code></td></tr><tr><td>EU</td><td><code>482836992928/sg-08891448b59100c0b</code></td><td><code>482836992928/sg-0982632f8f27c63d6</code></td></tr><tr><td>APAC</td><td><code>482836992928/sg-07c360aed40c4d922</code></td><td><code>482836992928/sg-04f8c2b04d92f5bc4</code></td></tr><tr><td>Managed</td><td>Contact us</td><td>Contact us</td></tr></tbody></table>

You will also need to add Secoda's CIDR to your Route Table. The VPC (Accepter) and the CIDR's for each region are: &#x20;

<table><thead><tr><th width="121">Region</th><th width="363">VPC (Accepter)</th><th>CIDR</th></tr></thead><tbody><tr><td>US</td><td>vpc-0d8e3f390c5aee744</td><td>10.2.0.0/16</td></tr><tr><td>EU</td><td>vpc-01a0b77b5b5616d60</td><td>10.4.0.0/16</td></tr><tr><td>APAC</td><td>vpc-0c7421c54b3efbc07</td><td>10.5.0.0/16</td></tr><tr><td>Managed</td><td>Contact us</td><td>Contact us</td></tr></tbody></table>

5. Once the connection is setup, you will simply need to add the specific integration following the steps on the [integration page](../).&#x20;
