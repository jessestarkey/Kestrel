## Design Intent
The security monitoring platform runs on premises, with a forwarding tier at the alternate site so collection continues if the data center is lost. It receives every source class the logging outcomes produce. Its automation is limited to enrichment, ticketing, notification, and isolating non-production hosts, under Automated Containment and Isolation Procedures (`RS-3.2`) and the IRP. Dashboards serve the Security Team and the CSSP. AI-assisted triage summarizes alerts through the foundation model over F32, cites the records it draws on, and takes no action. The Security Team owns that use case, and it passes AI Cyber T&E before going live.

## External Dependencies
The CSSP, which receives forwarded telemetry and adds its own detection under its service agreement. The IL5 cloud provider hosts the foundation model the triage assistant uses.
