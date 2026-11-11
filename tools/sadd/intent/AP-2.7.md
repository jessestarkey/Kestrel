## Design Intent
The package mirror in Platform Prod is the only source builds resolve from, and the hub blocks every other route to public package indexes. Each ecosystem's proxy draws only from its approved upstream indexes. KESTREL's internal package names are reserved in the mirror, so a public package with the same name cannot replace one.

## External Dependencies
The public package indexes and image sources the mirror draws from.
