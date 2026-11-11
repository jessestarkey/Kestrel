## Design Intent
Cloud workloads draw their keys from the cloud provider's HSM-backed key management tier, and production uses only that tier. The on-premises HSMs hold the root keys, the program PKI, code signing, and the datalink key material. One key policy covers both, managed by the Platform Team's Tier 0 administrators.

## External Dependencies
The IL5 cloud provider, whose HSM-backed key management service holds the cloud keys under its provisional authorization.
