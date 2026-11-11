## Design Intent
Every inbound flow reaches KESTREL only through the Boundary Cloud Access Point and then the cloud hub. That includes analysts, partners, performers, and the CSSP. The mission-owner stack behind it is the cloud hub's firewall and intrusion prevention, followed by the DMZ's edge services and WAF. Administration uses its own path through the VDI brokers and the privileged access workstations. KESTREL was registered with the access point's operator before it accepted traffic.

## External Dependencies
The Boundary Cloud Access Point, which DoD operates and which approves KESTREL's connection.
