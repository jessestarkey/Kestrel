## Design Intent
Each release carries a versioned runtime baseline covering its workload identity, privileges, filesystem, resource limits, and exposed interfaces. Stage runs the release against that baseline before Certification to Field, so a release that would run differently in production is caught first.

## External Dependencies
None outside the boundary.
