## Design Intent
The program PKI issues KESTREL's device, workload, and code-signing certificates from issuing authorities under the HSM-held root. A certificate management service distributes them. User and partner certificates come from DoD PKI and External Certificate Authorities, whose trust anchors the identity provider holds.

## External Dependencies
DoD PKI and External Certificate Authorities, which issue user and partner certificates.
