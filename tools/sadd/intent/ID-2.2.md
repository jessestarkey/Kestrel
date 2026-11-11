## Design Intent
KESTREL validates CACs and partner certificates but does not issue them. It issues and revokes only its own device and workload certificates from the program PKI, and it runs the revocation checking every external credential passes. The NSS PKI tokens this outcome names belong to the IL6 enclave, not to KESTREL.

## External Dependencies
DoD PKI and External Certificate Authorities for issuance and revocation of user credentials.
