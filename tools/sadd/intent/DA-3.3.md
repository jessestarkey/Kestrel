## Design Intent
Cloud workloads in every spoke holding mission data, including ML Dev/Test, draw keys only from the cloud provider's HSM-backed tier. That tier also holds the pipeline's release and dev/test signing keys. The on-premises HSMs hold the root keys, the program PKI, the fleet signing key, and the datalink key material, with the alternate site's HSM as standby. One key policy covers both, managed by the Tier 0 administrators.

## External Dependencies
The IL5 cloud provider, whose HSM-backed key management service holds the cloud keys under its provisional authorization.
