## Design Intent
Every backup is locked against change or deletion until its retention expires, even by a fully privileged account. A spill caught in a locked copy is sanitized by destroying that backup set's key. Copies leave the data center on two paths, to the alternate site and to immutable storage in the cloud provider's second IL5 region, so no single site or region holds every copy. While the cloud hub is down, the data center keeps local copies and the alternate site's standby runs on its last replication.

## External Dependencies
The IL5 cloud provider, whose native backup service and second IL5 region KESTREL relies on under its provisional authorization. The parent organization, which hosts KESTREL's alternate site under a facility agreement.
