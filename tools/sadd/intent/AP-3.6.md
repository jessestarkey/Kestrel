## Design Intent
Coverage-guided fuzzing targets every parser that takes untrusted input. These include the feedback endpoints that accept released products from the IL6 enclave, the partner API, and the ingest code that parses each payload vendor's raw formats. Fuzzing runs on each change to those parsers and continuously on the pipeline's runners. Vendor-format parsers are fuzzed in Platform Dev/Test from synthetic samples, so raw vendor data never leaves its zone.

## External Dependencies
None outside the boundary.
