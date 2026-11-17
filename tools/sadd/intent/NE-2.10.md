## Design Intent
KESTREL uses the enterprise cross domain solution a DoD cross domain service provider operates. That provider owns product selection, accreditation, and the guard's filtering, which KESTREL inherits. The transfer gateway sits alone in a DMZ subnet that reaches only the solution's low side and the feedback endpoints. Low-to-high baselines need Certification to Field approval before the gateway stages them, and the guard releases each approved baseline by verified type. High-to-low products pass the enclave's release review, then KESTREL's malware scan, format and schema validation, and marking check. They reach the feedback endpoints as untrusted input. Both sides' logs go to the security monitoring platform, and manual media transfer is prohibited.

## External Dependencies
The enterprise cross domain service provider, under the interconnection agreement covering both directions. The IL6 enclave's owner, whose release review approves every high-to-low product.
