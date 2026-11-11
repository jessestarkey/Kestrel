## Design Intent
Backups are encrypted in transit and at rest under KESTREL-controlled keys rooted in the HSMs. The backup keys are escrowed under split knowledge as the KMP requires, so losing a key never means losing the backups.

## External Dependencies
None outside the boundary.
