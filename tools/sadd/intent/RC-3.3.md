## Design Intent
A region rebuild starts by restoring the repository and pipeline runners in the cloud provider's second IL5 region from backup. It then runs the landing zone modules to rebuild the cloud spokes, and the circuits are re-homed to a hub there. The data center's Tier 1 services fail over to warm standbys at the alternate site, namely identity, the PKI, DNS, and the privileged access platform. Its other Tier 1 services are restored in the second IL5 region within Tier 1's recovery time. Recovery runs from the alternate site's privileged access workstations, on break-glass accounts if needed. A full failover exercise runs each year and a contingency plan tabletop each half year, and their findings update the CP.

## External Dependencies
The IL5 cloud provider, whose native backup service and second IL5 region KESTREL relies on under its provisional authorization. The parent organization, which hosts KESTREL's alternate site under a facility agreement.
