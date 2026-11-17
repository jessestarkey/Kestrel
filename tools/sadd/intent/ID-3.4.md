## Design Intent
Use mutual TLS with program PKI certificates on every service-to-service connection between KESTREL's own workloads, including across the circuits and into the feedback endpoints that accept IL6 products. Each internal service trusts only the program's issuing authorities. The partner API also trusts the partner and ECA issuers on External PKI Trust and Sponsorship (`ID-1.2`)'s trust list, so partner systems authenticate there with mutual TLS. Provider-managed services authenticate callers by workload identity under Cloud Workload Identities (`ID-3.1`). User-facing edge services present DoD PKI server certificates that browsers and partner systems already trust.

## External Dependencies
External Certificate Authorities and partner PKIs, whose issuers the partner API trusts.
