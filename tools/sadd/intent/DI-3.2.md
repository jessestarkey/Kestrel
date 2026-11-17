## Design Intent
One VDI golden image serves every host pool, and each pool adds only its own tools. Virtual machine images cover the signals conversion server and every other on-premises server. Container base images are hardened and minimal, built from the package mirror, and rebuilt rather than patched in place. Every managed Kubernetes cluster shares one baseline, whether it is a dev, test, stage, prod, notebook, or serving cluster. Every cloud virtual machine and node pool is separated from non-DoD tenants, as the Cloud Computing SRG requires at IL5. BMC hardening applies to every physical server.

## External Dependencies
The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization. The provider hardens the cloud's physical hosts and their management controllers.
