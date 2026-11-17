## Design Intent
A merged pull request is the change record for anything defined as code, and the service desk holds the record for everything else. Each change carries a security impact note feeding Security Impact Analysis (SIA) (`GV-5.11`). Cloud changes are tested in the owning team's stage cluster. Tier 0 and data center changes go first to the alternate site's standby or a lab, and a change with neither has a recorded exception and extra verification. A post-change compliance scan closes the record. Changes to the shared rule base, the identity provider, or an interconnection go to the Configuration Control Board. Emergency changes run through the privileged access platform and get a review within two business days.

## External Dependencies
None outside the boundary.
