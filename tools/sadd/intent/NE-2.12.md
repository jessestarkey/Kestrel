## Design Intent
Every port, protocol, and service crossing KESTREL's boundary is registered in the DoD PPSM registry and aligned to its Category Assurance List entry. These include the Boundary Cloud Access Point flows, the CSSP feed, the cross domain transfers, and the partner API. The approved baseline is the same policy-as-code rule base the hubs run, so the pipeline checks the deployed rules against the registration on every change. The Security Team recertifies the registration each year.

## External Dependencies
DISA's PPSM program, which maintains the registry and the Category Assurance List.
