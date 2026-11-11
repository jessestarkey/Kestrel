## Design Intent
Managed services that support it are injected into their spoke's subnets, so their traffic follows the hub's routes and inspection. Edge listeners exist only in the DMZ. Mission team services publish only internal listeners, which the DMZ's edge services reach through the cloud hub. The Platform Team reviews internal connections each quarter and removes any that no longer match a documented flow.

## External Dependencies
The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization.
