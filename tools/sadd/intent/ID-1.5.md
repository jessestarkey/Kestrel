## Design Intent
Keep the root certificate authority offline and off the domain. Its key sits in an HSM and is used only in two-person ceremonies to sign issuing authorities and revocation lists. Harden the directory, its domain controllers, the issuing authorities, and the directory sync servers as Tier 0, at the data center and at the alternate site's standby. Directory synchronization to the cloud runs only over the dedicated circuit.

## External Dependencies
None outside the boundary.
