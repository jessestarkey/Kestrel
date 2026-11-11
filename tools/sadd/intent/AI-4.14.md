## Design Intent
Every trained artifact is signed as the pipeline's last step, with keys held in the HSMs, and the signature binds the artifact to its run record and dataset snapshot. Serving platforms and aircraft load only signed artifacts.

## External Dependencies
None outside the boundary.
