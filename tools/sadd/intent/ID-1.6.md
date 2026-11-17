## Design Intent
KESTREL admits one SaaS service to its identities, its Microsoft 365 DoD tenant, through intake and with administrator consent. User consent is blocked at the tenant, so only an administrator can grant an application access, and only through intake. A foundation model the cloud provider hosts inside KESTREL's tenant receives no delegated user access, so it is not a third-party application. KESTREL has almost no general egress, so discovery watches the egress allow-list for any other service.

## External Dependencies
KESTREL's Microsoft 365 DoD tenant, admitted under its IL5 authorization.
