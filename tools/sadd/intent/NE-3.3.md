## Design Intent
KESTREL's own resolvers in the cloud, the data center, the alternate site, and each operating site are the only ones hosts may use. Outbound queries are filtered by policy, and the resolvers validate DNSSEC. KESTREL's public names are delegated under the program's DoD parent zone, signed, and point only at the access point's published addresses, with DoD publishing their delegation records. Resolver traffic across the circuits stays inside their encrypted tunnels.

## External Dependencies
DISA, which operates the DoD parent zone and publishes KESTREL's delegation records.
