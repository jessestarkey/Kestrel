## Design Intent
Cloud resources are removed through the same infrastructure as code that created them, which revokes their workload identities and deletes their vault secrets and keys. On-premises drives are sanitized on site before they leave, and HSMs are zeroized. An aircraft or station leaving service has its keys zeroized, its storage wiped, and its device certificates revoked. Orphaned resources are those whose owning team or tag no longer resolves. Refresh planning forecasts each asset's end of support with enough lead time to replace it, such as the payload processing workstation before 2027-09-30.

## External Dependencies
None outside the boundary.
