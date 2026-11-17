## Design Intent
Evaluate each request against identity, device posture, network origin, and risk before granting access. Performer users reach the identity-aware proxy and their VDI pools only from laptops that report as compliant at that moment. Program office staff connect over F38 from the parent organization's managed devices, checked the same way. Partner system calls from outside their nation's expected networks are denied. Identity threat detection feeds the policy engine.

## External Dependencies
The Boundary Cloud Access Point, which supplies the network-origin signal for inbound sessions. The performer's and the parent organization's device management, which supply each device's compliance signal. The IL5 cloud provider's identity service, inherited under its provisional authorization.
