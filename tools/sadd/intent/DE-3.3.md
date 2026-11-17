## Design Intent
Every record is written on arrival to an object-locked store in compliance mode, and each batch is hashed so later alteration is detectable. No role holds the index delete capability. A logging administrator role, held by named Security Team members under ID-4.1's stated exception, owns retention, collection, and content. Platform Team infrastructure administrators get no rights over indexes, retention, or the object lock. Break-glass use alerts. Storage nearing capacity alerts, and a full store halts nothing and buffers at the forwarders. A silent source or an ingestion failure alerts the Security Team and the CSSP.

## External Dependencies
None outside the boundary.
