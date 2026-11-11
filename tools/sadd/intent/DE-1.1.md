## Design Intent
The cloud provider's native detection services are on for every subscription, cluster, database, storage service, and the tenant, and the directory's own threat detection is on in the data center. The Security Team reviews their coverage against MITRE ATT&CK each quarter and tunes noisy alerts. Gaps they find go to custom rules in the security monitoring platform. The CSSP's analysts read the native detection consoles directly through their host pool.

## External Dependencies
The IL5 cloud provider, whose native detection and logging services KESTREL inherits under its provisional authorization. The CSSP, which reads the native detection consoles.
