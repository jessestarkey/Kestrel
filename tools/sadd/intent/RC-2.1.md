## Design Intent
Backup administration belongs to a small set of named operators in the Platform Team, separate from the administrators of the systems they protect. Deleting backups, shortening retention, or changing a policy needs a second approver. On premises that approval runs through the privileged access platform. In the cloud, the backup vault's own multi-user authorization enforces it, with its guard held by the Tier 0 administrators. The Security Team audits every such action.

## External Dependencies
None outside the boundary.
