## Design Intent
Register every AI agent as its own identity, scoped to the data and tools its approved use case needs. No agent identity can reach a tool that tasks an aircraft or changes a system without a named human role approving the action first. The mission-planning agent is the first. It calls no tool server outside the boundary, acts on behalf of the requesting user, and its sessions end at a fixed limit.

## External Dependencies
None outside the boundary.
