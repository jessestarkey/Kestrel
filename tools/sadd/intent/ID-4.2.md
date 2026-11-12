## Design Intent
Administer Tier 0, which holds the identity provider, PKI, and HSMs, only from the physical privileged access workstations in the mission data center and at the alternate site. The cloud tenant-owner roles, which can change a tenant's own security and identity settings, are restricted to the same workstations. Other Tier 1 work runs from the Platform Team's host pool in the VDI spoke, reached from performer laptops. The CSSP's analysts get their own host pool. It reads the security monitoring platform and the cloud's native threat protection and runs the pre-approved containment playbooks, but grants no administrative access. Developers hold no privileged roles, so they need neither path.

## External Dependencies
The performer, whose CMMC Level 2 laptops are the origin for Tier 1 sessions. The CSSP, whose analysts use their own host pool under its service agreement.
