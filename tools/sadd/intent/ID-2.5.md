## Design Intent
Evaluate each request against identity, device posture, network origin, and risk before granting access. Performer users reach the identity-aware proxy and the admin VDI pool only from laptops that report as compliant at that moment. Partner sessions that arrive from outside their nation's expected networks are stepped up or denied. Identity threat detection feeds the policy engine. The physical-logical correlation raises alerts in the security monitoring platform instead, since stations check sign-ins locally.

## External Dependencies
The Boundary Cloud Access Point, which supplies the network-origin signal for inbound sessions. The performer's device management, which supplies each laptop's compliance signal.
