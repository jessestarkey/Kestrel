## Design Intent
Every asset carries required tags for its owning team, spoke or data center segment, environment, data classification, mission criticality, and end-of-support date. Assets tied to a payload vendor's data rights also carry that vendor's tag, which lets the vendor split be checked from the inventory. The pipeline's policy-as-code checks reject untagged cloud resources at deployment, and Fleet Operations tags fleet equipment when it is received.

## External Dependencies
None outside the boundary.
