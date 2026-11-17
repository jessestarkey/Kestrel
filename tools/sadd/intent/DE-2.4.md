## Design Intent
First-party applications emit structured security events through a shared logging library, including the authenticated user, each authorization decision, and each data access and release. COTS output is normalized at ingest. Every AI agent logs each tool call with its parameters, its result, and the human approval behind it. API gateways log every request, and the feedback endpoints log every message they accept. Every model endpoint logs its callers and quota decisions.

## External Dependencies
None outside the boundary.
