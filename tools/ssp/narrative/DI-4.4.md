From Phase 2, every virtual machine, VDI desktop, and cluster will be compared against its baseline. In the cloud, Azure Machine Configuration and Defender for Cloud CSPM read each machine's configuration state. In the data center and at the alternate site, ACAS runs STIG audits. Inside the clusters, Gatekeeper rejects any workload that departs from the cluster baseline before it runs.

Drift alerts go to the owning team and the Security Team. A Splunk dashboard shows compute posture by team and spoke for the Platform Team, the Security Team, the PMO ISSE, and the CSSP.
