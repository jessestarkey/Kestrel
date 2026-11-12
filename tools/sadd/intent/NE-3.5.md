## Design Intent
Both sides' resolvers block known-malicious, newly registered, and algorithmically generated domains using a threat feed. Query logs go to the security monitoring platform, where analytics look for tunneling, beaconing, and exfiltration. Records are checked continuously against the asset inventory, so a record pointing at a removed resource is caught before someone else can claim the address.

## External Dependencies
A commercial threat feed service, pulled by zone transfer with no query data sent back. The CSSP, whose indicators load as a local policy zone.
