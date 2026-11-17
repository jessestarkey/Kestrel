## Design Intent
Every feed is tagged with its origin at ingest, and ingest rejects any feed missing from the Data Team's source register. Feeds include aircraft recordings, federated updates, analyst corrections, IL6 releases, and prior collection over F28. Provenance goes to an append-only ledger whose entries are hash-chained and signed, so an edit by any administrator is detectable. Training snapshots and partner releases verify provenance before they use a record, so data of unknown origin never trains a model or reaches a partner.

## External Dependencies
None outside the boundary.
