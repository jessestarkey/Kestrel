## Design Intent
Cloud configuration checks watch the portal database and every cloud storage service for public access, disabled logging, or a loosened resource firewall. On premises, each data lake zone's access policy is compared against its baseline, so access that crosses the vendor split is caught. Findings feed a storage compliance dashboard.

## External Dependencies
None outside the boundary.
