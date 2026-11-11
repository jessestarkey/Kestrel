## Design Intent
Intrusion prevention runs on both hubs, blocking at the DMZ's inbound paths, the circuit, and the ground segment conduit. East-west rules between spokes start in alert mode and move to blocking as the Security Team tunes them. Rule sets cover the exposure KESTREL actually has, namely web applications, the partner API, identity services, and the protocols crossing the conduit.

## External Dependencies
The CSSP, which supplies signatures and indicators drawn from its threat intelligence.
