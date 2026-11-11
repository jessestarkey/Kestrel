## Design Intent
Each spoke's private zone holds its internal names, and the private endpoint zones resolve every managed service to its endpoint. Each side's resolvers forward the other side's names across the circuit, so a circuit outage leaves local resolution working. The ground segment resolves only its own names and the IT/OT DMZ through a resolver in the data center.

## External Dependencies
The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization.
