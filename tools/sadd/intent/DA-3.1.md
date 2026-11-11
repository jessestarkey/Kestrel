## Design Intent
KESTREL uses only FIPS 140-3 validated modules, with Level 3 for the HSMs and the datalink crypto modules that protect CCSD row 13's key material. The KMP lists the approved algorithms, key lengths, and protocols. Scans of code, configuration, and traffic flag non-compliant use. KESTREL holds no classified data, so NSA-approved cryptography applies only within the cross domain solution, which its provider operates.

## External Dependencies
The aircraft and datalink manufacturers, who supply the datalink crypto modules.
