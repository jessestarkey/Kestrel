## Design Intent
Each team's pipeline identity reaches only its own repositories, its own registry namespace, and its own dev/test spoke. The Data Team builds and tests in Platform Dev/Test, on synthetic samples only. Only the release identity can deploy to a release target. These are the prod spokes (F5), the edge release path (F6), and the IL6 transfer gateway (F12). F35's on-premises targets are the data center's application hosts, the IT/OT DMZ, the security monitoring platform, and the firewalls. It acts only after Certification to Field approves the release. Build infrastructure access is reviewed twice a year.

## External Dependencies
None outside the boundary.
