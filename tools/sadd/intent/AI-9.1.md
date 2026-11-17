## Design Intent
Each fielded model's output distribution and confidence are tracked, along with its accuracy against analyst corrections as they return. The person-detection model's misses are tracked through the zones' sanitizing pipelines. Drift past the model card's limits alerts the ML Team and the owning mission team, and opens a retraining cycle.

## External Dependencies
None outside the boundary.
