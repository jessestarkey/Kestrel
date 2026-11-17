## Design Intent
The on-premises HSMs generate and hold KESTREL's most consequential keys, namely the root certificate authority, the fleet signing key, and CCSD row 13's datalink key material. A standby HSM at the alternate site holds their backups, which travel over F19 only as blobs wrapped under the HSMs' security world, unusable outside an HSM. These keys never exist in the clear outside an HSM, a datalink crypto module, or a key loader in transit. Loaders are accounted for and zeroized after each fill. HSM administration needs two people, and every HSM operation is logged to the security monitoring platform.

## External Dependencies
The aircraft and datalink manufacturers, who supply the datalink crypto modules.
