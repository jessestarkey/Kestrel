## Design Intent
The backup platform protects every supported service class automatically, including virtual machines, cloud databases with point-in-time restore, storage, the directory, the data lake, and the model registry. Cloud services are protected by the provider's native backup, kept immutable and copied to the second region. Schedules and retention come from each resource's tier, and both the pipeline and the configuration automation platform bind each resource to its tier. Infrastructure as code is backed up with its repository.

## External Dependencies
The IL5 cloud provider, whose native backup service and second IL5 region KESTREL relies on under its provisional authorization.
