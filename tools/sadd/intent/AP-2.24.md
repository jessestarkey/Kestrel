## Design Intent
Every build emits signed provenance naming its source revision, runner, pipeline definition, and inputs. Admission control and Certification to Field both verify it. The target is SLSA Build Level 3, which the in-cloud ephemeral runners make reachable.

## External Dependencies
None outside the boundary.
