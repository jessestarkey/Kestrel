## Design Intent
Build entitlements as bundles for each user role in the system description, scoped to the team that role belongs to. Analysts get their own mission team's raw collection and detections, and every team gets the shared reports. IT Operations provisions accounts, but the approval comes from the requester's product owner or team lead, so no one approves and provisions the same access. Approving an AI agent's actions is an entitlement in the bundle of the role that approves them, so each approval can be reviewed rather than reached by anyone. Today that is the operator bundle, which approves the mission-planning agent's drafts.

## External Dependencies
None outside the boundary.
