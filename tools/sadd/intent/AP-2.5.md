## Design Intent
Every image the pipeline builds is scanned before it is pushed to the registry, and the registry rescans stored images as new vulnerability data arrives. Images above the ASP's severity threshold cannot be pushed or deployed.

## External Dependencies
None outside the boundary.
