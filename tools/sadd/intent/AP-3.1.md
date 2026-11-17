## Design Intent
Dev, test, and stage clusters in the mission team and Platform dev/test spokes run on synthetic or sanitized data, never live mission data. The Data Team produces the sanitized sets by removing incidental imagery of people and anything identifying a source. ML Dev/Test is the one exception, holding live mission data under Secure Experimentation Environment (`AI-3.1`) and F18's release approval. Stage carries production's configuration but not production's data.

## External Dependencies
None outside the boundary.
