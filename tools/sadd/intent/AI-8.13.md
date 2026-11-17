## Design Intent
Every model leaving the cloud for a disconnected destination travels as a signed offline package with its weights, digest, AI-BOM, model card, and certification record. After Certification to Field, each edge package is counter-signed with the fleet key in the data center's HSMs. The station verifies it before loading, and the aircraft verifies it again at load. The transfer gateway verifies packages before IL6 staging.

## External Dependencies
None outside the boundary.
