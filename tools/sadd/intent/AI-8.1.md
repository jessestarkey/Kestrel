## Design Intent
Model endpoints in ML Prod accept calls only from approved mission team workloads, and each caller's query pattern is baselined. Systematic sweeps that look like extraction alert the ML team and the Security Team. The partner API's query volume per partner is watched the same way, since its detections reveal model behavior.

## External Dependencies
None outside the boundary.
