## Design Intent
The pipeline combines each model's results across jailbreak, injection, evasion, poisoning, out-of-distribution, and privacy tests into one score against the thresholds of each use case it serves. A model already certified takes only the new use case's acceptance tests when it gains one. Retraining within the approved envelope passes on that score alone, except for edge models, which always take full Certification to Field. Anything outside the envelope goes to the PMO ISSE, and any risk acceptance routes under RK-1.4.

## External Dependencies
None outside the boundary.
