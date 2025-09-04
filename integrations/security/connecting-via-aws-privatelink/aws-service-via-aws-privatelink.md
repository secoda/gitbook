# AWS Service via AWS PrivateLink

[AWS PrivateLink](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-privatelink.html) creates a secure, private connection between services running in AWS. This document describes the steps to set this up between MySQL (RDS) and Secoda.

### Prerequisites

You should already have the following:&#x20;

* Your own non-default VPC configured in AWS.
* A MySQL RDS instance running in AWS, linked to the non-default VPC.
* Private subnets defined within the non-default VPC sufficient for availability.

{% hint style="info" %}
Did you know? You will also need Secoda's AWS account ID later in this process. If you do not already have this, request it now from support.
{% endhint %}

### Setup network to RDS (in AWS)

To setup the private network of your MySQL instance, from within AWS:

1. Copy network settings
2. Navigate to Services, then Database, then RDS.
3. On the left, under Amazon RDS, click on Databases.
4. From the Databases table, click your instance's name under the DB identifier column.
5. Under the Connectivity & security tab, copy the following values:
   * Endpoint and Port values
   * VPC value
   * Subnet group value
6. On the left, click Subnet groups.
7. From the table, click the row whose Name matches the subnet group copied above.
8. From the Subnets table, copy each value under the CIDR block column for private subnets.
9. Create inbound rule
10. To create an inbound rule allowing your private subnet access to your RDS instance:
11. On the left, under Amazon RDS, click on Databases.
12. From the Databases table, click your instance's name under the DB identifier column.
13. Under the Connectivity & security tab, under the Security column and the VPC security groups heading click the link to your security group.
14. At the bottom of the screen, change to the Inbound rules tab and click the Edit inbound rules button.
15. At the bottom of the table, click the Add rule button and create the following rule:
16. For Type use MySQL/Aurora if you are using the default port (3306), or use Custom and enter your port under Port range.
17. For Source use Custom and enter your CIDR range (see Copy network settings).
18. Repeat these sub-steps for each of your CIDR ranges.
19. Below the table, click the Save rules button.

#### (Optional) Create RDS proxy

Before you create an RDS proxy, ensure that the user created in the RDS database is enabled with basic authentication. This method uses a username and password to connect to the RDS database.

To create an RDS proxy for your RDS instance:

1. On the left, under Amazon RDS, click on Proxies.
2. In the upper right of the Proxies table, click the Create proxy button.
3. Under Proxy configuration enter the following details:
   * For Engine family select MySQL.
   * For Proxy identifier enter a meaningful name for your proxy.
4. Under Target group configuration for Database choose your RDS instance.
5. Under Authentication for the Secrets Manager secrets:
   * If you have an existing secret for your RDS instance's database credentials, select it from the drop-down.
   * If not, click the Create a new secret link and enter these details in the new tab:
     1. For Secret type select Credentials for Amazon RDS database.
     2. For Credentials enter the Username and Password of the database user.
     3. Under Database select your RDS instance.
     4. At the bottom of the form, click the Next button.
     5. For Secret name enter a name for the secret.
     6. At the bottom of the form, click the Next button.
     7. Leave the automatic secret rotation off and click the Next button.
     8. Review the secret definition and click the Store button.
     9. Return to the tab where you started creating the RDS proxy.
6. Under Authentication for IAM authentication:
   * If IAM authentication is set to Required, Secoda will use an IAM role to connect to the RDS proxy.
   * If IAM authentication is set to Not Allowed, basic authentication will be enabled. Secoda will use a username and password to connect to the RDS proxy.
7. Under Connectivity expand the Additional connectivity configuration:
   * For VPC security group select Choose existing.
   * For Existing VPC security groups select the security group you edited with the inbound rules above.
8. At the bottom right of the form, click the Create proxy button.
9. From the Proxies table, click the link for the proxy you just created.
10. Under Proxy endpoints section, copy the hostname in the Endpoint column.

### Create internal Network Load Balancer

1. Retrieve IP address of the RDS
2.  Run the following command:

    ```bash
    nslookup <endpoint>
    ```

    * Replace `<endpoint>` with the fully-qualified endpoint hostname copied from the RDS endpoint or RDS proxy created above.
    * Copy the IP address that comes back from the command, under Non-authoritative answer and to the right of Address.
    * **Note**: If this command does not work, try executing it from an EC2 instance in the same VPC as the RDS instance.

### Start creating a Network Load Balancer (NLB)

To create an NLB, from within AWS:

1. Navigate to Services, then Compute, then EC2.
2. On the left, under Load Balancing, click on Load Balancers.
3. At the top of the screen, click the Create Load Balancer button.
4. Under the Network Load Balancer option, click the Create button.
5. Enter the following Basic configuration settings for the load balancer:
   * For Load balancer name enter a unique name.
   * For Scheme select Internal.
   * For IP address type select IPv4.
6. Enter the following Network mapping settings for the load balancer:
   * For VPC select the VPC where the RDS instance is located (see Copy network settings).
   * For Mappings select the availability zones with private subnets.
7. Enter the following Listeners and routing settings for the load balancer:
   * For Port enter 3306 (or the non-default port value from Copy network settings).
   * For Default action click the Create target group link. This will open the target group creation in a new browser tab.

### Create target group

To create a target group for the NLB:

1. Enter the following Basic configuration settings for the target group:
   * For Choose target type select IP addresses.
   * For Target group name enter a name.
   * For Port enter 3306 (or the non-default port value from Copy network settings).
   * For IP address type select IPv4.
   * For VPC select the VPC where the RDS instance is located (see Copy network settings).
   * At the bottom of the form, click the Next button.
2. Enter the following IP addresses settings for the target group:
   * For Network select the VPC where the RDS instance is located (see Copy network settings).
   * For IPv4 address enter the IP address returned by the nslookup command (see Retrieve IP address of the RDS).
   * For Ports enter 3306 (or the non-default port value from Copy network settings).
   * At the bottom of the IP addresses section, click the Include as pending below button.
3. Confirm the following Review targets settings for the target group:
   * Confirm IP address matches the IP address returned by the nslookup command.
   * Confirm Port is 3306 (or the non-default port value used by your RDS instance).
4. At the bottom of the form, click the Create target group button.

### Finish creating NLB

Return to the browser tab where you started the NLB creation, and continue:

1. Under Listeners and routing, click the refresh arrow to the far right of the Default action drop-down box.
2. Select the target group you created above in the Default action drop-down.
3. At the bottom of the form click the Create load balancer button.
4. In the resulting screen, click the View load balancer button.

### Verify target group is healthy

To verify the target group is healthy:

1. From the EC2 menu on the left, under Load Balancing click Target Groups.
2. From the Target groups table, click the link to the target group you created above.
3. At the bottom of the screen, under the Details tab, check that there is a 1 under both Total targets and Healthy.

### Create endpoint service

To create an endpoint service, from within AWS:

1. Navigate to Services, then Networking & Content Delivery, then VPC.
2. From the menu on the left, under Virtual private cloud click Endpoint services.
3. At the top of the page, click the Create endpoint service button.
4. Enter the following Endpoint service settings:
   * For Name enter a meaningful name.
   * For Load balancer type choose Network.
5. For Available load balancers select the load balancer you created above in Create internal Network Load Balancer.
6. Enter the following Additional settings:
   * For Require acceptance for endpoint enable Acceptance required.
   * For Supported IP address types enable IPv4.
7. At the bottom of the form, click the Create button.

{% hint style="info" %}
Under the Details of the endpoint service, enter the DNS name of the Secoda VPC endpoint in the following format — vpce--\<hash.>vpce-svc-..vpce.amazonaws.com. This is the hostname you will need to use to connect to the RDS instance from within Secoda.
{% endhint %}

### Allow Secoda Access

To allow Secoda access to the service, from within the endpoint service screen:

1. At the bottom of the screen, change to the Allow principals tab.
2. At the top of the Allow principals table, click the Allow principals button.
3. Under Principals to add and ARN enter the Secoda account ID and specified principal.
4. At the bottom of the form, click the Allow principals button.

### Notify Secoda support

Once all of the above steps are complete, contact Secoda support.

You will need to provide Secoda support:

* The RDS proxy or RDS endpoint DNS — if IAM authentication is enabled on your RDS proxy or RDS database, respectively.

Once this is done, there are additional steps that Secoda then needs to complete:

* Creating a security group.
* Creating an endpoint.

Once the Secoda team has confirmed the configuration is ready, please continue with the remaining steps.

### Accept the consumer connection request

To accept the consumer connection request, from within AWS:

1. Navigate to Services, then Networking & Content Delivery, then VPC.
2. From the menu on the left, under Virtual private cloud click Endpoint services.
3. From the Endpoint services table, select the endpoint service you created in Create endpoint service.
4. At the bottom of the screen, change to the Endpoint connections tab.
   * You should see a row in the Endpoint connections table with a State of Pending acceptance.
   * Select this row, and click the Actions button and then Accept endpoint connection request.
5. Wait for this to complete, it could take about 30 seconds.

The connection is now established. You can now use the DNS name of the Secoda VPC endpoint as the hostname to crawl MySQL in Secoda.

### FAQs

<details>

<summary>Why might I need to disable the default AWS Security Group restriction on PrivateLink connections?</summary>

By default, AWS applies a security restriction to PrivateLink connections through Security Groups. Disabling this restriction can prevent issues when there are overlapping IP address ranges between your VPC and Secoda’s, ensuring the connection works as expected.

</details>
