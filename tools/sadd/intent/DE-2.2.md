## Design Intent
Data-plane audit logs are on for every cloud database, storage service, vault, queue, and data lake zone. Every read of a vault secret and every data lake access is logged with the identity that made it. The pipeline turns these logs on when it creates a resource, and a policy-as-code check flags any instance that later loses them, on premises too. The log platform's own reads, deletes, and retention changes are logged and forwarded to the CSSP's copy.

## External Dependencies
None outside the boundary.
