## Design Intent
Intrusion prevention runs on every firewall, blocking at the DMZ's inbound paths, the circuits, and each operating site's conduit. On premises, sensors fed by the SDN fabric's mirrored traffic add detection behind the hub. East-west rules between spokes start in alert mode and move to blocking as the Security Team tunes them. Rule sets cover the exposure KESTREL actually has, namely web applications, the partner API, identity services, and the protocols crossing the conduits.

## External Dependencies
The CSSP, which supplies signatures and indicators drawn from its threat intelligence.
