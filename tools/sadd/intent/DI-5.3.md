## Design Intent
Exploit protection, tamper protection, and default-deny host firewalls apply to every privileged access workstation, VDI desktop, and virtual machine. Virtualization-based security isolates the EDR agent and credential stores on every workstation, desktop, and Windows server. The Tier 0 administrators own the tamper protection policy, and the Security Team must approve any change to it. A Platform Team administrator therefore cannot switch off the agent watching their own activity.

## External Dependencies
KESTREL's Microsoft 365 DoD tenant, which supplies the endpoint protection service under its IL5 authorization.
