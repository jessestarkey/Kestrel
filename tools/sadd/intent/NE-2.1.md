## Design Intent
Every provider-managed service is reached only through a private endpoint in its own spoke, with public access disabled. That includes the foundation model, the spoke vaults, and the portal database. Configuration checks alert if public access returns. Three dedicated circuits ride DISN through the Boundary Cloud Access Point to the cloud hub. The data center hub has two, from different carriers on diverse paths to different meet-me points, and the alternate site firewall has one. The carrier path is not trusted, so traffic crosses each circuit inside encrypted tunnels between the firewalls. Routing sessions are authenticated, and prefix filters accept only KESTREL's own ranges.

## External Dependencies
The IL5 cloud provider, which supplies the private endpoint service and the circuits' cloud side under its provisional authorization. DISA, which carries the circuits over DISN through the access point. The circuit carriers.
