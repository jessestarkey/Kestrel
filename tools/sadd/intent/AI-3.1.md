## Design Intent
Experimentation workspaces in ML Dev/Test give each data scientist an individual notebook server, scoped to the datasets they are approved for. They are reached only from the ML VDI host pool, so notebook output renders inside the session and never on the laptop. Downloads are disabled, servers end after a set lifetime, and the workspaces have no route to any prod spoke beyond F25's shared services.

## External Dependencies
The performer, whose CMMC Level 2 laptops display the ML host pool's sessions under the interconnection agreement.
