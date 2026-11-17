## Design Intent
The pipeline signs every image and release package with HSM-backed keys, a release key kept separate from the dev/test key, under the KMP. Admission control in every prod spoke admits only images carrying the release signature and a Certification to Field attestation, which protects CCSD row 10's High integrity. Edge model packages are counter-signed for the fleet under Offline/Air-Gapped Model Integrity Verification (`AI-8.13`).

## External Dependencies
None outside the boundary.
