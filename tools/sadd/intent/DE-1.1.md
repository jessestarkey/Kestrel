## Design Intent
The cloud provider's native detection services are on for every subscription, cluster, database, storage service, and the tenant. The directory's own threat detection is on in the data center and at the alternate site. Each quarter, the Security Team reviews their coverage against MITRE ATT&CK and tunes noisy alerts through detection content in the pipeline. Gaps they find go to custom rules in the security monitoring platform. The CSSP's analysts read the native detection consoles directly through their host pool.

## External Dependencies
The IL5 cloud provider, whose native detection and logging services KESTREL inherits under its provisional authorization. KESTREL's Microsoft 365 DoD tenant, whose endpoint and identity detection it inherits at IL5. The CSSP, which reads the native detection consoles.
