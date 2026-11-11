## Design Intent
The digest of every member of a release bundle is recorded when the bundle is assembled. Each digest is checked again at deployment to a prod spoke, at staging for the IL6 transfer, and at loading on a ground control station. A bundle that fails any check is stopped and reported to the Security Team.

## External Dependencies
None outside the boundary.
