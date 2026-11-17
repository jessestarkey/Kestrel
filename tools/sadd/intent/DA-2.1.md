## Design Intent
Each data lake zone encrypts under its own key, which the record's owning team or vendor label selects. A workload that escapes the network controls still cannot read another team's or vendor's data. Personal fields in KESTREL-built databases are encrypted at the column level, and the service desk database uses transparent encryption under a customer-managed key. Scans confirm that every labeled record sits under the key its label requires.

## External Dependencies
None outside the boundary.
