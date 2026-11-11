## Design Intent
Every vault has soft delete and purge protection enabled, so a deleted vault or key can be recovered within the retention window and cannot be purged by one person. Vault operations and threat detection alerts go to the security monitoring platform.

## External Dependencies
The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization.
