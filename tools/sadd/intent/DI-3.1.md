## Design Intent
DISA STIGs and SRGs are the hardening basis, with the Cloud Computing SRG's IL5 requirements for the cloud. The landing zone defines the hub and ten spokes as subscriptions under one tenant, each with its own guardrail policies. The Platform Team's infrastructure as code modules encode that design, so a new spoke is built the same way as the existing ten. Both hubs, the access proxy, the VDI brokers, and the cross domain transfer gateway fail closed.

## External Dependencies
The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization.
