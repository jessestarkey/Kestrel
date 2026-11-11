## Design Intent
The cloud spokes can be rebuilt in the cloud provider's second IL5 region from infrastructure as code and the replicated backups. The data center's Tier 1 services fail over to a warm standby at the alternate site, so identity and the PKI keep working if the data center is lost. A full failover exercise runs each year and a contingency plan tabletop runs each half year, and their findings update the CP.

## External Dependencies
The IL5 cloud provider, whose native backup service and second IL5 region KESTREL relies on under its provisional authorization. The parent organization, which hosts KESTREL's alternate site under a facility agreement.
