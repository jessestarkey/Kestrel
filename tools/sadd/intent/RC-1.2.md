## Design Intent
The backup platform protects every supported service class automatically, including virtual machines, cloud databases, storage, the directory, the data lake, and the model registry. Schedules and retention come from each resource's tier. Infrastructure as code is backed up by its repository, so rebuilding is a pipeline run.

## External Dependencies
The IL5 cloud provider, whose native backup service and second IL5 region KESTREL relies on under its provisional authorization.
