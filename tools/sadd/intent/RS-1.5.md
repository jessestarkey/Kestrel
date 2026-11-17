## Design Intent
A declared incident pages the on-call security analyst through the service desk, and the CSSP's operations center is notified at the same time. Severe incidents also page the ISSM and the affected team's lead. The security monitoring platform hands incidents to the service desk through an event stream, not by email. If the service desk or the circuits are down, the platform pages directly over F29, and pages carry only an incident ID and severity.

## External Dependencies
The CSSP, under the detection and response split in its service agreement. The paging service, reached over F29.
