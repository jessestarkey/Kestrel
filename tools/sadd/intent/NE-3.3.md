## Design Intent
The cloud DNS resolvers and the data center DNS are KESTREL's only recursive resolvers, and hosts are allowed no other. Outbound queries are filtered by policy, and the resolvers validate DNSSEC. KESTREL's public names, one for each user-facing application, are hosted in the cloud provider's DNS service and signed. Resolver traffic across the circuit stays inside its encryption.

## External Dependencies
The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization. The provider hosts KESTREL's public zone.
