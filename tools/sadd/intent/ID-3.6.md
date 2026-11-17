## Design Intent
Hold every cloud non-person secret in its own spoke's secrets vault and rotate it automatically, so no vault holds another team's secrets. Data center, alternate site, and fleet secrets are vaulted in the privileged access platform. CCSD row 13's datalink and root signing keys stay in the HSMs and the datalink crypto modules, since their High confidentiality calls for hardware protection.

## External Dependencies
None outside the boundary.
