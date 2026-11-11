## Design Intent
Pipeline jobs authenticate with short-lived credentials bound to their workload identity, and they fetch any remaining secret from their spoke's vault at run time. No long-lived credential is stored in a pipeline variable or repository.

## External Dependencies
None outside the boundary.
