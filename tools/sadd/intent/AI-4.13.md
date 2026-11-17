## Design Intent
Every training environment pins its dependency versions and image digest. Each run hashes its assembled environment at start, compares it with the pipeline's approved baseline, and halts on a mismatch. The verified hash goes in the run record and the AI-BOM. Sampled reproduction of runs belongs to Experiment Tracking and Reproducibility (`AI-3.2`).

## External Dependencies
None outside the boundary.
