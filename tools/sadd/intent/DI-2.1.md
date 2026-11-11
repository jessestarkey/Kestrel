## Design Intent
Every cloud resource is created by infrastructure as code through the shared pipeline from the Platform Team's landing zone modules. Those modules set secure defaults, and policy-as-code checks block a resource that departs from them. A second reviewer approves each infrastructure change, as with application code. Console creation is denied outside break-glass, and data center servers are built from the same kind of templates through the SDN controller and privileged access platform.

## External Dependencies
None outside the boundary.
