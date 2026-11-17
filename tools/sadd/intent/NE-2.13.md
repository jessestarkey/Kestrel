## Design Intent
Every flow to or from outside KESTREL's own sites crosses a named managed interface, as the Cloud Computing SRG requires at IL5 (CCSD Section 6). For the cloud, that is the Boundary Cloud Access Point and then the cloud hub, and the dedicated circuits reach the hub over DISN through the same access point. For the data center, it is the data center hub, for the CSSP feed and its DISN egress. Inbound users, partners, performers, vendors, and the CSSP all arrive this way. IL6 products over F13 arrive instead through the enterprise cross domain solution, then the cloud hub. The mission-owner stack is the hub's firewall and intrusion prevention, then the DMZ's edge services and WAF. The VDI brokers have their own listener and subnet. KESTREL is registered with the access point's operator before it accepts traffic.

## External Dependencies
The Boundary Cloud Access Point and DISA, which approve KESTREL's connection and carry its DISN paths.
