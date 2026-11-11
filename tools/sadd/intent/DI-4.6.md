## Design Intent
Cloud configuration checks watch every platform service against its baseline. The checks with the highest priority are a re-enabled public endpoint and the foundation model's provider-side prompt logging being turned back on. The same checks cover how each application is hosted, and findings appear on the platform and application compliance dashboard.

## External Dependencies
The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization. The provider exposes the configuration state these checks read.
