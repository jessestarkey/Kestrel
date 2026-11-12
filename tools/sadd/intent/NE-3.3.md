## Design Intent
KESTREL's own resolvers in the cloud, the data center, the alternate site, and each operating site are the only ones hosts may use. Outbound queries are filtered by policy, and the resolvers validate DNSSEC. KESTREL's public names, one for each user-facing application, are hosted in the cloud provider's DNS service and signed. Resolver traffic across the circuits stays inside their encrypted tunnels.

## External Dependencies
The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization. The provider hosts KESTREL's public zone.
