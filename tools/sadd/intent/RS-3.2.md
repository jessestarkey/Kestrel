## Design Intent
Network containment moves a workload into a quarantine policy at the cloud hub, or into the SDN fabric's quarantine segment in the data center. Identity containment disables the account, revokes its sessions and tokens, and suspends any workload or AI agent identity. Both run from playbooks, and the Security Team approves before either touches production. The CSSP may run them on its own authority when an incident cannot wait for the Security Team. Neither the Security Team's playbooks nor the CSSP's may touch fleet systems.

## External Dependencies
The CSSP, whose containment role its service agreement defines.
