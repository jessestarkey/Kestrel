## Design Intent
Coverage-guided fuzzing targets every parser that takes untrusted input. These include the feedback endpoints that accept released products from the IL6 enclave, the partner API, and the ingest code that parses each payload vendor's raw formats. Fuzzing runs on each change to those parsers and continuously in the dev/test spokes.

## External Dependencies
None outside the boundary.
