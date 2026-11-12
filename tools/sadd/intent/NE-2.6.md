## Design Intent
The WAF in the DMZ's edge services fronts every user-facing application in blocking mode, with managed rules plus custom rules for each application. Today those are the identity-aware access proxy, the analyst portal, the signals workbench, and the partner API. Every partner-facing API is checked against its published schema and rate-limited per partner. Nothing on premises faces users directly, so no on-premises reverse-proxy WAF is needed.

## External Dependencies
The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization. The provider supplies the WAF service.
