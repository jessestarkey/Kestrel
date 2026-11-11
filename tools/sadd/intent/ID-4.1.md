## Design Intent
Define privileged roles for each administrative surface, namely the cloud hub, each spoke, the cluster control planes, the data center, the PKI and HSMs, and the ground segment. A team's administrators can administer only that team's spokes, and Tier 0 roles go only to the Platform Team's named Tier 0 administrators. The Security Team and the CSSP get read and audit roles, never the administrative roles they check. No single role spans the HSMs and the cloud tenants, and the cloud tenant-owner roles are separate from day-to-day cloud administration so they can be held to the privileged access workstations.

## External Dependencies
None outside the boundary.
