## Design Intent
Every training run reads an immutable dataset snapshot in the ML training zone, identified by its content hash. Each snapshot's provenance record names the zones it came from, the release approvals behind it, and the payload vendor terms it falls under. A model can therefore be traced to the exact data and permissions that produced it.

## External Dependencies
None outside the boundary.
