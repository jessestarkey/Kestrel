## Design Intent
Every person authenticates with a CAC, an ECA certificate, or a partner PKI certificate. Apart from built-in accounts the privileged access platform vaults and injects, the only passwords are the break-glass accounts under Emergency Access (`ID-4.6`). Stations always check the CAC locally against a cached revocation list, so they keep working when the conduit is down. At a station whose aircraft is airborne, failed logons delay the next prompt and alert rather than lock the account, a parameter the AMP records.

## External Dependencies
DoD PKI and External Certificate Authorities for the certificates themselves.
