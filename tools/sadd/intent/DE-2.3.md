## Design Intent
Every cluster's API server audit log, container runtime events, and image pull records go to the security monitoring platform. So do registry push, tag, promotion, and deletion events and each workload's deployed digest. The pipeline enables these when it creates a cluster, and a policy-as-code check flags any cluster that later loses them. The managed training service sends its compute logs through its own diagnostic settings.

## External Dependencies
None outside the boundary.
