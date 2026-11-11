## Design Intent
Hold every non-person secret in its own spoke's secrets vault and rotate it automatically, so no vault holds another team's secrets. CCSD row 13's datalink and root signing keys stay in the HSMs instead, since their High confidentiality calls for hardware protection a software vault does not give.

## External Dependencies
None outside the boundary.
