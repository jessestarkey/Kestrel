## Design Intent
One backup policy per tier sets schedule, retention, and immutability, and the pipeline binds it to each resource from its criticality tag. A resource without a tier tag cannot be deployed, so no resource is created without backup.

## External Dependencies
None outside the boundary.
