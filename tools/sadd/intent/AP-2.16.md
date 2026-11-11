## Design Intent
The pipeline checks every image and its runtime configuration against the container hardening benchmark before it ships. The checks require a non-root user, a read-only filesystem, dropped capabilities, and resource limits. A failing image cannot reach the registry's release namespace.

## External Dependencies
None outside the boundary.
