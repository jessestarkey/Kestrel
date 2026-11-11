## Design Intent
The deployment inventory reads the versions actually running in every prod spoke and the edge model versions each aircraft reports at connection. It compares them with what Certification to Field approved, so anything running that was never certified is flagged.

## External Dependencies
None outside the boundary.
