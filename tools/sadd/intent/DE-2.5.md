## Design Intent
Log agents and EDR run on every server, physical or virtual, every privileged access workstation, and every VDI desktop. They collect Windows security events, including process creation with command line, and Linux system and audit logs, under the audit policy the hardening baseline sets. They report agent health so a silenced agent is noticed.

## External Dependencies
KESTREL's Microsoft 365 DoD tenant, which supplies the endpoint protection service under its IL5 authorization.
