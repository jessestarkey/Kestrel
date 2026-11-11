## Design Intent
Every application emits structured security events in a common format, including the authenticated user, each authorization decision, and each data access and release. Every AI agent also logs each tool call with its parameters, its result, and the human approval behind it. Every model endpoint logs its callers and quota decisions.

## External Dependencies
None outside the boundary.
