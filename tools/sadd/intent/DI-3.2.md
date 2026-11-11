## Design Intent
One VDI golden image serves every host pool, and each pool adds only its own tools. Virtual machine images cover the experimentation workspaces, the payload vendors' conversion servers, and the data center's other servers. Container base images are hardened and minimal, built from the package mirror, and rebuilt rather than patched in place. Every managed Kubernetes cluster shares one baseline, whether it is a dev, test, stage, prod, or training cluster. BMC hardening applies to the data center's physical servers.

## External Dependencies
The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization. The provider hardens the cloud's physical hosts and their management controllers.
