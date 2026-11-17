## Design Intent
The package mirror in Platform Prod is the only source builds resolve from, and the hub blocks every other route to public package indexes. The mirror fetches only over F30, from each ecosystem's approved upstream, and checks each publisher's digest or signature before caching. Newly published versions wait out a quarantine window before builds may use them. KESTREL's internal package names are reserved in the mirror, so a public package with the same name cannot replace one.

## External Dependencies
The public package indexes and image sources the mirror draws from.
