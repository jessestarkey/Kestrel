## Design Intent
Backup coverage follows three criticality tiers. Tier 1 holds every service whose loss stops identity, signing, release, or flight control. Today those are the identity provider, the PKI, the privileged access platform, the hubs' rule base, the ground segment's configuration, and the spoke secrets vaults. The source repository, pipeline configuration, and artifact and model registry are Tier 1 too. HSM key backups go only to the standby HSM at the alternate site, wrapped, and never enter the backup platform. That keeps CCSD row 17 at Moderate confidentiality. Tier 2 holds the data lake, the mission teams' applications and databases, the service desk, and the security monitoring platform. Tier 3 holds dev/test, training scratch, and experimentation. Gaps are recorded with an owner and a disposition, and coverage is re-reviewed on every significant change and each year.

## External Dependencies
None outside the boundary.
