## Design Intent
The owning team carries out eradication at the ISSM's direction, and Fleet Operations does so only in a maintenance window or after landing. Eradication removes the adversary's persistence, rotates every credential and secret the incident touched, and verifies the exploited weakness is closed before the incident can close. A compromised model version is withdrawn, and the registry blocks any rollback to it. A compromised signing key is revoked under the KMP, every package it signed is re-certified and re-signed, and aircraft are reloaded in maintenance windows. A lost aircraft's datalink keys are always superseded fleet-wide under Certificate Lifecycle and Revocation (`DA-3.9`).

## External Dependencies
None outside the boundary.
