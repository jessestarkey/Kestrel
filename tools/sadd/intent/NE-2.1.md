## Design Intent
Every provider-managed service, including the foundation model, the spoke vaults, and the portal database, is reached only through a private endpoint in its own spoke, with public access disabled. Configuration checks alert if public access returns. The dedicated circuit terminates on the cloud hub and the data center hub. Its routing sessions are authenticated, and prefix filters accept only KESTREL's own address ranges.

## External Dependencies
The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization. The provider supplies the private endpoint service and the dedicated circuit's cloud side.
