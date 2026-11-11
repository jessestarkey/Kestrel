## Design Intent
Every AI agent tool call is checked against the tools and parameters its task authorized before it runs, and tools run in a sandboxed container. The mission-planning agent is the first: its tools only read mission data and write drafts to an operator's approval queue. Plans are also checked against approved areas and airspace.

## External Dependencies
None outside the boundary.
