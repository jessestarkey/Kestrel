## Design Intent
Every AI agent tool call is checked against the tools and parameters its task authorized before it runs, and each tool runs in its own isolated container. The coding agent's commands and file actions pass the same kind of check inside its session sandbox. The mission-planning agent reads shared reports and collection requests, never either team's raw collection. Its tools write drafts only to the planning queue in Mission Team 2 Prod, where an operator approves them. Plans are also checked against approved areas and airspace. Every call passes through that check, and an agent has no other route to a tool. A call the check cannot decide is denied. Each tool's response is checked against its schema before it reaches the model.

## External Dependencies
None outside the boundary.
