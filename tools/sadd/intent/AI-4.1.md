## Design Intent
Each training run gets its own containers on the training cluster's GPU nodes, built from an approved image and isolated from concurrent runs. Each run's scratch storage is destroyed when the run ends.

## External Dependencies
None outside the boundary.
