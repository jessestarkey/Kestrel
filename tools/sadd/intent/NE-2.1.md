## Design Intent
Every provider-managed service is reached only through a private endpoint in its own spoke, with public access disabled. That includes the foundation model, the spoke vaults, and the portal database. Configuration checks alert if public access returns. Both dedicated circuits terminate on the cloud hub, one on the data center hub and one on the alternate site firewall. The carrier path is not trusted, so traffic crosses each circuit inside encrypted tunnels between the firewalls. Its routing sessions are authenticated, and prefix filters accept only KESTREL's own address ranges.

## External Dependencies
The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization. The provider supplies the private endpoint service and the dedicated circuit's cloud side.
