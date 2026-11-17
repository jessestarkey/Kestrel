## Design Intent
Every user-facing application serves all of its own client code from KESTREL, with no third-party scripts, fonts, or analytics, and content security policies block anything else. Every provider-hosted service an application calls goes into an inventory before release, with the data it receives, the credential it uses, and its residency. Residency stays within the SA-9(5) parameter CCSD tailoring action 5 sets. Today those are the foundation model deployment, the managed databases, the event streams, and the rights protection service in the Microsoft 365 DoD tenant.

## External Dependencies
The IL5 cloud provider and KESTREL's Microsoft 365 DoD tenant, whose hosted services the inventory records.
