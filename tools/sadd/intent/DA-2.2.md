## Design Intent
Every service accepts only TLS 1.2 or later, with TLS 1.3 preferred, using the approved cipher suites. Service-to-service connections use mutual TLS with program PKI certificates. Plaintext connection attempts are blocked and logged.

## External Dependencies
None outside the boundary.
