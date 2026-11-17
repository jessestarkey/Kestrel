## Design Intent
Before the ATO, training data is government-furnished prior collection the AO admits under the interim authorization to test, received over F28, plus synthetic and simulator data. After it, training data comes only from KESTREL's own collection, analyst corrections, federated updates from the aircraft, and IL6 releases. The Data Team screens every batch for provenance, outliers, duplicates, and label shifts before it enters the ML training zone. A flagged batch is held automatically and any run that would read it fails. A new external dataset needs AI intake first.

## External Dependencies
None outside the boundary.
