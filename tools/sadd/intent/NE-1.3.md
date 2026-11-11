## Design Intent
Flow telemetry from both hubs and the SDN fabric is checked for cleartext and obsolete protocols, such as Telnet, FTP, SMBv1, unsigned LDAP, and TLS below 1.2. Each one found is disabled. The payload processing workstation's operating system may not negotiate current TLS. If so, its transfer to the data lake is the one registered exception, confined to its single conduit and covered by CCSD tailoring action 3.

## External Dependencies
None outside the boundary.
