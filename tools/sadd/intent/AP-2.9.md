## Design Intent
Every user-facing application serves all of its own client code from KESTREL, with no third-party scripts, fonts, or analytics. Content security policies block anything else. No application calls an external runtime service other than those the cloud provider hosts inside the boundary, and any proposal to add one goes through intake.

## External Dependencies
None outside the boundary.
