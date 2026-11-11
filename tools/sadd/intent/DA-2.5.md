## Design Intent
KESTREL owns and controls the keys for every store holding mission data, models, or backups. Those keys come from the HSM-backed key management service under keys rooted in the on-premises HSMs. Platform-managed keys are allowed only for dev/test data that is synthetic or sanitized. The KMP maps each data class to its key ownership tier.

## External Dependencies
The IL5 cloud provider, whose HSM-backed key management service holds the cloud keys under its provisional authorization.
