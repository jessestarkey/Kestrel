## Design Intent
KESTREL owns and controls the keys for every store holding mission data, models, or backups. Cloud keys come from the HSM-backed key management tier under keys rooted in the on-premises HSMs, and on-premises stores draw their keys from the HSMs directly. Platform-managed keys are allowed only for synthetic or sanitized dev/test data, never in ML Dev/Test. The KMP maps each data class to its key ownership tier.

## External Dependencies
The IL5 cloud provider, whose HSM-backed key management service holds the cloud keys under its provisional authorization.
