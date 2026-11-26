Cosign will sign every release image and package in the pipeline, using a Key Vault Premium key backed by the HSMs. A separate key signs dev/test artifacts. Ratify and Gatekeeper admit to production only images that carry the release signature and a Certification to Field attestation. Vendor images are signed again once the mirror has scanned them.

The fleet signing key never leaves the nShield HSMs in the data center. Before it signs anything for the fleet, the signing host checks the cloud signature, the build provenance, and the Certification to Field approval.
