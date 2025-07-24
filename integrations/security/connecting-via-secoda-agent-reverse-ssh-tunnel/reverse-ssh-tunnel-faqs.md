---
hidden: true
---

# Reverse SSH Tunnel FAQs

**Q: What protections or filtering does Secoda have in place on its end to limit or filter network traffic through the reverse SSH tunnel?**\
Secoda uses dedicated SSH port paired to the provided private RSA or ECDSA key. We delete our copy of the private key immediately after it is generated. All other inbound traffic is blocked. The tunneling server is strictly configured to only allow reverse SSH tunnel sessions on the designated listening ports.

**Q: Are there IP, port, or traffic restrictions for the tunnel?**\
Yes, the tunnel requires private/public key authentication. Only authenticated connections using the assigned key pair are allowed.

**Q: Is the tunnel always on, or is it only established when data is being communicated?**\
The tunnel is a reverse tunnel—our server is always listening for your connection. Your team can control when to start the SSH agent on your end. While the agent doesn’t need to run continuously, it should be active during scheduled metadata extraction runs.

**Q: Do you have any recommendations for VM sizing or specs for the reverse SSH VM?**\
For Linux-based VMs, we recommend at least 1GB RAM and >0.5 vCPU.\
For Windows-based VMs, we recommend 4GB RAM and >2 vCPUs.
