## Design Intent
Every build records its base image and digest, and the lineage report shows how far each base has fallen behind its upstream. Base images are the Platform Team's hardened ones from the package mirror. A base past end of life fails the build.

## External Dependencies
The public image sources the hardened base images derive from.
