## Design Intent
Both sides' resolvers block known-malicious, newly registered, and algorithmically generated domains using a threat feed. Query logs go to the security monitoring platform, where analytics look for tunneling, beaconing, and exfiltration. Records are reconciled weekly against the asset inventory, so a record pointing at a removed resource is caught before someone else can claim the address.

## External Dependencies
The CSSP and the cloud provider, which supply the threat feeds the resolvers use.
