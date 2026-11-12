## Design Intent
Keep break-glass accounts for the cloud tenant, the directory, and the ground segment. The two cloud accounts use different phishing-resistant methods. The directory set holds a domain account, each domain controller's Directory Services Restore Mode password, and a local administrator for each privileged access workstation, and every station has its own local account. All of those are console-only passwords under CCSD tailoring action 6, since their recovery cannot depend on the PKI or the directory they may be recovering. Cloud and directory sets are sealed in the data center and at the alternate site, and each station's account at its operating site, since an identity outage must never stop operators from recovering an airborne aircraft.

## External Dependencies
None outside the boundary.
