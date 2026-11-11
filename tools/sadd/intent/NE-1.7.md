## Design Intent
Every wired port in the data center and at the operating sites requires 802.1X, with device certificates from the program PKI. Posture checks gate admission for the privileged access workstations and servers. Ground control stations and launch equipment that cannot run a supplicant are admitted by registered hardware address to their own zone only. A device that fails is quarantined, and the SDN controller alerts the Security Team.

## External Dependencies
None outside the boundary.
