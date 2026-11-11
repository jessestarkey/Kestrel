## Design Intent
EDR sensors run in blocking mode on every agentable host and report to the security monitoring platform, which forwards their telemetry to the CSSP. Hosts that run payload vendor software start in audit mode until the vendor software is profiled. File integrity monitoring covers the identity provider, PKI, privileged access platform, and privileged access workstations. Boot integrity attestation covers the privileged access workstations and data center servers, with trusted launch for cloud virtual machines. The SDN controller reports any device it does not know.

## External Dependencies
The CSSP, which supplies threat intelligence indicators and joins the Security Team's threat hunts.
