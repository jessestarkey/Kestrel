## Design Intent
Every port, protocol, and service crossing KESTREL's boundary is registered in the DoD PPSM registry and aligned to its Category Assurance List entry. These include the Boundary Cloud Access Point flows, the outbound service classes, the CSSP feed, the cross domain transfers, and the partner API. The DMZ's internet-facing services are also registered for DISA's internet access points. The approved baseline is a separate CMP record with each entry's justification and approver. The pipeline compares both the rule base and observed reachability with it on every change, and the Security Team recertifies it each year.

## External Dependencies
DISA's PPSM program, which maintains the registry and the Category Assurance List.
