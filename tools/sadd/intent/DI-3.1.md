## Design Intent
DISA STIGs and SRGs are the hardening basis, with the Cloud Computing SRG's IL5 requirements for the cloud. The landing zone defines the hub and ten spokes as subscriptions under one tenant, each with its own guardrail policies. The Platform Team's modules encode that design, so a new spoke is built the same way. Every firewall, the access proxy, the VDI brokers, and the cross domain transfer gateway fail closed and preserve their state for recovery.

## External Dependencies
The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization. DISA, which publishes the STIG and SRG content.
