## Design Intent
Every cloud database and storage service disables public access, accepts connections only from private endpoints in its own spoke, and sends access logs to the security monitoring platform. On premises, each data lake zone's access policy admits its own team's workloads, the Data Team, and the ML training zone where F18 allows. It also admits the data catalog's read-only scan identity and the backup service. The object store's array has its exports, legacy protocols, and management interfaces hardened. Self-hosted database and analytics engines drop default accounts and turn on native audit. Each zone's policy is checked against its baseline after every change, so access that crosses the vendor split is caught. The backup repository is reachable only from the backup service.

## External Dependencies
None outside the boundary.
