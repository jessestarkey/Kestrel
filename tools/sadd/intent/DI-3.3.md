## Design Intent
Every cloud database and storage service disables public access, accepts connections only from private endpoints in its own spoke, and sends access logs to the security monitoring platform. On premises, each data lake zone's access policy admits only its own team's workloads, the Data Team, and the ML training zone where F18 allows. The backup repository is reachable only from the backup service.

## External Dependencies
None outside the boundary.
