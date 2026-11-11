## Design Intent
One policy engine evaluates the pipeline's gates and every cluster's admission decisions. Its rules are version-controlled policy in the Platform Team's repository, changed only by reviewed pull requests. Admission runs in deny mode in every prod spoke and in stage, so stage rejects what production would.

## External Dependencies
None outside the boundary.
