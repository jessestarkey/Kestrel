## Design Intent
Control-plane activity logs from every subscription and the tenant, together with the identity provider's authentication and directory change logs, flow to the security monitoring platform. Configuration checks alert when a source stops sending. Identity logs are kept longer than the default, as the log retention strategy sets.

## External Dependencies
The IL5 cloud provider, whose native detection and logging services KESTREL inherits under its provisional authorization.
