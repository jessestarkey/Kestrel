The nShield HSMs in the data center will generate and hold KESTREL's most consequential keys: the root certificate authority, the fleet signing key, and the datalink key material. Their backups reach the standby HSM at the alternate site over F19, only as blobs wrapped under the HSMs' security world, which are useless outside an HSM.

Outside the HSMs, these keys exist only inside a datalink crypto module or a key loader in transit, and each loader is zeroized after every fill. HSM administration needs two people, and every HSM operation is logged to Splunk.
