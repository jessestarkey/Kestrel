## Design Intent
The portal database and every cloud storage service disable public access, accept connections only from private endpoints in their own spoke, and send access logs to the security monitoring platform. On premises, each data lake zone's access policy admits only its own team's workloads, the Data Team, and the ML training zone where F18 allows. The backup repository is reachable only from the backup service.

## External Dependencies
None outside the boundary.
