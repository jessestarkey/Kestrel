## Design Intent
Before certification, each model's rollback is rehearsed in stage, and so is its kill switch. Cloud endpoints fall back to the prior certified version, and AI agents are disabled. For edge models, the rehearsal runs on a spare aircraft, which falls back to its stored prior model or turns onboard detection off. The cutover times are compared with the recovery time the model committed to, and a model that misses it is not promoted.

## External Dependencies
None outside the boundary.
