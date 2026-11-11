## Design Intent
The pipeline combines each model's results across jailbreak, injection, evasion, poisoning, out-of-distribution, and privacy tests into one score against its risk tier's thresholds. Retraining within the approved envelope passes on that score alone. Anything outside it goes to the PMO ISSE for a decision.

## External Dependencies
None outside the boundary.
