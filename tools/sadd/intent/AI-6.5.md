## Design Intent
The pipeline combines each model's results across jailbreak, injection, evasion, poisoning, out-of-distribution, and privacy tests into one score against its risk tier's thresholds. Retraining within the approved envelope passes on that score alone, except for edge models, which always take full Certification to Field. Anything outside the envelope goes to the PMO ISSE, and any risk acceptance routes under RK-1.4.

## External Dependencies
None outside the boundary.
