## Design Intent
Each spoke's private zone holds its internal names, and the private endpoint zones resolve every managed service to its endpoint. Every resolver forwards the other sites' names across the circuits, so an outage leaves local resolution working. The alternate site's standby DNS takes over the data center's names if it is lost. Each operating site resolves only its own names and the IT/OT DMZ, through a local resolver pair, so a lost conduit leaves resolution working.

## External Dependencies
The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization.
