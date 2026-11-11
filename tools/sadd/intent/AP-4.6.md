## Design Intent
Every prod spoke keeps the previous certified release ready to roll back to. New releases reach a small share of traffic first, and they widen only if security and health signals stay clean. Feature flags are configuration in the repository, so changing one is a reviewed change like any other.

## External Dependencies
None outside the boundary.
