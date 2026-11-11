## Design Intent
Every feed is tagged with its origin at ingest, and provenance is written to an append-only log the Data Team cannot edit. Feeds include aircraft recordings, federated updates, analyst corrections, and products released from the IL6 enclave. Training snapshots and partner releases verify provenance before they use a record, so data of unknown origin never trains a model or reaches a partner.

## External Dependencies
None outside the boundary.
