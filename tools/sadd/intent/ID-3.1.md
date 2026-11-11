## Design Intent
Give every IL5 workload the managed Kubernetes service's native workload identity, so services read the data lake zones, the report index, and ML Prod's model endpoints without a stored secret. Each workload's identity is scoped to its own spoke and team. Static credentials found in the cloud spokes are removed once native identity replaces them.

## External Dependencies
The IL5 cloud provider's workload identity mechanism, inherited under its provisional authorization.
