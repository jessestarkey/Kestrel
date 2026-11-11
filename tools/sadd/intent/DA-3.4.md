## Design Intent
The on-premises HSMs generate and hold KESTREL's most consequential keys, namely the root certificate authority, code signing, and CCSD row 13's datalink key material. These keys never exist outside an HSM or a datalink crypto module. HSM administration needs two people, and every HSM operation is logged to the security monitoring platform.

## External Dependencies
The aircraft and datalink manufacturers, who supply the datalink crypto modules.
