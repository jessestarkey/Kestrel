## Design Intent
The data center runs its own time servers, disciplined by GNSS and checked against DoD's authoritative time service. Every data center host, network device, and ground segment device syncs to them. Cloud workloads use the provider's time service, and drift between the two sides is monitored. Timestamps everywhere are UTC in one format, and drift alerts the Platform Team.

## External Dependencies
The IL5 cloud provider's time service, and DoD's authoritative time service that the data center's time servers check against.
