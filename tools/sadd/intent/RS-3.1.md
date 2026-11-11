## Design Intent
Playbooks in the security monitoring platform run the program's decided responses as code and update the service desk record at each step. Actions that disrupt production need a Security Team approval inside the playbook. Fully automatic actions are limited to what Endpoint Response allows, namely isolating a host outside production. The CSSP may run the containment playbooks from its host pool, and each run pages the Security Team's on-call at once. The Security Team reviews or reverses each run by the next business day.

## External Dependencies
The CSSP, whose containment role its service agreement defines.
