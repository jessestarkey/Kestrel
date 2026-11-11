## Design Intent
The Security Team takes every endpoint response action, namely isolation, file remediation, and live response, under the IRP. Live response sessions are recorded. The CSSP correlates detections and recommends actions but holds no response rights, which matches its read-only host pool. Automated response is limited to isolating a non-production host, and a production host is isolated only with its owning team told at once.

## External Dependencies
The CSSP, under the detection and response split in its service agreement.
