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
3. Configure the information as follows, and choose **Create Peering Connection** when you are done:
   * **Peering connection name tag**: You can optionally name your VPC peering connection. Doing so creates a tag with a key of `Name` and a value that you specify. This tag is only visible to you; the owner of the peer VPC can create their own tags for the VPC peering connection.
   * **VPC (Requester)**: Select the VPC in your account with which to create the VPC peering connection.
   * **Account**: Choose **Another account**.
   * **Account ID**: Enter 482836992928.
   * **Region**: Choose **Another region**, if you're VPC is not in **us-east-1**.
   * **VPC (Accepter)**: Enter vpc-0d8e3f390c5aee744.
4. In the confirmation dialog box, choose **OK**.

After sending the VPC Peering request you will need to accept incoming connections on the  appropriate ports and machines from these two security groups (prefixed with Secoda' account id) where our integrations connect from:

* (Worker) `482836992928/sg-096e49e8ee5ebd1b6`
* (Service)  `482836992928/sg-0c2d21417310fd28f`&#x20;

You will also need to add Secoda's CIDR (`10.2.0.0/16`) OR the specific private subnets ( `10.2.1.0/24` , `10.2.0.0/24` ) to your Route Table.

