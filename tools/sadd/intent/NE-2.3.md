## Design Intent
Every platform service has its resource firewall on, such as the spoke vaults, the database services, the feedback endpoints' queues, and each foundation model deployment. Each admits only its own spoke's private endpoint and the workloads that need it. No KESTREL platform service is reachable over a public address, so no public allow-list exists.

## External Dependencies
The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization.
