## Design Intent
Each training run gets its own containers on the training cluster's GPU nodes, built from an approved image and isolated from concurrent runs. Each run's scratch storage is destroyed when it ends, and nodes are deallocated or their GPU memory cleared before reuse.

## External Dependencies
None outside the boundary.
