## Design Intent
The security monitoring platform runs on premises and receives every source class the logging outcomes produce. Its correlation rules come from the Security Team's rule repository, and its response automation is limited to what Endpoint Response allows. Dashboards serve the Security Team and the CSSP. AI-assisted triage summarizes alerts through a CSP-hosted foundation model, but it only advises and takes no action.

## External Dependencies
The CSSP, which receives forwarded telemetry and adds its own detection under its service agreement. The IL5 cloud provider hosts the foundation model the triage assistant uses.
