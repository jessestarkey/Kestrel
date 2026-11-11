## Design Intent
KESTREL admits no third-party OAuth or SaaS application to its identities by default. The foundation model is a service the cloud provider hosts inside KESTREL's tenant, so it receives no delegated user access and is not a third-party application in this outcome's sense. Discovery runs against IL5 production egress to catch any other service in use.

## External Dependencies
None outside the boundary.
