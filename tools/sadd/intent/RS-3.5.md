## Design Intent
The likeliest spill is classified content arriving through a high-to-low product, or pasted into a language model prompt, which the content filters are tuned to catch. The ISSM traces every copy, including index entries, embeddings, model training snapshots, and backups. The ISSM then suspends access to them and has each one sanitized. The ISSM reports the spill to the AO, the PSO, and the IL6 enclave's owner.

## External Dependencies
The IL6 enclave's owner, whose release review and security office join any spill traced to a high-to-low product. The PSO, who receives every spill report.
