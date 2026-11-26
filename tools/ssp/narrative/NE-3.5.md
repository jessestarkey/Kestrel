From Phase 2, Infoblox Threat Defense will block known-malicious, newly registered, and algorithmically generated domains at every resolver. Its feeds arrive as response policy zones, pulled by zone transfer through the hub, and no query data is sent to Infoblox. The CSSP's indicators load as a local response policy zone.

Query logs go to Splunk, where analytics look for tunneling, beaconing, and exfiltration. DNS records are also checked continuously against the asset inventory. A record left pointing at a removed resource is caught before anyone else can claim the address.
