## Design Intent
Training scripts, data loaders, and feature-engineering code go through the same SAST in the shared pipeline as application code, with rules for the ML frameworks they use. That includes checks for unsafe deserialization and shell execution.

## External Dependencies
None outside the boundary.
