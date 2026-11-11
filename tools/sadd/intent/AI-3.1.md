## Design Intent
Experimentation workspaces in ML Dev/Test are individual, scoped to the datasets each data scientist is approved for, and reached only through the identity-aware proxy. Downloads are disabled, and the workspaces have no route to any prod spoke. Mission data therefore never reaches a laptop or production.

## External Dependencies
None outside the boundary.
