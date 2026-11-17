## Design Intent
A certificate inventory and dashboard track every certificate KESTREL issues or trusts, and alerts fire on approaching expiry or on issuance nobody requested. Revocation procedures cover every case. A Tier 0 administrator authorizes each revocation, and the revocation list and status responses publish within an hour. An aircraft declared lost has its device certificates revoked at once, and the datalink keys it shared are always superseded fleet-wide.

## External Dependencies
None outside the boundary.
