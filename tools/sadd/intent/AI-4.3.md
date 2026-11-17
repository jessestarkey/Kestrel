## Design Intent
The training cluster sits in ML Dev/Test, which the cloud hub isolates from every prod spoke. It reaches only F25's shared services, pulling images and approved checkpoints from the registry and mirror, and the ML training zone across the circuit. Trained weights leave only when the release runners collect them, so neither the corpus nor the weights have another way out. Any transfer from the cluster sized like a corpus or a set of weights alerts the Security Team.

## External Dependencies
None outside the boundary.
