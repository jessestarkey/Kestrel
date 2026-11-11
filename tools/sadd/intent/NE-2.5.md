## Design Intent
The cloud provider's network-layer DDoS protection covers the DMZ's public addresses, which sit behind the Boundary Cloud Access Point. The DMZ's edge services add request-rate limits for every user-facing application. The cloud hub rate-limits each spoke, so a runaway workload cannot flood the hub or ML Prod's endpoints. DDoS alerts go to the security monitoring platform.

## External Dependencies
The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization. The Boundary Cloud Access Point also filters upstream of KESTREL.
