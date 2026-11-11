## Design Intent
Candidates are evaluated in a disposable environment in ML Dev/Test, which has no route to any prod spoke. The held-out evaluation data is readable only by the evaluation pipeline, so no one tuning a model can see it.

## External Dependencies
None outside the boundary.
