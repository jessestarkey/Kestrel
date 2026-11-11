## Design Intent
Every backup is locked against change or deletion until its retention expires, even by a fully privileged account. Copies leave the data center on two paths. One goes to the alternate site, and the other goes to immutable storage in the cloud provider's second IL5 region, so no single site or region holds every copy.

## External Dependencies
The IL5 cloud provider, whose native backup service and second IL5 region KESTREL relies on under its provisional authorization. The parent organization, which hosts KESTREL's alternate site under a facility agreement.
