## Design Intent
KESTREL receives indicators from the CSSP as STIX over TAXII into the security monitoring platform (F31), each with source, confidence, and expiry. The Security Team's threat intelligence analyst vets each one for quality and relevance before it reaches detection. Outbound, KESTREL shares indicators only through the CSSP, after the ISSM's release determination, and none cross the cross domain solution. DC3's DIB Cybersecurity program covers only the performer's own network and laptops, and its indicators reach KESTREL only after vetting.

## External Dependencies
The CSSP, under its service agreement. DC3's DIB Cybersecurity program, for the performer's own systems.
