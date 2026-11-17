## Design Intent
Define privileged roles for each administrative surface, namely the cloud hub, each spoke, the cluster control planes, the data center, the alternate site, the PKI and HSMs, and the ground segment. In the cloud, a team gets administrative roles only once it runs its own production spoke. On premises, each owning team holds the roles for the systems it runs, such as Fleet Operations for the ground segment. Tier 0 roles go only to the named Tier 0 administrators. The Security Team and the CSSP get read and audit roles. Their stated exceptions are the EDR responder role, the logging administrator role, and the detection content role, which deploys detection rules through the pipeline. Containment playbooks run by the Security Team or the CSSP are the last exception. No single role spans the HSMs and the cloud tenants.

## External Dependencies
None outside the boundary.
