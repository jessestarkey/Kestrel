## Design Intent
KESTREL uses only FIPS 140-3 validated modules, with Level 3 for the HSMs and the datalink crypto modules that protect CCSD row 13's key material. The KMP lists the approved algorithms, key lengths, and protocols. Scans of code, configuration, and traffic flag non-compliant use. As a national security system, KESTREL uses the CNSA algorithms CNSSP 15 requires and follows its CNSA 2.0 transition. KESTREL protects no classified information, so NSA-approved cryptography sits on the IL6 side, owned by the enclave and the cross domain service provider.

## External Dependencies
The aircraft and datalink manufacturers, who supply the datalink crypto modules.
