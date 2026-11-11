## Design Intent
Data-plane audit logs are on for every cloud database, storage service, vault, queue, and the data lake zones. Every read of a vault secret and every data lake access is logged with the identity that made it. The pipeline turns these logs on when it creates a resource, so no data service starts without them.

## External Dependencies
None outside the boundary.
