## Design Intent
The WAF in the DMZ's edge services fronts every user-facing application in blocking mode, with managed rules plus custom rules for each application. Today those are the identity-aware access proxy, the service desk behind it, the analyst portal, the signals workbench, the LLM analyst assistant's front end, and the partner API. API calls are checked against the registered schema and admitted only on routes in the runtime API inventory. Bot management and per-partner rate limits throttle abusive clients. On-premises web consoles are reachable only from the VDI pools and the privileged access workstations, so no on-premises reverse-proxy WAF is needed.

## External Dependencies
The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization. The provider supplies the WAF service.
