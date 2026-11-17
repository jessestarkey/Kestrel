## Design Intent
Control-plane activity logs from every subscription and the tenant flow to the security monitoring platform. So do the identity provider's authentication and directory change logs, and the on-premises management planes, namely the SDN controller, hypervisors, BMCs, and the privileged access platform. A policy-as-code check evaluates every source continuously and flags any without its required logging. Identity logs follow the retention DE-3.2 sets. The Security Team reviews the audit and accountability procedures each year.

## External Dependencies
The IL5 cloud provider, whose native detection and logging services KESTREL inherits under its provisional authorization.
