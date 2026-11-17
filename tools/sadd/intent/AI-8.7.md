## Design Intent
Every AI agent tool call is checked against the tools and parameters its task authorized before it runs, and each tool runs in its own isolated container. The mission-planning agent reads shared reports and collection requests, never either team's raw collection. Its tools write drafts only to the planning queue in Mission Team 2 Prod, where an operator approves them. Plans are also checked against approved areas and airspace.

## External Dependencies
None outside the boundary.
