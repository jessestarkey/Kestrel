## Design Intent
Training repositories are covered by the same four-point secret scanning as application repositories. Training jobs also have no reason to hold a static secret, since they authenticate with workload identity.

## External Dependencies
None outside the boundary.
