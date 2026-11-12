## Design Intent
The DMZ holds no cloud provider public addresses. Its DoD-registered addresses are reached only through DISA's internet access points and the Boundary Cloud Access Point, which absorb network-layer floods upstream. The DMZ's edge services add request-rate limits for every user-facing application. The cloud hub rate-limits each spoke, so a runaway workload cannot flood the hub or ML Prod's endpoints. DDoS alerts go to the security monitoring platform.

## External Dependencies
The Boundary Cloud Access Point, which absorbs network-layer floods before they reach KESTREL. The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization, supplies the edge services' rate limiting.
