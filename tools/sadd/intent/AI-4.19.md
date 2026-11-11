## Design Intent
Training jobs authenticate to the dataset snapshots and the model registry with short-lived workload credentials. Any remaining secret comes from ML Dev/Test's vault at run time.

## External Dependencies
None outside the boundary.
