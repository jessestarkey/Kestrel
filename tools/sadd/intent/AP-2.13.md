## Design Intent
The pipeline signs every image and release package automatically, with keys held in the HSMs. Admission control in every cluster rejects an unsigned image or one signed by any other key. The ground control stations and aircraft verify each edge model package's signature before loading it.

## External Dependencies
None outside the boundary.
