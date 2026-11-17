## Design Intent
Give every IL5 workload the cloud's native workload or managed identity, so services read the data lake zones, the report index, and ML Prod's model endpoints without a stored secret. The on-premises data lake trusts these federated workload tokens. Pipeline identities are a workload class of their own, scoped by Least-Privilege CI/Build Infrastructure Access (`AP-2.22`). Static credentials found in the cloud spokes are removed once native identity replaces them.

## External Dependencies
The IL5 cloud provider's workload identity mechanism, inherited under its provisional authorization.
