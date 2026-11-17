## Design Intent
The CSSP's service agreement divides the work. The CSSP monitors around the clock, triages, and supplies threat intelligence, and its advisories land on incident records automatically. The CSSP runs the pre-approved containment playbooks when an incident cannot wait for the Security Team. The Security Team directs every other response action, which the owning team carries out or the Security Team runs through an approved playbook under Privileged Access Control (`ID-4.1`). The security monitoring platform forwards all telemetry to the CSSP, and a stalled feed alerts. The ISSM receives the CSSP's directives and tracks each one to completion.

## External Dependencies
The CSSP, under the detection and response split in its service agreement.
