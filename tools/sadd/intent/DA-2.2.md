## Design Intent
Every service KESTREL terminates accepts only TLS 1.2 or later, with TLS 1.3 preferred and CNSA cipher suites. Service-to-service connections use mutual TLS with program PKI certificates, and user-facing edge services present DoD PKI server certificates. Provider-managed endpoints present the provider's certificates under its minimum TLS setting. Plaintext connection attempts are blocked and logged.

## External Dependencies
None outside the boundary.
