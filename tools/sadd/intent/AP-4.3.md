## Design Intent
Every review, approval, dismissal, and override in the source repository is forwarded to the security monitoring platform, where the Platform Team's administrators cannot change it. Each batch is hashed so an alteration is detectable. Each approval is checked against the approver's entitlement at the time. Identities resolve to the person through the identity provider, and a merge whose approver is also its author is refused.

## External Dependencies
None outside the boundary.
