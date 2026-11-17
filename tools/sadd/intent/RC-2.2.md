## Design Intent
Backups are encrypted in transit and at rest under KESTREL-controlled keys rooted in the HSMs. Each backup set has its own data key, so destroying one key sanitizes one set without touching the rest. Each mission team's zone is backed up under its own key and vault, so a restore lands only in that team's zone. Backup keys are escrowed under split knowledge and rotated on a cadence the KMP sets against the longest retention.

## External Dependencies
None outside the boundary.
