## Design Intent
Before certification, each model's rollback is rehearsed in stage, and so is its kill switch: cloud endpoints fall back to the prior certified version, and AI agents are disabled. For edge models, the rehearsal runs on a spare aircraft, which falls back to its stored prior model or turns onboard detection off. The cutover times are recorded in the evidence.

## External Dependencies
None outside the boundary.
