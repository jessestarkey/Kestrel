## Design Intent
Every vault is reached only through a private endpoint in its own spoke, with public network access disabled and its resource firewall limited to that spoke's workloads.

## External Dependencies
The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization.
