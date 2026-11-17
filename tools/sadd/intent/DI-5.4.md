## Design Intent
Authenticated vulnerability scans cover every host in every location on a continuously updated feed. Scan credentials for Tier 0 hosts are vaulted in the privileged access platform and used only from a Tier 0 scanner. EDR sensors run in blocking mode on every agentable host and report to the Microsoft 365 DoD tenant's endpoint service over F29, whose alerts reach the security monitoring platform and the CSSP. Hosts running payload vendor software start in audit mode until the software is profiled. File integrity monitoring covers Tier 0 and the privileged access platform. Boot integrity attestation covers every physical server and workstation, with trusted launch for cloud virtual machines.

## External Dependencies
KESTREL's Microsoft 365 DoD tenant, which supplies the endpoint protection service under its IL5 authorization. The CSSP, which supplies threat intelligence indicators and joins the Security Team's threat hunts.
