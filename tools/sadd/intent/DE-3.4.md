## Design Intent
The data center runs its own time servers, disciplined by GNSS and checked against DoD's authoritative time service, with a secondary source at the alternate site. Every on-premises host and network device syncs to them. Ground segment devices fall back to each operating site's holdover reference when the conduit is down. Offsets for controllers that cannot be disciplined are recorded at ingest. Cloud workloads use the provider's time service, and drift between the sides is monitored. Timestamps everywhere are UTC in one format, and drift alerts the Platform Team.

## External Dependencies
The IL5 cloud provider's time service, and DoD's authoritative time service that the data center's time servers check against.
