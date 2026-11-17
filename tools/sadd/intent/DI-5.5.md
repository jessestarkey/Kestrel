## Design Intent
The Security Team takes endpoint response actions under the IRP, namely isolation, file remediation, and live response. It does so under Privileged Access Control (`ID-4.1`)'s EDR responder exception, and live response sessions are recorded. Tier 0 hosts sit in their own device group, where those actions are bound to roles usable only from the privileged access workstations. That group is excluded from CSSP playbooks and automated isolation. Elsewhere the CSSP may isolate a host through a pre-approved playbook, which pages the Security Team. Automated response isolates only non-production hosts, and nothing here acts on fleet equipment.

## External Dependencies
KESTREL's Microsoft 365 DoD tenant, which supplies the endpoint protection service under its IL5 authorization. The CSSP, under the detection and response split in its service agreement.
