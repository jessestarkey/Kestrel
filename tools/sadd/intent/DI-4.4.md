## Design Intent
Configuration scans compare every virtual machine, VDI desktop, and cluster against its baseline, reading the cloud provider's configuration state, and admission control rejects workloads that depart from the cluster baseline. Drift alerts go to the owning team and the Security Team. A compute compliance dashboard shows posture by team and spoke for the Platform Team, the Security Team, the CSSP, and the PMO ISSE.

## External Dependencies
The IL5 cloud provider, whose configuration state these scans read.
