## Design Intent
Each team maps the flows its workloads need, and those flows become allow rules on workload security groups, with everything else denied. Inside each cluster, Kubernetes network policies deny traffic between namespaces by default. Flow logs feed the security monitoring platform, which flags rules nothing has used for 90 days. The penetration testers try to cross the vendor split and the dev/test to prod deny at every engagement.

## External Dependencies
The penetration testing provider, which tests segmentation and exfiltration paths under each engagement's rules of engagement.
