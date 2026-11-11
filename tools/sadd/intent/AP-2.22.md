## Design Intent
Each team's pipeline identity reaches only its own repositories, its own registry namespace, and its own dev/test spoke. Only the release identity can deploy to a prod spoke, the IL6 transfer gateway, or the edge release path, and it acts only after Certification to Field approves the release.

## External Dependencies
None outside the boundary.
