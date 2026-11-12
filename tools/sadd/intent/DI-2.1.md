## Design Intent
Every cloud resource is created by infrastructure as code through the shared pipeline from the Platform Team's landing zone modules. Those modules set secure defaults, and policy-as-code checks block a resource that departs from them. A second reviewer approves each infrastructure change, as with application code. Console creation is denied outside break-glass. Data center and alternate site servers are built from the same kind of templates through the configuration automation platform.

## External Dependencies
The parent organization's facility, which hosts the alternate site's equipment under the facility agreement.
