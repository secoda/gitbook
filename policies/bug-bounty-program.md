# Bug Bounty Program

At Secoda, we care deeply about the safety and security of our customer’s data. This is why we greatly value any inputs from our community that can help us detect vulnerabilities in our product.

### How to report an issue

If you have discovered an issue that is not part of our out-of-scope vulnerabilities, please send an email to [security@secoda.co](mailto:security@secoda.co) with the following details:

* A summary of the issue and potential impact
* A breakdown of the steps to replicate the issue
* Details of the environment you are using
* If available, any proof-of-concept code to exploit the vulnerability

Upon receiving your email, our team will start investigating the issue. We will keep you updated on the progress and may reach back for further details if needed. Once the issue is resolved we will update our customers.

Of course, we want to compensate your effort, so for any valid vulnerabilities with a [CVSS](https://nvd.nist.gov/vuln-metrics/cvss) score of 4 or higher, we will reach back to you with a financial reward.

### Focus areas

* Authentication bypass and privilege escalation
* Exposure of personally identifiable information (PII)
* Access to data outside of the authenticated workspace
* SQL injection and remote command execution

### In scope

* https://app.secoda.co
* https://eu.secoda.co
* https://apac.secoda.co

### Out-of-scope

* Automated scanning of any kind
* Social engineering of any kind, in particular Secoda employees
* Denial of Service attacks of any kind
* Attacks requiring physical access to the victim's computer
* Theoretical attacks without proof of exploitability
* Man-in-the-middle attacks
* Clickjacking on pages with no sensitive actions
* High-privilege users (admins, owners) using a bug to sabotage/deface their own workspace
* Logic bugs which allow an attacker to bypass limits on free accounts and get access to features on paid plans.
* Missing best practices in CSP, email DNS records or cookies may be considered informative but are unlikely to qualify for any reward.

### We kindly ask you

* Only test the vulnerability on your own account or with explicit permission from the account holder.
* Make a good faith effort to avoid privacy violations, copying or destruction of data, and interruption or degradation of our service.
* If you obtain remote access to our systems, do not attempt to expand or elevate access to other servers.
* To prevent further exploitation, please do not make the vulnerability public before reporting it to us, and give us adequate time to address the issue.

### Safe harbor

Any activities conducted in a manner consistent with this policy will be considered authorized conduct and we will not initiate legal action against you. If legal action is initiated by a third party against you in connection with activities conducted under this policy, we will take steps to make it known that your actions were conducted in compliance with this policy.
