## Design Intent
Intrusion detection runs on sensors fed by the SDN fabric's mirrored traffic and the alternate site's internal paths, covering what the cloud hub never sees. In the ground segment, the passive sensors' anomaly detection is the intrusion detection. The CSSP triages first. Platform Team network engineers adjudicate IT alerts, and Fleet Operations' OT maintainers adjudicate ground segment ones. Evidence is captured at triage before sensor buffers roll, and the IRP sets when an anomaly becomes an incident.

## External Dependencies
The CSSP, which triages network alerts around the clock.
