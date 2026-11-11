## Design Intent
Harden the directory, its domain controllers, and the PKI's issuing certificate authorities as Tier 0. The root certificate authority and its keys sit in the HSMs that hold CCSD row 13's key material, so this outcome protects KESTREL's one High confidentiality type directly. Directory synchronization to the cloud runs only over the dedicated circuit.

## External Dependencies
None outside the boundary.
