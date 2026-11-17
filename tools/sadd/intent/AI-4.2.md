## Design Intent
Each training pipeline identity reads only the dataset snapshots its run declares and writes only to its own run's output, which the release runners collect. ML engineers hold no privileged roles on the training cluster. The Platform Team performs privileged operations on their behalf under Just in Time Access (`ID-4.3`), from its admin VDI host pool. That access is reviewed twice a year.

## External Dependencies
None outside the boundary.
