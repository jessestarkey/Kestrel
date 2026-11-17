## Design Intent
KESTREL's own endpoints are its privileged access workstations, which a Tier 0 management plane enrolls, scans against a compliance policy, and remediates. A workstation that falls out of compliance loses Tier 0 sign-in until it is fixed. Devices KESTREL does not own never join its network. Performer laptops reach it only through the identity-aware access proxy and the VDI brokers, after a posture check. Parent organization devices use the proxy alone (F38), and vendor devices only the vendor host pool (F37). The interconnection agreement, the performer's CMMC Level 2 attestation, and the CMP record the terms. KESTREL has no mobile devices, and its workstations never travel.

## External Dependencies
The performer and the parent organization, which manage their own devices and attest their compliance under their interconnection agreements.
