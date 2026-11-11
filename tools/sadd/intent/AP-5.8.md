## Design Intent
The secrets present in every deployed environment are enumerated and reconciled against what each spoke's vault issued. A secret nobody issued, or one nothing has used since its last rotation, is flagged for removal.

## External Dependencies
None outside the boundary.
