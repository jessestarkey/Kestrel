## Design Intent
Every build emits signed provenance naming its source revision, runner, pipeline definition, and inputs. Admission control and Certification to Field both verify it. KESTREL commits to SLSA Build Level 3, which the in-cloud ephemeral runners make reachable, and records any shortfall as a dated gap.

## External Dependencies
None outside the boundary.
