Every feed will be tagged with its origin at ingest, and ingest rejects any feed missing from the Data Team's source register. Feeds include aircraft recordings, federated updates, analyst corrections, IL6 releases, and prior collection. Provenance goes to an append-only ledger in immutable storage, whose entries are hash-chained and signed, so an edit by any administrator is detectable.

From Phase 2, training snapshots and partner releases verify a record's provenance before they use it. Data of unknown origin therefore never trains a model or reaches a partner.
