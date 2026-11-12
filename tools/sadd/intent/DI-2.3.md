## Design Intent
Cloud resources are removed through the same infrastructure as code that created them. Removal revokes their workload identities and deletes their spoke vault secrets and encryption keys. Data center drives are sanitized on site before they leave, and HSMs are zeroized. An aircraft or ground control station leaving service has its keys zeroized and its onboard storage wiped. Orphaned resources are those whose owning team or tag no longer resolves. Refresh planning tracks the payload processing workstation's replacement against its 2027-09-30 deadline, and a slip goes to the AO before the workstation connects.

## External Dependencies
None outside the boundary.
