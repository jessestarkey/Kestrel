## Design Intent
The program PKI issues KESTREL's device, workload, and code-signing certificates from issuing authorities under the HSM-held root, and the PMO ISSE confirms the root's approval under DoDI 8520.02. A certificate management service distributes them. User, partner, and edge server certificates come from DoD PKI and External Certificate Authorities, whose trust anchors the identity provider holds.

## External Dependencies
DoD PKI and External Certificate Authorities, which issue user and partner certificates.
