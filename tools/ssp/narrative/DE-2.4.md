From Phase 2, a shared logging library in each team's code will send authorization, data access, and release events to Splunk. API Management logs every request, each model endpoint logs its callers and quota decisions, and the feedback endpoints log every message they accept. COTS output is normalized at ingest.

The agents arrive in Phase 3, and their actions are logged from the start. Semantic Kernel logs each of the mission-planning agent's tool calls with its parameters and approval, and the coding agent's OpenHands event stream goes to Splunk as well.
