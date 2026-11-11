## Design Intent
The training cluster sits in ML Dev/Test, which the cloud hub isolates from every prod spoke. Its only outbound paths are the package mirror, the model registry, and the ML training zone across the circuit, so neither the corpus nor the weights have another way out.

## External Dependencies
None outside the boundary.
