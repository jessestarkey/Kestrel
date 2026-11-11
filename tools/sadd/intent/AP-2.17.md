## Design Intent
Every workload ships with a deny-by-default network policy that permits only the flows its team mapped. The pipeline checks that policy against the approved flow map before admission, so a workload with a missing or loosened policy is refused.

## External Dependencies
None outside the boundary.
