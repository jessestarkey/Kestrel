## Design Intent
KESTREL validates CACs and partner certificates but does not issue them. The program office sponsors performer CACs through DoD's contractor sponsorship system and requests revocation the day someone leaves. IT Operations resets CAC PINs at dedicated workstations. Every credential's status is checked against DoD PKI and the partner authorities. When a site's conduit is down, it accepts its last revocation list for an AMP-set grace period, and break-glass covers anything longer. The NSS PKI tokens this outcome names belong to the IL6 enclave.

## External Dependencies
DoD PKI and External Certificate Authorities for issuance and revocation of user credentials. The program office's contractor CAC sponsorship with DMDC.
